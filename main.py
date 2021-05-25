import numpy
from graph import *
from boilerplate import *
from methods import *

methods = (
    (newton, 'Многочлен Ньютона с конечными разностями'),
    (lagrange, 'Многочлен Лагранжа')
)

functions = (
    (lambda t: math.cos(t), 'cos(x)'),
    (lambda t: 2 ** t, '2^x'),
    (lambda t: t ** 7 - 3 * (t ** 4) + t ** 3 - 5*t, 'x^7 - 3x^4 + x^3 - 5x')
)

MAX_POINTS = 20

if __name__ == '__main__':
    while True:
        if bool_choice('Вы хотите использовать исходные данные на основе функции?'):
            print('Выберите функцию. ')
            print_indexed_list(map(lambda tup: tup[1], functions))
            index = int(number_input('Введите номер: ', min=1, max=len(functions)))
            func, _ = functions[index - 1]
            left, right = float_interval_choice()
            nodes = int(
                number_input(f'Введите количество узлов интерполяции (2-{MAX_POINTS}): ', min=2, max=MAX_POINTS))

            x = list(numpy.linspace(left, right, nodes))
            y = list(map(lambda t: func(t), x))
            dataset = [x, y]
        else:
            dataset = read_table()
            left = min(dataset[0])
            right = max(dataset[0])

        print("\n" + tabulate(dataset, tablefmt='grid', floatfmt='2.4f') + "\n")

        x0 = number_input('Введите x0: ', min=left, max=right)

        print('Результаты:')
        x, y = dataset
        for solve, name in methods:
            try:
                result = solve(x, y, x0)
                graph(dataset, x0, result, solve, name)
                print(name + ':', result)
            except Exception as e:
                print(e)

        if input('\nЕще раз? [y/n] ') != 'y':
            break
