import math
from typing import Callable


def create_dataset(get_line: Callable[..., str]):
    try:
        x = list(map(float, get_line().split(',')))
        y = list(map(float, get_line().split(',')))
        if len(x) != len(y):
            raise
        x, y = zip(*sorted(zip(x, y)))
    except:
        print("Введите корректную таблицу.")
        return None
    return [x, y]


def number_input(prompt: str, min=1.0, max=math.inf) -> float:
    while True:
        ans = input(prompt)
        try:
            num = float(ans)
            if num < min or num > max:
                print(f'Число должно быть в интервале [{round(min, 1)}, {round(max, 1)}].')
                continue
            return num
        except:
            continue


def float_interval_choice() -> [float, float]:
    while True:
        ans = input('Введите интервал: ').split()
        try:
            left, right = float(ans[0]), float(ans[1])
            if left >= right:
                print(f'Введите корректный интервал.')
                continue
            return left, right
        except:
            continue


def print_indexed_list(indexed_list, start=1):
    for index, item in enumerate(indexed_list, start=start):
        print(f'{index}. {item}')


def bool_choice(prompt: str) -> bool:
    return input(prompt + ' [y/n] ').strip() == 'y'


def read_table():
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        try:
            input_function = input if filename == '' else open(filename, "r").readline
            dataset = create_dataset(input_function)
            if dataset is not None:
                return dataset
        except FileNotFoundError:
            print('Файл не найден.')
