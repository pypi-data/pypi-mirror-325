import subprocess
import logging

class TestOrchestrator:
    """
    Выполнение набора тестовых команд.
    """
    def __init__(self) -> None:
        self.commands = [
            "testsystem --stage preburn --debug --output old_aq_test",
            "testsystem --stage inventory --debug --output old_aq_test",
            "testsystem --stage wifi --debug --output old_aq_test",
            "testsystem --stage bluetooth --debug --output old_aq_test",
            "testsystem --stage memory_stress --debug --output old_aq_test",
            "testsystem --stage gpu_stress --debug --output old_aq_test",
            "testsystem --stage fio_test --debug --output old_aq_test",
            "testsystem --stage os_install --debug --output old_aq_test",
        ]

    def run(self) -> None:
        for command in self.commands:
            try:
                logging.info("Выполнение команды: %s", command)
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                logging.error("Ошибка при выполнении команды '%s': %s", command, e)
