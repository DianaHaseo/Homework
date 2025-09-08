import logging
import os

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

def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX. Показывает первые 6 и последние 4 цифры."""
    digits = "".join(card_number.split())
    if len(digits) == 0:
        masks_logger.error("Нулевая длина номера карты")
        raise ValueError("Нулевая длина номера карты")
    if len(digits) != 16 or not digits.isdigit():
        masks_logger.error("Нестандартный номер карты, должно быть 16-значное число")
        raise ValueError("Нестандартный номер карты, должно быть 16-значное число")
    first_4 = digits[:4]
    next_2 = digits[4:6]
    mask_2 = "**"
    mask_4 = "****"
    last_4 = digits[-4:]
    masked = f"{first_4} {next_2}{mask_2} {mask_4} {last_4}"
    masks_logger.info(f'Успешно замаскирован номер карты: {masked}')
    return masked

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта в формате **XXXX. Показывает только последние 4 цифры."""
    digits = "".join(account_number.split())
    if len(digits) == 0:
        masks_logger.error("Нулевая длина номера счета")
        raise ValueError("Нулевая длина номера счета")
    if len(digits) != 20 or not digits.isdigit():
        masks_logger.error("Нестандартный номер счета, должно быть 20-значное число")
        raise ValueError("Нестандартный номер счета, должно быть 20-значное число")
    masked = f"**{digits[-4:]}"
    masks_logger.info(f'Успешно замаскирован номер счета: {masked}')
    return masked
