import json
from typing import List, Dict, Any

import logging
import os


def setup_logger(name: str) -> logging.Logger:
    # Абсолютный путь к папке logs в том же каталоге, что и скрипт
    base_dir = os.path.dirname(os.path.abspath(__name__))
    log_dir = os.path.join(base_dir, 'logs')
    log_path = os.path.join(log_dir, f'utils.log')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Очищаем обработчики до добавления новых
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False  # Чтобы логи не дублировались по иерархии

    return logger


utils_logger = setup_logger('utils')
utils_logger.info('Логгер для utils успешно создан')
utils_logger.error('Пример ошибки, которая может произойти')

# Завершение работы логгов в конце программы
logging.shutdown()


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список словарей или пустой список при ошибках/несоответствии
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        if not all(isinstance(item, dict) for item in data):
            return []
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []