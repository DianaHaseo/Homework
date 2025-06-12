def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты в формате XXXX XX** **** XXXX.
    Показывает первые 6 и последние 4 цифры, остальные — звёздочками."""
    # Удаляем все пробелы на случай, если номер введён с ними
    digits = ''.join(card_number.split())
    if len(digits) < 10:
        raise ValueError("Некорректный номер карты")
    # Формируем маску
    first_4 = digits[:4]
    next_2 = digits[4:6]
    mask_2 = '**'
    mask_4 = '****'
    last_4 = digits[-4:]
    return f"{first_4} {next_2}{mask_2} {mask_4} {last_4}"

def get_mask_account(account_number: str) -> str:
    """ Маскирует номер счёта в формате **XXXX.
    Показывает только последние 4 цифры, остальные — звёздочками."""
    digits = ''.join(account_number.split())
    if len(digits) < 4:
        raise ValueError("Некорректный номер счёта")
    return f"**{digits[-4:]}"
