from math import sqrt
import logging

# Escape-последовательности для цвета текста в терминале
GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"

# Сторона внешнего квадрата
L_EXTERNAL = 2
# Сторона внутренних квадратов
L_INTERNAL = 1

def is_in_region(
    x: float,
    y: float,
    l_ext: float,
    l_int: float
) -> bool:
    """Определяет, находится ли точка в области

    Args:
        x: координата точки по оси $Ox$.
        y: координата точки по оси $Oy$.
        l_ext: длина стороны внешнего квадрата.
        l_int: длина сторон внутренних квадратов.

    Returns:
        Находится ли точка в области.
    """

    # Проверка, что точка внутри внешнего квадрата
    if abs(x) > l_ext / 2 or abs(y) > l_ext / 2:
        return False

    # Проверка, что точка не попадает в верхний левый квадрат
    if (-l_int < x < 0) and (0 < y < l_int):
        return False

    # Проверка, что точка не попадает в нижний правый квадрат
    if (0 < x < l_int) and (-l_int < y < 0):
        return False

    return True

def main() -> None:
    print("Введите координаты через запятую.")

    x, y = map(
        float,
        input("Ввод >>> ").strip().split(",")
    )

    if is_in_region(
        x, y,
        l_ext=L_EXTERNAL,
        l_int=L_INTERNAL
    ):
        print(f"{GREEN}Точка находится в области.{RESET}")
    else:
        print(f"{RED}Точка вне области.{RESET}")

if __name__ == "__main__":
    main()
