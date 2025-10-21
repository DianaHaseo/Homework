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


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    Если цифр больше 16 — берёт последние 16.
    Если меньше 10 — вызывает ошибку.
    """
    digits = "".join(re.findall(r"\d", card_number))

    if not digits:
        raise ValueError("Номер карты не содержит цифр")

    if len(digits) < 10:
        raise ValueError("Слишком короткий номер карты")

    # Если больше 16 цифр — используем последние 16
    if len(digits) > 16:
        digits = digits[-16:]

    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"

def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта. Поддерживает формат вроде 'Счет 40817810099910004312'.
    Показывает только последние 4 цифры.
    """
    digits = "".join(re.findall(r"\d", account_number))

    if len(digits) == 0:
        masks_logger.error("Нулевая длина номера счета")
        raise ValueError("Нулевая длина номера счета")

    if len(digits) != 20:
        masks_logger.error("Нестандартный номер счета, должно быть 20-значное число")
        raise ValueError("Нестандартный номер счета, должно быть 20-значное число")

    masked_number = f"**{digits[-4:]}"

    # Добавляем слово "Счет" если оно было
    if "Счет" in account_number or "счет" in account_number:
        masked = f"Счет {masked_number}"
    else:
        masked = masked_number

    masks_logger.info(f'Успешно замаскирован номер счета: {masked}')
    return masked
