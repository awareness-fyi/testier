from pathlib import Path


class FileReader:

    def read(self, file_path: Path) -> str:
        with open(file_path) as f:
            return f.read()
