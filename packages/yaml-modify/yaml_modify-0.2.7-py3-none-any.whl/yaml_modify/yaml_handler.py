import yaml
from pathlib import Path
from typing import Any, Dict

class YAMLFileError(Exception):
    pass

class YAMLFileHandler:
    """
    Обёртка для безопасного чтения и записи YAML-файлов.
    """
    def __init__(self, path: Path) -> None:
        self.path = path

    def read(self) -> Dict[str, Any]:
        if not self.path.exists():
            raise YAMLFileError(f"Файл не найден: {self.path}")
        try:
            with self.path.open("r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            raise YAMLFileError(f"Ошибка чтения файла {self.path}: {e}")

    def write(self, data: Dict[str, Any]) -> None:
        try:
            with self.path.open("w", encoding="utf-8") as f:
                yaml.safe_dump(data, f, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            raise YAMLFileError(f"Ошибка записи файла {self.path}: {e}")
