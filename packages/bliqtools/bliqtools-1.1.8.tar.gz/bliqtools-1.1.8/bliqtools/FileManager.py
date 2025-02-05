import os
import re
from typing import Callable


class FileManager:
    def __init__(self, directory: str):
        self.directory = directory
        self.listed_files = []

    def list_files(
        self,
        extensions: list[str] = None,
        pattern: str = None,
        content_check: Callable[[str], bool] = None,
        use_cache: bool = True,
    ) -> list[str]:
        """
        List files in the directory with optional filtering.

        :param extensions: List of file extensions to include (e.g., ['.tif', '.jpg'])
        :param pattern: Regex pattern to match filenames
        :param content_check: Function that takes a filepath and returns True if the file should be included
        :param use_cache: If True, return cached results if available, otherwise cache the result
        :return: List of filepaths matching the criteria
        """
        matching_files = []
        if use_cache and self.listed_files:
            return self.listed_files

        for root, _, files in os.walk(self.directory):
            for filename in files:
                filepath = os.path.join(root, filename)

                if extensions and not any(
                    filename.lower().endswith(ext.lower()) for ext in extensions
                ):
                    continue

                if pattern and not re.search(pattern, filename):
                    continue

                if content_check and not content_check(filepath):
                    continue

                matching_files.append(filepath)

        if use_cache:
            self.listed_files = matching_files
        return matching_files

    def clear_cache(self):
        """Clear the cached file list."""
        self.listed_files = []

    @staticmethod
    def is_image_file(filepath: str) -> bool:
        """Check if a file is an image based on its extension."""
        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff"]
        return any(filepath.lower().endswith(ext) for ext in image_extensions)

    @staticmethod
    def is_tiff_file(filepath: str) -> bool:
        """Check if a file is a TIFF image."""
        return filepath.lower().endswith((".tif", ".tiff"))

    @staticmethod
    def contains_text(filepath: str, text: str) -> bool:
        """Check if a file contains the specified text."""
        try:
            with open(filepath, "r") as file:
                return text in file.read()
        except:
            return False
