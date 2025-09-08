import json
from typing import List, Dict, Any
import logging
import os

# Настройка логгера для модуля utils
def setup_logger(utils: str) -> logging.Logger:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger = logging.getLogger(utils)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(os.path.join(log_dir, f'{utils}.log'), mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger

utils_logger = setup_logger('utils')


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    abs_path = os.path.abspath(file_path)
    utils_logger.info(f'Попытка загрузить транзакции из файла: {abs_path}')
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            utils_logger.error(f'Данные из {abs_path} не являются списком')
            return []
        if not all(isinstance(item, dict) for item in data):
            utils_logger.error(f'Некоторые элементы данных из {abs_path} не являются словарями')
            return []
        utils_logger.info(f'Успешно загружены транзакции из {abs_path}')
        return data
    except FileNotFoundError:
        utils_logger.error(f'Файл не найден: {abs_path}')
        return []
    except json.JSONDecodeError:
        utils_logger.error(f'Ошибка декодирования JSON из файла: {abs_path}')
        return []
    except Exception as e:
        utils_logger.error(f'Неожиданная ошибка при загрузке файла {abs_path}: {e}')
        return []

