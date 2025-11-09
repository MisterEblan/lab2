from collections.abc import Callable
from math import cos, exp

eps: float = 1e-3

# Точка, в которой функция меняет определение
THRESHOLD = 1

def f_1(x: float) -> float:
    """Часть функции, вычисляемая при x >= 1

    Args:
        x: значение аргумента.

    Returns:
        Результат вычисления функции.

    Raises:
        ZeroDivisionError: если знаменатель в тангенсе слишком близок к нулю.
    """

    result = cos(x) - exp(-x / 2) + x - 1

    return result

def f_2(x: float) -> float:
    """Часть функции, вычисляемая при x < 1

    Args:
        x: значение аргумента.

    Returns:
        Результат вычисления функции.
    """
    result = (3 * x) / (-4 * x + 4)

    return result

def function_factory(x: float) -> Callable[[float], float]:
    """Фабрика функций

    При x < 1 возвращает f_2, при x >= 1 - f_1

    Args:
        x: значение аргумента для определения функции..

    Returns:
        Часть функции.
    """
    if x >= THRESHOLD:
        return f_1

    return f_2

