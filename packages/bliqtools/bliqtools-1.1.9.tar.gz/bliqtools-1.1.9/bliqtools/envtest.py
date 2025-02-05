"""
Common functions for testing, especially BigImage
"""

import unittest
import subprocess
from pathlib import Path
import shutil
from contextlib import suppress
import tempfile

import numpy as np
import tifffile
from matplotlib import pyplot as plt


class TestCaseBigImage(unittest.TestCase):  # pylint: disable=too-many-public-methods
    """
    Several methods to create datasets and organize tests for BigImage
    """

    img_graph_path = None
    img_test_data = None

    @classmethod
    def setUpClass(cls):
        cls.img_graph_path = Path(tempfile.gettempdir(), "Graphs")
        Path(cls.img_graph_path).mkdir(parents=True, exist_ok=True)

        cls.img_test_data = Path(tempfile.gettempdir(), "Test_Data")
        cls.dataset_grayscale = Path(cls.img_test_data, "grayscale")
        cls.dataset_rgb = Path(cls.img_test_data, "rgb")

        shutil.rmtree(cls.img_test_data, ignore_errors=True)
        cls.dataset_grayscale.mkdir(parents=True, exist_ok=True)
        cls.dataset_rgb.mkdir(parents=True, exist_ok=True)

        cls.create_dataset(directory=cls.dataset_grayscale, shape=(512, 512))
        cls.create_dataset(directory=cls.dataset_rgb, shape=(512, 512, 3))

    @classmethod
    def tearDownClass(cls):
        """
        We save the graphs into files to avoid blocking the UI.  Open the folder when done (macOS)
        Don't delete: the files are small and need to be inspected after the tests.
        """
        with suppress(Exception):
            subprocess.run(["open", cls.img_graph_path], check=True)
            subprocess.run(["open", cls.img_test_data], check=True)

        shutil.rmtree(cls.img_test_data, ignore_errors=True)

    @classmethod
    def create_dataset(cls, directory, map_size=None, shape=None, dtype=np.uint8):
        """
        A general function to create datasets in temprorary directories that we can access and delete
        later
        """
        if map_size is None:
            map_size = (10, 10, 4)

        if shape is None:
            shape = (512, 512, 3)

        for i in range(map_size[0]):
            for j in range(map_size[1]):
                for k in range(map_size[2]):
                    value = (
                        (
                            (i / map_size[0])
                            + float(j / map_size[1])
                            + float(k / map_size[2])
                        )
                        / 3
                        * np.iinfo(dtype).max
                    )

                    block = np.full(shape=shape, fill_value=value, dtype=np.uint8)
                    # We follow Nirvana's naming conventions (see nirvana.py)
                    filepath = Path(
                        directory,
                        f"test_TEST-VOI_001-X{i + 1:03}-Y{j + 1:03}-Z{k + 1:03}-C1-T001.tif",
                    )
                    tifffile.imwrite(filepath, block)

        return directory

    def current_test_name(self):
        """
        A short name that identifies a test for titles on figures and filenames
        """
        return self.id().split(".")[-1]

    def save_test_image_result(self, img, suffix=""):
        """
        It is often convenient to look at an image in matplotlib but we do not
        want to block the testing.  We save the figure instead of showing it.
        """
        fig, ax = plt.subplots()
        ax.imshow(img, interpolation="nearest")
        ax.set_title(self.current_test_name())
        image_path = Path(
            self.img_graph_path, self.current_test_name() + f"{suffix}.pdf"
        )
        fig.savefig(image_path)
        plt.close(fig)

    def cheap_tile_loader_knock_off(self, filepaths):
        """
        This function mimicks the behaviour of TileLoader because I do not want to import it
        for testing here.

        Returns the number of tiles in i,j,k
        """
        i = set()
        j = set()
        k = set()
        for filepath in filepaths:
            i.add(filepath.i)
            j.add(filepath.j)
            k.add(filepath.k)

        some_filepath = filepaths[0]
        some_entry = tifffile.imread(some_filepath)

        shape = some_entry.data.shape

        w = shape[0]
        h = shape[1]
        c = 1
        if len(shape) == 3:
            c = shape[2]

        return len(i), len(j), len(k), w, h, c

    def test_00_datasetcreation(self):
        """
        A quick test to confirm our dataset function works.
        """
        with tempfile.TemporaryDirectory() as td:
            self.create_dataset(directory=td)


if __name__ == "__main__":
    unittest.main()
