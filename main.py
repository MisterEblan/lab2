from math import sqrt
import logging

# Escape-последовательности для цвета текста в терминале
GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"

# Радиус первой, малой окружности
R_1: float = 1.0
# Радиус второй, бОльшей окружности
R_2: float = 4.0

def is_in_ring(
    *xs: float,
    r_1: float,
    r_2: float
) -> bool:
    """Определяет, находится ли точка в кольце

    Args:
        xs: координаты в n-мерном пространстве.
        r_1: радиус первой окружности.
        r_2: радиус второй, бОльшей окружности.

    Returns:
        Находится точка в кольце или нет.
    """
    norm = sqrt(
        sum(x**2 for x in xs)
    )

    return r_1 <= norm <= r_2

def main() -> None:
    print("Введите координаты через запятую.")

    x, y = map(
        float,
        input("Ввод >>> ").strip().split(",")
    )

    if is_in_ring(
        x, y,
        r_1=R_1,
        r_2=R_2
    ):
        print(f"{GREEN}Точка находится в кольце.{RESET}")
    else:
        print(f"{RED}Точка вне кольца.{RESET}")

if __name__ == "__main__":
    main()
