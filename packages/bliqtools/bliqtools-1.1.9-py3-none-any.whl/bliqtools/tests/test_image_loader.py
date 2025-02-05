import unittest
import tempfile
import os
import numpy as np
from PIL import Image
import tifffile
from unittest.mock import patch
from bliqtools.image_loader import ImageLoader


class TestImageLoader(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.tiff_path = os.path.join(self.temp_dir, "test.tif")
        self.jpg_path = os.path.join(self.temp_dir, "test.jpg")
        self.gif_path = os.path.join(self.temp_dir, "test.gif")

        # Create test images
        tifffile.imwrite(self.tiff_path, np.random.rand(100, 100))
        Image.fromarray((np.random.rand(100, 100, 3) * 255).astype("uint8")).save(
            self.jpg_path
        )
        Image.fromarray((np.random.rand(100, 100, 3) * 255).astype("uint8")).save(
            self.gif_path, format="GIF"
        )

        self.file_paths = [self.tiff_path, self.jpg_path, self.gif_path]

    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def test_lazy_load(self):
        loader = ImageLoader(self.file_paths, lazy_load=True)
        self.assertEqual(len(loader.images), 0)  # No images should be loaded initially

        # Load one image
        image = loader.load_image(self.tiff_path)
        self.assertIsNotNone(image)
        self.assertEqual(len(loader.images), 1)

    def test_preload(self):
        loader = ImageLoader(self.file_paths, lazy_load=False)
        self.assertEqual(len(loader.images), 3)  # All images should be loaded

    def test_load_tiff(self):
        loader = ImageLoader([self.tiff_path])
        image = loader.load_image(self.tiff_path)
        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape, (100, 100))

    def test_load_jpg(self):
        loader = ImageLoader([self.jpg_path])
        image = loader.load_image(self.jpg_path)
        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape, (100, 100, 3))

    def test_load_gif(self):
        loader = ImageLoader([self.gif_path])
        image = loader.load_image(self.gif_path)
        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape[:2], (100, 100))

    def test_get_image(self):
        loader = ImageLoader(self.file_paths, lazy_load=False)
        image = loader.get_image(self.tiff_path)
        self.assertIsNotNone(image)

        # Test getting a non-existent image
        self.assertIsNone(loader.get_image("non_existent.jpg"))

    def test_lazy_load_image(self):
        loader = ImageLoader(self.file_paths, lazy_load=True)
        future = loader.lazy_load_image(self.jpg_path)
        image = future.result()
        self.assertIsInstance(image, np.ndarray)

    def test_iterator(self):
        loader = ImageLoader(self.file_paths, lazy_load=False)
        for filename, image in loader:
            self.assertIn(filename, self.file_paths)
            self.assertIsInstance(image, np.ndarray)

    @patch.object(ImageLoader, "_load_image")
    def test_load_image_error(self, mock_load_image):
        # TODO: Try to make a working loading error test
        pass

    def test_unsupported_file_type(self):
        unsupported_path = os.path.join(self.temp_dir, "test.unsupported")
        with open(unsupported_path, "w") as f:
            f.write("This is not an image file")

        loader = ImageLoader([unsupported_path])
        with self.assertRaises(ValueError):
            loader.load_image(unsupported_path)


if __name__ == "__main__":
    unittest.main()
