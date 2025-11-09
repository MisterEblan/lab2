from task1_functions import function_factory
from task2_functions import (
    is_in_region,
    L_EXTERNAL,
    L_INTERNAL,
    GREEN,
    RED,
    RESET
)

def main() -> None:
    task_num = int(input("Введите номера задания (1 или 2) >>> "))

    if task_num == 1:
        x = float(input("Введите x >>> "))

        f = function_factory(x)

        print(f"x={x}")
        print(f"f={f(x)}")
        return

    if task_num == 2:
        x, y = map(
            float,
            input("Введите x и y через запятую >>> ").strip().split(",")
        )

        if is_in_region(
            x, y,
            l_ext=L_EXTERNAL,
            l_int=L_INTERNAL
        ):
            print(f"{GREEN}Точка внутри области.{RESET}")
            return
        else:
            print(f"{RED}Точка вне области.{RESET}")
            return
    else:
        print("Неизвестный номер задания.")
        return

if __name__ == "__main__":
    main()
