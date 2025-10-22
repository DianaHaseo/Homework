import logging
import os
import re

# Настройка логгера для модуля masks
def setup_logger(masks: str) -> logging.Logger:
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger(masks)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(f'logs/{masks}.log', mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger


masks_logger = setup_logger('masks')


def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты (16 цифр)."""
    if len(number) != 16 or not number.isdigit():
        raise ValueError("Неверный номер карты")
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(number: str) -> str:
    """Маскирует счет (20 цифр)."""
    if len(number) != 20 or not number.isdigit():
        raise ValueError("Неверный счет")
    return f"**{number[-4:]}"


def mask_card_or_account(text: str) -> str:
    """Определяет и маскирует счет или карту в строке."""
    import re
    digits = re.findall(r"\d+", text)
    for number in digits:
        if len(number) == 16:
            return get_mask_card_number(number)
        elif len(number) == 20:
            return get_mask_account(number)
    raise ValueError("Не найден номер карты или счета")