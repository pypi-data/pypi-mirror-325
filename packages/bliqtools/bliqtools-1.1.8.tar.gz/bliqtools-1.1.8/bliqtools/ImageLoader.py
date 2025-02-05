import tifffile
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import numpy as np
from bliqtools.testing import Progress


class ImageLoader(Progress):
    def __init__(self, file_paths: [str], lazy_load=True):
        super().__init__(lazy_load)
        self.file_paths = file_paths
        self.images = {}
        self.executor = ThreadPoolExecutor()
        self.pillow_image_extension = ["jpg", "gif", "jpeg", "jpg"]
        self.lazy_load = lazy_load

        if not lazy_load:
            self.preload_all_images()

    def load_image(self, path: str) -> np.ndarray:
        if path not in self.images:
            try:
                self.images[path] = self._load_image(path)
            except IOError as e:
                raise f"Error loading image: {path}. Error: {str(e)}"
        return self.images[path]

    def get_image(self, path) -> np.ndarray | None:
        return self.images.get(path)

    def preload_all_images(self) -> None:
        futures = [
            self.executor.submit(self.load_image, path) for path in self.file_paths
        ]
        for future in futures:
            future.result()  # Wait for all images to load

    def is_image_loaded(self, path: str) -> bool:
        return path in self.images and self.images[path] is not None

    def _load_image(self, filename) -> np.ndarray | None:
        if ".tif" in filename:
            image = tifffile.imread(filename)
        elif any(ext in filename.lower() for ext in self.pillow_image_extension):
            with Image.open(filename) as img:
                image = np.array(img)
        else:
            raise ValueError("File type not supported yet")
        return image

    def lazy_load_image(self, path) -> np.ndarray | None:
        if path not in self.images:
            return self.executor.submit(self.load_image, path)
        return self.images[path]

    def __del__(self):
        self.executor.shutdown()

    def __iter__(self):
        for filename in self.file_paths:
            yield filename, self.load_image(filename)
