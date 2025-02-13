from typing import Any
from pathlib import Path
import yaml
import toml
from .base_loader import BaseLoader


class FileLoader(BaseLoader):
    def __init__(self, file_paths: list[str]):
        """
        Load configuration from JSON, YAML or TOML files.

        :param file_paths: list of file paths to load.
        """
        self.file_paths = file_paths

    def load(self) -> dict[str, Any]:
        merged_config: dict[str, Any] = {}

        for file_path in self.file_paths:
            path = Path(file_path)

            if not path.exists():
                continue  # Skip missing files

            try:
                with open(path, "r", encoding="utf-8") as f:
                    if path.suffix in set([".yaml", ".yml", ".json"]):
                        data = yaml.safe_load(f)
                    elif path.suffix in set([".toml"]):
                        data = toml.load(f)  # Use TOML parser
                    else:
                        raise ValueError(f"Unsupported file type: {file_path}")

                if isinstance(data, dict):
                    self._merge_dicts(merged_config, data)  # type: ignore

            except Exception as e:
                print(f"Failed to load {file_path}: {e}")

        return merged_config
