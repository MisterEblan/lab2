from task1_functions import function_factory
from task2_functions import (
    is_in_ring,
    R_1,
    R_2,
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

        if is_in_ring(x,y, r_1=R_1, r_2=R_2):
            print(f"{GREEN}Точка внутри кольца.{RESET}")
            return
        else:
            print(f"{RED}Точка вне кольца.{RESET}")
            return
    else:
        print("Неизвестный номер задания.")
        return

if __name__ == "__main__":
    main()
