import os
import tempfile
from pathlib import Path


class TemporaryFilePath:
    temp_dir = Path(tempfile.gettempdir())

    def __init__(self, ext: str | None = None, initial_content: str = ""):
        self.name = os.urandom(24).hex()
        self.file_path = (
            self.temp_dir / f"{self.name}.{ext}" if ext else self.temp_dir / self.name
        )
        self.file_path.write_text(initial_content)

    def __enter__(self):
        return self.file_path

    def __exit__(self, *exc_info):
        self.file_path.unlink()


if __name__ == "__main__":
    with TemporaryFilePath("mol2", "HELLO WORLD") as file_path:
        print(file_path)
        assert file_path.read_text() == "HELLO WORLD"
    assert not file_path.exists()
