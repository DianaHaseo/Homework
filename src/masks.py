import logging
import os

def setup_logger(name: str) -> logging.Logger:
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(f'logs/masks.log', encoding='utf-8', mode='w')
    file_handler.setFormatter(formatter)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(file_handler)
    return logger

masks_logger = setup_logger('masks')
masks_logger.info('Маскировка карты выполнена для: 1234567890123456')
masks_logger.error('Ошибка при маскировке карты: Некорректный номер карты')
masks_logger.info('Маскировка счета выполнена для: 1234567890')

def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX.
    Показывает первые 6 и последние 4 цифры, остальные — звёздочками."""
    # Удаляем все пробелы на случай, если номер введён с ними
    digits = "".join(card_number.split())
    if len(digits) < 10 or not digits.isdigit():
        raise ValueError("Некорректный номер карты")
    first_4 = digits[:4]
    next_2 = digits[4:6]
    mask_2 = "**"
    mask_4 = "****"
    last_4 = digits[-4:]
    return f"{first_4} {next_2}{mask_2} {mask_4} {last_4}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта в формате **XXXX.
    Показывает только последние 4 цифры, остальные — звёздочками."""
    digits = "".join(account_number.split())
    if len(digits) < 4 or not digits.isdigit():
        raise ValueError("Некорректный номер счёта")
    return f"**{digits[-4:]}"
