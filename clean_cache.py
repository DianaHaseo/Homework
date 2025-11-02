import shutil
from pathlib import Path

# Папка проекта (текущая папка)
root = Path(__file__).parent

# Ищем все папки __pycache__ рекурсивно
for cache_dir in root.rglob("__pycache__"):
    print(f"Удаляю {cache_dir}")
    shutil.rmtree(cache_dir)

print("Очистка кэша завершена.")