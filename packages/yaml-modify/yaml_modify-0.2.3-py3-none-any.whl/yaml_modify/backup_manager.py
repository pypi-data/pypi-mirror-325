import json
import logging
from pathlib import Path
from typing import Any, Dict, List

from .yaml_handler import YAMLFileHandler

class BackupError(Exception):
    pass

class BackupManager:
    """
    Менеджер резервного копирования и восстановления.
    Резервная копия хранится в JSON-файле.
    """
    def __init__(self, backup_file: Path) -> None:
        self.backup_file = backup_file
        # Если файл резервной копии отсутствует, создаём его
        if not self.backup_file.exists():
            self.create_backup_file()
        self.backups: Dict[str, Dict[str, Any]] = self.load_backups()

    def create_backup_file(self) -> None:
        """
        Создает пустой JSON-файл для резервных копий, если он не существует.
        """
        try:
            self.backup_file.parent.mkdir(parents=True, exist_ok=True)
            with self.backup_file.open("w", encoding="utf-8") as f:
                json.dump({}, f)
            logging.info("Создан файл резервной копии: %s", self.backup_file)
        except Exception as e:
            raise BackupError(f"Ошибка создания файла резервной копии: {e}")

    def delete_backup_file(self) -> None:
        """
        Удаляет файл резервной копии, если он существует.
        """
        if self.backup_file.exists():
            try:
                self.backup_file.unlink()
                logging.info("Удалён файл резервной копии: %s", self.backup_file)
            except Exception as e:
                raise BackupError(f"Ошибка удаления файла резервной копии: {e}")

    def load_backups(self) -> Dict[str, Dict[str, Any]]:
        if self.backup_file.exists():
            try:
                with self.backup_file.open("r", encoding="utf-8") as f:
                    backups = json.load(f)
                    logging.debug("Загружены резервные данные: %s", backups)
                    return backups
            except Exception as e:
                raise BackupError(f"Ошибка загрузки резервной копии: {e}")
        return {}

    def save_backups(self) -> None:
        try:
            with self.backup_file.open("w", encoding="utf-8") as f:
                json.dump(self.backups, f, indent=4)
            logging.info("Резервная копия сохранена: %s", self.backup_file)
        except Exception as e:
            raise BackupError(f"Ошибка сохранения резервной копии: {e}")

    def backup_data(self, file_path: Path, key_path: List[str], old_value: Any) -> None:
        file_str = str(file_path)
        if file_str not in self.backups:
            self.backups[file_str] = {}
        self.backups[file_str][".".join(key_path)] = old_value
        self.save_backups()

    def restore(self) -> None:
        if not self.backup_file.exists():
            logging.info("Файл резервной копии не найден: %s", self.backup_file)
            return

        # Перечитываем резервные данные с диска для актуальности
        backups = self.load_backups()
        for file_str, changes in backups.items():
            file_path = Path(file_str)
            try:
                handler = YAMLFileHandler(file_path)
                data = handler.read()
            except Exception as e:
                logging.error("Ошибка чтения файла %s для восстановления: %s", file_path, e)
                continue

            for key_path_str, old_value in changes.items():
                keys = key_path_str.split(".")
                ref = data
                for key in keys[:-1]:
                    ref = ref.setdefault(key, {})
                ref[keys[-1]] = old_value
                logging.debug("Восстановление ключа '%s' в файле %s: новое значение %s",
                              key_path_str, file_path, old_value)

            try:
                handler.write(data)
                logging.info("Файл %s успешно восстановлен.", file_path)
            except Exception as e:
                logging.error("Ошибка записи файла %s при восстановлении: %s", file_path, e)
        # После успешного восстановления удаляем резервный файл
        self.delete_backup_file()
