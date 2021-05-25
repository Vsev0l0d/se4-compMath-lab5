import matplotlib.pyplot as plt
import numpy as np


def graph(data, x0, y0, interpolate, title: str):
    data_x, data_y = data
    plt.figure()
    plt.title = title
    plt.grid(True)

    plt.scatter(data_x, data_y, s=20, label='Исходные данные', zorder=10)

    x_linspace = np.linspace(data_x[0], data_x[-1], 100)
    interpolated_y = [interpolate(data_x, data_y, x) for x in x_linspace]
    plt.plot(x_linspace, interpolated_y, zorder=5, label=title)

    plt.plot(x0, y0, 'o', markersize=5, zorder=10, label='Искомое значение')

    plt.legend(fontsize='x-small')
    plt.savefig(f'{title.replace(" ", "_")}.png')
    plt.show()
