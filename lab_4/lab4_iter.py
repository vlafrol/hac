import argparse
from random import randint
from matplotlib import pyplot as plt


def sma(window, arr):
    """ функция расчета sma """
    calc = []
    for i in range(len(arr)):
        if i + 1 < window:
            calc.append(0)
        else:
            calc.append(sum(arr[i + 1 - window:i + 1]) / window)
    return calc

if __name__ == '__main__':
    # разбираем аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--window', type=int, required=True,
                        help='Window size')
    parser.add_argument('-s', '--size', type=int, default=100,
                        help='Array size')
    namespace = parser.parse_args()

    # генерируем список
    array = [randint(0, 120) for i in range(namespace.size)]
    array_len = [i for i in range(len(array))]
    # считаем sma
    result = sma(namespace.window, array)

    # рисуем график
    plt.figure('SMA')
    plt.plot(array_len, result, '-r', array_len, array)
    plt.title('Simple moving average')
    plt.show()
