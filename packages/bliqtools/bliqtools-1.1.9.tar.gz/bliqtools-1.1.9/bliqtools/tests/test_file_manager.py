import unittest
import os
import tempfile
import pathlib

from bliqtools.file_manager import FileManager, FileManagerPresetType, FileFilter


class TestFileManager(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = pathlib.Path(tempfile.mkdtemp())
        self.file_manager = FileManager(self.temp_dir)

        self.create_test_file("test1.txt", "This is a test file")
        self.create_test_file("test2.pdf", "PDF content")
        self.create_test_file("image.jpg", "JPEG content")
        self.create_test_file("data.csv", "CSV content")
        self.create_test_file(".hidden.txt", "Hidden file")

        # Create a subdirectory with files for recursive testing
        self.sub_dir = os.path.join(self.temp_dir, "subdir")
        os.makedirs(self.sub_dir)
        self.create_test_file(os.path.join("subdir", "sub_test.txt"), "Subdir test file")

    def tearDown(self):
        # Clean up all test files and directories
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.temp_dir)

    def create_test_file(self, filename, content):
        filepath = os.path.join(self.temp_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)

    def test_list_files_no_filter(self):
        files = self.file_manager.list_files()
        self.assertEqual(len(files), 4)

    def test_list_files_with_extensions(self):
        files = self.file_manager.list_files(extensions=[".txt", ".pdf"])
        self.assertEqual(len(files), 2)
        self.assertTrue(any(f.name == "test1.txt" for f in files))
        self.assertTrue(any(f.name == "test2.pdf" for f in files))

    def test_list_files_with_pattern(self):
        files = self.file_manager.list_files(pattern=r"test\d\..*")
        self.assertEqual(len(files), 2)
        self.assertTrue(any(f.name == "test1.txt" for f in files))
        self.assertTrue(any(f.name == "test2.pdf" for f in files))

    def test_list_files_with_content_check(self):
        def check_content(filepath: str) -> bool:
            with open(filepath, "r") as file:
                return "test" in file.read().lower()

        files = self.file_manager.list_files(content_check=check_content)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].name == "test1.txt")

    def test_list_files_recursive(self):
        files = self.file_manager.list_files(recursive=True)
        self.assertEqual(len(files), 5)  # All non-hidden files including subdirectory
        self.assertTrue(any(f.name == "sub_test.txt" for f in files))

    def test_list_files_include_hidden(self):
        files = self.file_manager.list_files(include_hidden=True)
        self.assertEqual(len(files), 5)  # Including hidden file
        self.assertTrue(any(f.name == ".hidden.txt" for f in files))

    def test_preset_filters(self):
        # Test document preset
        doc_files = self.file_manager.list_files(preset=FileManagerPresetType.DOCUMENTS)
        self.assertEqual(len(doc_files), 2)  # test1.txt and test2.pdf

        # Test image preset
        img_files = self.file_manager.list_files(preset=FileManagerPresetType.IMAGES)
        self.assertEqual(len(img_files), 1)  # image.jpg

    def test_custom_preset(self):
        custom_filter = FileFilter(
            extensions=[".txt", ".csv"],
            pattern=r".*data.*",
            description="Custom data files"
        )
        self.file_manager.add_custom_preset("data_files", custom_filter)

        files = self.file_manager.list_files(preset="data_files")
        self.assertEqual(len(files), 1)  # Should only find data.csv
        self.assertTrue(files[0].name == "data.csv")

    def test_list_available_presets(self):
        custom_filter = FileFilter(
            extensions=[".dat"],
            description="Custom data files"
        )
        self.file_manager.add_custom_preset("custom", custom_filter)

        presets = self.file_manager.list_available_presets()

        self.assertIn("IMAGES", presets)
        self.assertIn("DOCUMENTS", presets)
        self.assertIn("TEXT", presets)

        self.assertIn("custom", presets)
        self.assertEqual(presets["custom"], "Custom data files")

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