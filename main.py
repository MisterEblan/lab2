from collections.abc import Callable
from math import tan, cos

eps: float = 1e-3

def f_1(x: float) -> float:
    """Часть функции, вычисляемая при x >= 0.2

    Args:
        x: значение аргумента.

    Returns:
        Результат вычисления функции.

    Raises:
        ZeroDivisionError: если знаменатель в тангенсе слишком близок к нулю.
    """
    if abs(cos(x)) < eps:
        raise ZeroDivisionError("Знаменатель в тангенсе близок к нулю!")

    result = (x * tan(x)) - (1 / 3)

    return result

def f_2(x: float) -> float:
    """Часть функции, вычисляемая при x < 0.2

    Args:
        x: значение аргумента.

    Returns:
        Результат вычисления функции.
    """

    result = cos(3 * x) + 3

    return result

def function_factory(x: float) -> Callable[[float], float]:
    """Фабрика функций

    При x < 0.2 возвращает f_2, при x >= 0.2 - f_1

    Args:
        x: значение аргумента для определения функции..

    Returns:
        Часть функции.
    """
    if x >= 0.2:
        return f_1

    return f_2


def main() -> None:
    x = float(input("Ввод >>> "))

    f = function_factory(x)

    print(f"x={x}")
    print(f"f={f(x)}")

if __name__ == "__main__":
    main()
