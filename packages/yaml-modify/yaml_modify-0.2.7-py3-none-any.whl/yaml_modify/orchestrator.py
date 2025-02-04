import logging
from pathlib import Path
from typing import List

from dataclasses import dataclass

from .backup_manager import BackupManager
from .test_orchestrator import TestOrchestrator
from .yaml_handler import YAMLFileHandler, YAMLFileError

@dataclass
class Modification:
    """
    Data class для описания изменения в YAML-файле.
    """
    file_path: Path
    key_path: List[str]
    new_value: any

class Orchestrator:
    """
    Главный класс-оркестратор, объединяющий изменение YAML, восстановление и выполнение тестов.
    """
    def __init__(self, backup_file: Path) -> None:
        self.backup_manager = BackupManager(backup_file)
        self.test_orchestrator = TestOrchestrator()

    def run_restore(self) -> None:
        logging.info("Восстановление изменений из резервной копии...")
        self.backup_manager.restore()
        logging.info("Восстановление завершено.")

    def run_test_mode(self) -> None:
        logging.info("Запуск тестовых команд...")
        self.test_orchestrator.run()
        logging.info("Тестирование завершено.")

    def run_modify(self) -> None:
        modifications = self.get_modifications()
        if not modifications:
            logging.info("Модификации не заданы. Завершение работы без изменений.")
            return

        for mod in modifications:
            try:
                handler = YAMLFileHandler(mod.file_path)
                data = handler.read()
            except YAMLFileError as e:
                logging.error("Ошибка чтения файла %s: %s", mod.file_path, e)
                continue

            # Получаем текущее значение по указанному ключевому пути
            current_value = data
            for key in mod.key_path:
                current_value = current_value.get(key)
            # Создаём резервную копию перед изменением
            self.backup_manager.backup_data(mod.file_path, mod.key_path, current_value)

            # Применяем модификацию: идём до предпоследнего ключа, затем задаём новое значение
            ref = data
            for key in mod.key_path[:-1]:
                ref = ref.setdefault(key, {})
            ref[mod.key_path[-1]] = mod.new_value

            try:
                handler.write(data)
                logging.info("Файл %s успешно обновлён.", mod.file_path)
            except YAMLFileError as e:
                logging.error("Ошибка записи файла %s: %s", mod.file_path, e)

    def get_modifications(self) -> List[Modification]:
        """
        Определяет список модификаций.
        Здесь задаются изменения для ваших YAML-файлов.
        """
        return [
            Modification(
                file_path=Path("/etc/aquarius/testing/local/gpu_test/gpu_test.yml"),
                key_path=["duration"],
                new_value=1
            ),
            Modification(
                file_path=Path("/etc/aquarius/testing/local/stressapptest/stressapptest.yml"),
                key_path=["testing_time"],
                new_value=30
            ),
            Modification(
                file_path=Path("/etc/aquarius/testing/local/fio_test/fio_test.yml"),
                key_path=["disks", "test1", "options", "test_time"],
                new_value="30s"
            )
        ]
