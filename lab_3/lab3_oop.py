import argparse


class Poly:
    def __init__(self, arg):
        self.arg = arg

    def get_poly(self):
        poly = 0
        for i in self.arg:
            poly += 1 / i + 3

        return poly

if __name__ == '__main__':
    # разбираем аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument('--poly', type=str,
                        help='Example:dir python lab3_iter.py --poly 1,2,3,4,5')

    namespace = parser.parse_args()
    # преобразуем входные данные в кортеж
    poly_arg = tuple(map(lambda x: int(x), namespace.poly.split(',')))

    poly_obj = Poly(poly_arg)
    # считаем сумму
    result = poly_obj.get_poly()
    # выводим результат
    print(result)



