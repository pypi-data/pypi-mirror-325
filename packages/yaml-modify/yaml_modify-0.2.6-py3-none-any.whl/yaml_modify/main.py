import argparse
import logging
import sys
from pathlib import Path

from .orchestrator import Orchestrator

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Утилита для управления изменениями YAML и оркестрацией тестов."
    )
    parser.add_argument("-t", "--test", action="store_true", help="Запуск тестовых команд")
    parser.add_argument("-r", "--restore", action="store_true", help="Восстановление изменений из резервной копии")
    parser.add_argument("-v", "--verbose", action="store_true", help="Подробное логирование")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")
    
    orchestrator = Orchestrator(backup_file=Path("backup.json"))
    if args.test:
        orchestrator.run_test_mode()
    elif args.restore:
        orchestrator.run_restore()
    else:
        # Если не указаны флаги -t или -r, выполняется режим модификации YAML.
        orchestrator.run_modify()

if __name__ == "__main__":
    main()
