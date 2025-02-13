import os
import tempfile
from pathlib import Path


class TemporaryFilePath:
    temp_dir = Path(tempfile.gettempdir())

    def __init__(self, ext: str | None = None):
        self.name = os.urandom(24).hex()
        self.file_path = (
            self.temp_dir / f"{self.name}.{ext}" if ext else self.temp_dir / self.name
        )

    def __enter__(self):
        return self.file_path

    def __exit__(self, *exc_info):
        self.file_path.unlink()


if __name__ == "__main__":
    with TemporaryFilePath("mol2") as file_path:
        print(file_path)
        file_path.write_text("Hello, world!")
