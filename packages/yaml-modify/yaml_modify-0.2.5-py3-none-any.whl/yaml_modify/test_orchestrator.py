import subprocess
import logging

class TestOrchestrator:
    """
    Выполнение набора тестовых команд в одном терминальном сеансе.
    
    Все команды объединяются в один скрипт, который передается оболочке для последовательного выполнения.
    Вывод команд поступает непосредственно в консоль.
    Если пользователь прерывает выполнение (Ctrl+C), выводится сообщение, но скрипт корректно завершается.
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
        # Объединяем все команды в один многострочный скрипт без запуска в фоне.
        script = "\n".join(self.commands) + "\n"
        
        logging.info("Запущен:\n%s", script)
        try:
            # Передаем скрипт в оболочку. Команды выполняются последовательно.
            subprocess.run(script, shell=True, check=True)
        except KeyboardInterrupt:
            logging.info("Исполнение команд прервано пользователем (Ctrl+C).")
        except subprocess.CalledProcessError as e:
            logging.error("Ошибка при выполнении скрипта команд: %s", e)
