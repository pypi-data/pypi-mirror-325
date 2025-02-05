import unittest
import os
import tempfile
from bliqtools.FileManager import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.file_manager = FileManager(self.temp_dir)

        self.create_test_file("test1.txt", "This is a test file")
        self.create_test_file("test2.pdf", "PDF content")
        self.create_test_file("image.jpg", "JPEG content")
        self.create_test_file("data.csv", "CSV content")

    def tearDown(self):
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def create_test_file(self, filename, content):
        with open(os.path.join(self.temp_dir, filename), "w") as f:
            f.write(content)

    def test_list_files_no_filter(self):
        files = self.file_manager.list_files()
        self.assertEqual(len(files), 4)

    def test_list_files_with_extensions(self):
        files = self.file_manager.list_files(extensions=[".txt", ".pdf"])
        self.assertEqual(len(files), 2)
        self.assertTrue(any(f.endswith("test1.txt") for f in files))
        self.assertTrue(any(f.endswith("test2.pdf") for f in files))

    def test_list_files_with_pattern(self):
        files = self.file_manager.list_files(pattern=r"test\d\..*")
        self.assertEqual(len(files), 2)
        self.assertTrue(any(f.endswith("test1.txt") for f in files))
        self.assertTrue(any(f.endswith("test2.pdf") for f in files))

    def test_list_files_with_content_check(self):
        def safe_content_check(f):
            # Safely open file to silence the malloc warning
            try:
                with open(f, "r") as file:
                    return "test" in file.read().lower()
            except:
                return False

        files = self.file_manager.list_files(content_check=safe_content_check)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].endswith("test1.txt"))

    def test_caching(self):
        files1 = self.file_manager.list_files()
        self.assertEqual(len(files1), 4)

        self.create_test_file("new_file.txt", "New content")

        files2 = self.file_manager.list_files(use_cache=True)
        self.assertEqual(len(files2), 4)
        self.assertEqual(files1, files2)

        files3 = self.file_manager.list_files(use_cache=False)
        self.assertEqual(len(files3), 5)

    def test_clear_cache(self):
        self.file_manager.list_files()
        self.file_manager.clear_cache()
        self.create_test_file("another_file.txt", "More content")

        files = self.file_manager.list_files(use_cache=True)
        self.assertEqual(len(files), 5)

    def test_is_image_file(self):
        self.assertTrue(FileManager.is_image_file("test.jpg"))
        self.assertTrue(FileManager.is_image_file("test.JPEG"))
        self.assertTrue(FileManager.is_image_file("test.png"))
        self.assertFalse(FileManager.is_image_file("test.txt"))

    def test_is_tiff_file(self):
        self.assertTrue(FileManager.is_tiff_file("test.tif"))
        self.assertTrue(FileManager.is_tiff_file("test.TIFF"))
        self.assertFalse(FileManager.is_tiff_file("test.jpg"))

    def test_contains_text(self):
        filepath = os.path.join(self.temp_dir, "test1.txt")
        self.assertTrue(FileManager.contains_text(filepath, "test"))
        self.assertFalse(FileManager.contains_text(filepath, "notpresent"))


if __name__ == "__main__":
    unittest.main()
