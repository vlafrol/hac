import argparse

if __name__ == '__main__':
    # разбираем аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument('--poly', type=str,
                        help='Example: python3 lab3_iter.py --poly 1,2,3,4,5')

    namespace = parser.parse_args()

    # преобразуем входные данные в кортеж
    poly_arg = tuple(map(lambda x: int(x), namespace.poly.split(',')))

    # считаем сумму
    poly = 0
    for i in poly_arg:
        poly += 1 / i + 3

    # выводим результат
    print(poly)
