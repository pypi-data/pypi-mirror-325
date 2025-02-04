import json
import logging
import shutil
from pathlib import Path
from typing import Any, Dict, List

from .yaml_handler import YAMLFileHandler

# Опционально можно использовать filelock для защиты от конкурентного доступа.
try:
    from filelock import FileLock, Timeout
except ImportError:
    FileLock = None  # Если библиотека не установлена, блокировка не используется.

class BackupError(Exception):
    """Исключение для ошибок резервного копирования и восстановления."""
    pass

class BackupManager:
    """
    Менеджер резервного копирования и восстановления.

    Резервная копия хранится в JSON-файле. Этот класс защищает исходное значение от перезаписи
    при повторных запусках утилиты, используя атомарную запись. Резервный файл не удаляется после восстановления,
    чтобы исходное значение оставалось доступным для повторного восстановления.
    """
    def __init__(self, backup_file: Path) -> None:
        """
        Инициализирует BackupManager.

        :param backup_file: Путь к файлу, где будет храниться резервная копия.
        """
        self.backup_file: Path = backup_file
        # Опционально: настройка файла блокировки.
        self.lock_file: Path = backup_file.with_suffix(backup_file.suffix + ".lock")
        if not self.backup_file.exists():
            self.create_backup_file()
        self.backups: Dict[str, Dict[str, Any]] = self.load_backups()

    def create_backup_file(self) -> None:
        """
        Создает пустой JSON-файл для резервных копий, если он отсутствует.
        """
        try:
            self.backup_file.parent.mkdir(parents=True, exist_ok=True)
            self._atomic_write({})
            logging.info(f"Создан файл резервной копии: {self.backup_file}")
        except Exception as e:
            raise BackupError(f"Ошибка создания файла резервной копии: {e}") from e

    def delete_backup_file(self) -> None:
        """
        Удаляет файл резервной копии, если он существует.
        """
        try:
            if self.backup_file.exists():
                self.backup_file.unlink()
                logging.info(f"Удалён файл резервной копии: {self.backup_file}")
        except Exception as e:
            raise BackupError(f"Ошибка удаления файла резервной копии: {e}") from e

    def load_backups(self) -> Dict[str, Dict[str, Any]]:
        """
        Загружает резервные данные из JSON-файла.

        :return: Словарь резервных данных.
        """
        try:
            if self.backup_file.exists():
                with self.backup_file.open("r", encoding="utf-8") as f:
                    backups = json.load(f)
                    logging.debug(f"Загружены резервные данные: {backups}")
                    return backups
        except Exception as e:
            raise BackupError(f"Ошибка загрузки резервной копии: {e}") from e
        return {}

    def save_backups(self) -> None:
        """
        Сохраняет резервные данные в JSON-файл с использованием атомарной записи.
        """
        try:
            self._atomic_write(self.backups)
            logging.info(f"Резервная копия сохранена: {self.backup_file}")
        except Exception as e:
            raise BackupError(f"Ошибка сохранения резервной копии: {e}") from e

    def _atomic_write(self, data: Any) -> None:
        """
        Атомарно записывает данные в JSON-файл через временный файл.

        :param data: Данные для записи.
        """
        temp_file: Path = self.backup_file.with_suffix(self.backup_file.suffix + ".tmp")
        with temp_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        shutil.move(str(temp_file), str(self.backup_file))

    def backup_data(self, file_path: Path, key_path: List[str], old_value: Any) -> None:
        """
        Сохраняет резервную копию значения по указанному ключевому пути,
        если для данного файла/ключа резерв уже не создан.
        Если значение уже сохранено, обновление не производится.

        :param file_path: Путь к YAML-файлу.
        :param key_path: Список ключей, определяющих путь к значению.
        :param old_value: Исходное значение для сохранения.
        """
        file_str: str = str(file_path)
        key: str = ".".join(key_path)
        if file_str not in self.backups:
            self.backups[file_str] = {}
        if key in self.backups[file_str]:
            logging.info(f"Резервная копия для '{key}' в файле {file_str} уже существует. Пропуск обновления.")
        else:
            self.backups[file_str][key] = old_value
            self.save_backups()

    def restore(self) -> None:
        """
        Восстанавливает значения в YAML-файлах из резервной копии.

        Для каждого файла производится чтение резервных данных, затем обновляется YAML-файл,
        и исходное значение для каждого ключа восстанавливается.
        Резервный файл не удаляется, чтобы исходное значение оставалось доступным для повторного восстановления.
        """
        if not self.backup_file.exists():
            logging.info(f"Файл резервной копии не найден: {self.backup_file}")
            return

        backups: Dict[str, Dict[str, Any]] = self.load_backups()  # Актуальные резервные данные
        for file_str, changes in backups.items():
            file_path: Path = Path(file_str)
            try:
                handler: YAMLFileHandler = YAMLFileHandler(file_path)
                data: Any = handler.read()
            except Exception as e:
                logging.error(f"Ошибка чтения файла {file_path} для восстановления: {e}")
                continue

            for key_path_str, old_value in changes.items():
                keys: List[str] = key_path_str.split(".")
                ref: Any = data
                for key in keys[:-1]:
                    ref = ref.setdefault(key, {})
                ref[keys[-1]] = old_value
                logging.debug(f"Восстановление ключа '{key_path_str}' в файле {file_path}: значение {old_value}")

            try:
                handler.write(data)
                logging.info(f"Файл {file_path} успешно восстановлен.")
            except Exception as e:
                logging.error(f"Ошибка записи файла {file_path} при восстановлении: {e}")

