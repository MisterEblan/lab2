from task1_functions import function_factory
from task2_functions import is_in_ring

def main() -> None:
    task_num = int(input("Введите номера задания (1 или 2) >>> "))

    if task_num == 1:
        x = float(input("Введите x >>> "))

        f = function_factory(x)

        print(f"x={x}")
        print(f"f={f(x)}")

    if task_num == 2:
        x,

if __name__ == "__main__":
    main()
