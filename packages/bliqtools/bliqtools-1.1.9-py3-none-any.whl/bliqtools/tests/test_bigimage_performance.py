"""
Perfomance Unit tests for BigImage, a class to manipulate very large images
"""

import unittest
import cProfile
from multiprocessing import Pool, cpu_count
from collections import deque
import shutil
from pathlib import Path
from threading import Thread
import tempfile

import numpy as np
import tifffile
import psutil

from bliqtools import envtest
from bliqtools.nirvana import FilePath
from bliqtools.bigimage import BlockEntry, BigImage
from bliqtools.testing import MemoryMonitor, TimeIt, Progress


class TestRGBBigImage(envtest.TestCaseBigImage):  # pylint: disable=too-many-public-methods
    """
    Several tests for BigImage and understanding its details
    """

    @classmethod
    def setUpClass(cls):
        """
        Create a very large dataset for testing
        """
        super().setUpClass()

        cls.dataset_very_big = Path(cls.img_test_data, "very_big")
        shutil.rmtree(cls.dataset_very_big, ignore_errors=True)
        cls.dataset_very_big.mkdir(parents=True, exist_ok=True)

        _, _, free, _ = psutil.disk_usage("/")
        estimated_size = cls.estimate_dataset_size(
            shape=(2048, 2048), map_size=(17, 17, 10), dtype=np.uint8
        )
        # We need twice because we will save combined layers, should be about same total size
        if free > 2.1 * estimated_size:
            cls.create_dataset(
                directory=cls.dataset_very_big,
                shape=(2048, 2048),
                map_size=(17, 17, 10),
            )
        elif free > estimated_size * 0.2:
            print(
                "Low on disk space, creating a 'somewhat large' dataset, but only 1 layers (half the big size)"
            )
            cls.create_dataset(
                directory=cls.dataset_very_big, shape=(2048, 2048), map_size=(17, 17, 1)
            )
        else:
            cls.fail(
                "You are too low on disk space, not really possible to create a significant dataset"
            )

    @classmethod
    def estimate_dataset_size(cls, map_size, shape, dtype):
        """
        Try to estimate to required memory for the tests
        """
        return np.prod(map_size) * np.prod(shape) * np.iinfo(dtype).bits // 8

    @classmethod
    def tearDownClass(cls):
        """
        We always delete dthis very large dataset on the way out.
        """
        super().tearDownClass()
        shutil.rmtree(cls.dataset_very_big, ignore_errors=True)

    def setUp(self):
        """
        Display what is running since many tests output text to the console and are very lengthy
        """
        print(f"\n# Current test : {self.current_test_name()}")

    def test_10_preview32_from_very_large_dataset_attempt(self):
        """
        This assumes a very large dataset at path self.dataset_very_big, with Nirvana-style tiles.
        We work with the first layer only. We try to see the performance for a preview of factor=32
        """
        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()
        layer1_filepaths = [filepath for filepath in filepaths if filepath.k == 1]
        _, _, _, w, h, _ = self.cheap_tile_loader_knock_off(layer1_filepaths)

        img = BigImage()
        with TimeIt(description="Real dataset"):
            with Progress(total=len(layer1_filepaths)) as p:
                for filepath in layer1_filepaths:
                    pixel_x = (filepath.i - 1) * w
                    pixel_y = (filepath.j - 1) * h

                    entry = BlockEntry(
                        coords=(pixel_x, pixel_y), data=None, image_filepath=filepath
                    )
                    img.add_entry(entry)
                    p.next()
            with cProfile.Profile() as profiler:
                with MemoryMonitor():
                    preview = img.get_reduced_resolution_preview(factor=32)
                    profiler.print_stats("time")

        self.save_test_image_result(preview)

    def test_12_tifffile_writes_images_as_tiles(self):
        """
        Tifffile can write "tiled" images. This attempts to use the feature
        to try to see if it means what I think it means, but when the file
        is opened, I see multiple pages, nto a single image.
        Not sure what to do with this.
        """
        data = np.random.rand(2, 5, 3, 301, 219).astype("float32")
        with tempfile.TemporaryDirectory() as td:
            tifffile.imwrite(
                Path(td, "temp.tif"),
                data,
                bigtiff=True,
                photometric="rgb",
                planarconfig="separate",
                tile=(32, 32),
                compression="zlib",
                compressionargs={"level": 8},
                predictor=True,
                metadata={"axes": "TZCYX"},
            )

    def test_13_get_fast_preview_from_cache(self):
        """
        When loading entries directly with data, the BlockEntry class
        will keep a preview reduced by a factor 16.  Making the preview will be really fast

        """

        BlockEntry.use_cache_previews = True

        img = BigImage()
        with TimeIt():
            with Progress(total=100, description="Tile") as p:
                for i in range(10):
                    for j in range(10):
                        small_block = np.full(
                            shape=(1_024, 1_024), fill_value=10 * i + j, dtype=np.uint8
                        )
                        img.add_block(coords=(i * 2048, j * 2048), data=small_block)
                        p.next()

        preview = img.get_reduced_resolution_preview(factor=32)
        self.save_test_image_result(preview)

        BlockEntry.use_cache_previews = False

    def test_14_compute_previews_in_parallel(self):
        """
        Could we compute many previews in the background and save time?
        This assumes a dataset at path, with Nirvana-style tiles.
        We work with the first layer only.

        Short answer: using Pool() is not possible with our class. Leaving it
        for educational purposes.
        """

        root_dir = FilePath(Path.home(), self.dataset_very_big)
        filepaths = root_dir.contents()
        layer1_filepaths = [filepath for filepath in filepaths if filepath.k == 1]
        _, _, _, w, h, _ = self.cheap_tile_loader_knock_off(layer1_filepaths)

        img = BigImage()

        for filepath in layer1_filepaths:
            pixel_x = (filepath.i - 1) * w
            pixel_y = (filepath.j - 1) * h

            entry = BlockEntry(
                coords=(pixel_x, pixel_y), data=None, image_filepath=filepath
            )
            img.add_entry(entry)

        with TimeIt():
            for entry in img.entries:
                compute_previews(entry)

        with self.assertRaises(TypeError):
            with TimeIt():
                with Pool(5) as p:
                    p.map(
                        compute_previews, img.entries
                    )  # This will fail with a TypeError because of Pickle

    def test_25_from_very_large_dataset(self):  # pylint: disable=too-many-locals
        """
        The ultimate test: a very large 3D dataset.
        """
        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()

        _, _, nk, w, h, _ = self.cheap_tile_loader_knock_off(filepaths)
        overlap = 250
        mask = None
        with tempfile.TemporaryDirectory() as td, TimeIt(
            description="Real dataset building with mask (single thread)"
        ), Progress(description="Completing layer", total=nk) as p:
            for k in range(1, nk + 1):
                img = BigImage()
                layer_k_filepaths = [
                    filepath for filepath in filepaths if filepath.k == k
                ]
                for filepath in layer_k_filepaths:
                    pixel_x = (filepath.i - 1) * (w - overlap)
                    pixel_y = (filepath.j - 1) * (h - overlap)

                    entry = BlockEntry(
                        coords=(pixel_x, pixel_y),
                        data=None,
                        image_filepath=filepath,
                    )

                    if mask is None:
                        mask = entry.linear_overlap_mask(overlap_in_pixels=overlap)

                    entry.apply_mask(mask)
                    img.add_entry(entry)
                p.next()

                preview = img.get_reduced_resolution_preview(factor=1)
                tifffile.imwrite(Path(td, f"Layer-{k}.tif"), preview, bigtiff=True)

                self.save_test_image_result(preview)

    def test_26_from_real_3d_dataset_one_big_tiff(self):  # pylint: disable=too-many-locals
        """
        Again with a large 3D dataset, now save all layers in a single TIFF using the
        contiguous=True option and a contextmanager with tifffile ... as tif:
        """
        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()

        _, _, nk, w, h, _ = self.cheap_tile_loader_knock_off(filepaths)
        overlap = 250
        mask = None
        with tempfile.TemporaryDirectory() as td, tifffile.TiffWriter(
            Path(td, "Big_Image.tif"), bigtiff=True
        ) as tif, MemoryMonitor() as m, TimeIt(
            description="Real dataset building with mask"
        ), Progress(
            description="Completing layer",
            total=nk,
        ) as p:
            for k in range(1, nk + 1):
                img = BigImage()
                layer_k_filepaths = [
                    filepath for filepath in filepaths if filepath.k == k
                ]
                for filepath in layer_k_filepaths:
                    pixel_x = (filepath.i - 1) * (w - overlap)
                    pixel_y = (filepath.j - 1) * (h - overlap)

                    entry = BlockEntry(
                        coords=(pixel_x, pixel_y),
                        data=None,
                        image_filepath=filepath,
                    )

                    if mask is None:
                        mask = entry.linear_overlap_mask(overlap_in_pixels=overlap)

                    entry.apply_mask(mask)
                    img.add_entry(entry)
                p.next()

                preview = img.get_reduced_resolution_preview(factor=1)
                tif.write(preview, contiguous=True)
                self.save_test_image_result(preview)

            m.report_stats()

    def test_26_from_real_3d_dataset_save_layers_in_thread(self):  # pylint: disable=too-many-locals
        """
        Is it faster to save in a separate thread?

        Short answer: no.

        """
        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()

        _, _, nk, w, h, _ = self.cheap_tile_loader_knock_off(filepaths)
        overlap = 250
        masks = None
        with tempfile.TemporaryDirectory() as td:
            with MemoryMonitor() as m:
                with TimeIt(description="Real dataset building with mask"):
                    with Progress(
                        description="Completing layer",
                        total=nk,
                        show_count=nk,
                        delay_before_showing=0,
                    ) as p:
                        for k in range(1, nk // 3 + 1):
                            img = BigImage()
                            layer_k_filepaths = [
                                filepath for filepath in filepaths if filepath.k == k
                            ]
                            for filepath in layer_k_filepaths:
                                pixel_x = (filepath.i - 1) * (w - overlap)
                                pixel_y = (filepath.j - 1) * (h - overlap)

                                entry = BlockEntry(
                                    coords=(pixel_x, pixel_y),
                                    data=None,
                                    image_filepath=filepath,
                                )

                                if masks is None:
                                    masks = entry.linear_overlap_masks(
                                        overlap_in_pixels=overlap
                                    )

                                entry.apply_partial_masks(masks)
                                img.add_entry(entry)
                            p.next()

                            preview = img.get_reduced_resolution_preview(factor=1)
                            thread = Thread(
                                target=tifffile.imwrite,
                                args=(Path(td, f"Layer-{k}.tif"), preview),
                                kwargs={"bigtiff": True},
                            )
                            thread.start()

                            self.save_test_image_result(preview)

            m.report_stats()

    def test_27_one_layer_one_thread(self):
        """
        Is it faster to do each layer in its own thread?
        The number of thread is hard to estimate: it depends on available cores and memory.

        """
        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()

        _, _, nk, w, h, _ = self.cheap_tile_loader_knock_off(filepaths)
        overlap = 250
        factor = 1
        thread = None

        available_mem = psutil.virtual_memory().available / 1e9
        approximate_task = available_mem // 2

        with tempfile.TemporaryDirectory() as td:
            for k in range(1, nk + 1):
                layer_filepath = Path(td, f"Layer-{k}.tif")
                layer_k_filepaths = [
                    filepath for filepath in filepaths if filepath.k == k
                ]

                thread = Thread(
                    target=build_one_layer,
                    args=(
                        layer_k_filepaths,
                        k,
                        w,
                        h,
                        overlap,
                        factor,
                        layer_filepath,
                    ),
                )
                thread.start()

                if k % approximate_task == 0:
                    thread.join()

            thread.join()

    def test_29_use_worker_threads_and_deque(self):  # pylint: disable=too-many-locals
        """
        Use worker threads to go through the queue of data to process.
        We allow 4 threads because we have 4 to 8 cores but other processes
        need to run too.
        """

        root_dir = FilePath(self.dataset_very_big)
        filepaths = root_dir.contents()
        _, _, nk, w, h, _ = self.cheap_tile_loader_knock_off(filepaths)
        overlap = 250
        factor = 1

        # First, use same mechanism with a single thread
        with TimeIt() as t1:
            with tempfile.TemporaryDirectory() as td:
                # Fill the queue with data
                queue = deque()  # a deque is MUCH faster and simpler than a Queue
                for k in range(1, nk + 1):
                    layer_k_filepaths = [
                        filepath for filepath in filepaths if filepath.k == k
                    ]
                    layer_filepath = Path(td, f"Layer-{k}.tif")
                    queue.appendleft(
                        (layer_k_filepaths, k, w, h, overlap, factor, layer_filepath)
                    )

                # Start the worker threads
                thread = None
                thread = Thread(target=layer_builder_worker_thread, args=(queue,))
                thread.start()
                thread.join()

        # Then do it again with a small number of threads
        # Assume a laptop with 4 or 8 CPUs
        number_of_threads = cpu_count() // 4
        if cpu_count() - nk >= 2:
            number_of_threads = nk

        with TimeIt() as t2:
            with tempfile.TemporaryDirectory() as td:
                # Fill the queue with data
                queue = deque()  # a deque is MUCH faster and simpler than a Queue
                for k in range(1, nk + 1):
                    layer_k_filepaths = [
                        filepath for filepath in filepaths if filepath.k == k
                    ]
                    layer_filepath = Path(td, f"Layer-{k}.tif")
                    queue.appendleft(
                        (layer_k_filepaths, k, w, h, overlap, factor, layer_filepath)
                    )

                # Start the worker threads
                threads = []
                for _ in range(number_of_threads):
                    thread = Thread(target=layer_builder_worker_thread, args=(queue,))
                    thread.start()
                    threads.append(thread)

                # Wait for completion of all threads
                for thread in threads:
                    thread.join()

        print(f"Single-threaded: {t1.duration:.2f}")
        print(f"Multi({number_of_threads})-threaded: {t2.duration:.2f}")

    def test_30_time_versus_layer_size(self):
        """
        Perform several image reconstruction and output data for further studies of the performance
        versus the various parameters
        """
        for map_width in range(2, 20):
            map_size = (map_width, map_width, 1)

            for shape_width in (128, 256, 512, 1024, 2048):
                shape = (shape_width, shape_width, 3)
                overlap = shape_width // 5
                with tempfile.TemporaryDirectory() as td:
                    root_dir = FilePath(td)

                    self.create_dataset(
                        directory=root_dir, map_size=map_size, shape=shape
                    )

                    filepaths = root_dir.contents()

                    with TimeIt(description=f"{map_width}\t{shape_width}"):
                        img = BigImage()
                        for filepath in filepaths:
                            i = filepath.i
                            j = filepath.j
                            img.add_block(
                                coords=(
                                    i * (shape_width - overlap),
                                    j * (shape_width - overlap),
                                ),
                                image_filepath=filepath,
                            )

                        preview = img.get_reduced_resolution_preview(factor=32)
                        preview.shape  # pylint: disable=unused-variable, pointless-statement


def layer_builder_worker_thread(queue):
    """
    Small worker thread that will take data if available to build one layer,
    ifno data available it quits.
    """
    while True:
        try:
            args = queue.pop()
            # Reusing the same function as previous test
            build_one_layer(*args)
        except IndexError:
            break


def build_one_layer(filepaths, k, w, h, overlap, factor, layer_filepath):  # pylint: disable=too-many-locals
    """
    With all the filepaths making up a layer, this function builds the preview of
    the image at 'factor' reduction and saves it to layer_filepath
    """
    masks = None
    img = BigImage()
    layer_k_filepaths = filepaths
    print(f"Building layer {k}")
    with Progress(total=len(layer_k_filepaths), description=f"Layer {k} progress") as p:
        for filepath in layer_k_filepaths:
            pixel_x = (filepath.i - 1) * (w - overlap)
            pixel_y = (filepath.j - 1) * (h - overlap)

            entry = BlockEntry(
                coords=(pixel_x, pixel_y),
                data=None,
                image_filepath=filepath,
            )

            if overlap > 0:
                if masks is None:
                    masks = entry.linear_overlap_masks(overlap_in_pixels=overlap)

                entry.apply_partial_masks(masks)

            img.add_entry(entry)
            img.purge_if_needed()
            p.next()

    print(f"Starting preview for layer {k} at factor {factor}")
    preview = img.get_reduced_resolution_preview(factor=factor)
    tifffile.imwrite(layer_filepath, preview, bigtiff=True)


def compute_previews(entry):
    """
    Function used in the multiprocessing example
    """
    for factor in [16, 32, 64, 128]:
        preview = entry.get_preview(factor=factor)
        entry.previews[factor] = preview


if __name__ == "__main__":
    # unittest.main()
    unittest.main(defaultTest=["TestRGBBigImage.test_30_time_versus_layer_size"])
