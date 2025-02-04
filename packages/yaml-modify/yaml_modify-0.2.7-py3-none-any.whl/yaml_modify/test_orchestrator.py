import subprocess
import logging
import os
import signal

class TestOrchestrator:
    """
    Выполнение набора тестовых команд (стадий) по очереди.

    Каждая команда запускается как отдельный процесс в своей группе процессов.
    Если на конкретной стадии (команде) происходит прерывание (Ctrl+C),
    то эта команда завершается, и оркестратор переходит к следующей стадии.
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
            logging.info("Запуск стадии: %s", command)
            try:
                # Запуск команды в отдельной группе процессов.
                process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
                # Ожидаем завершения команды.
                process.communicate()
            except KeyboardInterrupt:
                logging.info("Стадия прервана пользователем (Ctrl+C): %s", command)
                try:
                    # Отправляем SIGTERM всей группе процессов, чтобы корректно завершить её.
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                except Exception as e:
                    logging.error("Ошибка при завершении процесса для команды '%s': %s", command, e)
                # Переходим к следующей стадии.
                continue
            except Exception as e:
                logging.error("Ошибка при выполнении команды '%s': %s", command, e)
                # Переходим к следующей стадии
                continue

            retcode = process.returncode
            if retcode != 0:
                logging.error("Стадия '%s' завершилась с кодом %s", command, retcode)
            else:
                logging.info("Стадия '%s' успешно завершена.", command)
        
        logging.info("Исполнение всех стадий завершено.")
