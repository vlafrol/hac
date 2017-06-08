import argparse
from random import randint
from matplotlib import pyplot as plt


class SMA:
    def __init__(self, array, window):
        self.array = array
        self.window = window

    def get_sma(self):
        sma = []
        for i in range(len(self.array)):
            if i + 1 < self.window:
                sma.append(0)
            else:
                sma.append(sum(self.array[i + 1 - self.window:i + 1]) / self.window)
        return sma

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
    sma_obj = SMA(array, namespace.window)

    # строим график
    plt.figure('SMA')
    plt.plot(array_len, sma_obj.get_sma(), '-r', array_len, array)
    plt.title('Simple moving average')
    plt.show()
