from sys import exit


class Calc:
    def __init__(self):
        self._first_value = None
        self._second_value = None

    @property
    def first_value(self):
        return self._first_value

    @property
    def second_value(self):
        return self._second_value

    @first_value.setter
    def first_value(self, value):
        if value.lower() == 'exit':
            exit(0)
        try:
            self._first_value = float(value)
        except ValueError:
            raise NameError("This is not number! '{}'".format(value))

    @second_value.setter
    def second_value(self, value):
        if value.lower() == 'exit':
            exit(0)
        try:
            self._second_value = float(value)
        except ValueError:
            raise NameError("This is not number! '{}'".format(value))

    # Функции сложения, вычитания, умнжения, деления, возведения в степень
    def sum_values(self):
        return self._first_value + self._second_value

    def dif_values(self):
        return self._first_value - self._second_value

    def mult_values(self):
        return self._first_value * self._second_value

    def div_values(self):
        return self._first_value / self._second_value

    def exp_values(self):
        return self._first_value ** self._second_value

    def cleaner(self):
        """ Функция очищает переменные """
        self._first_value = None
        self._second_value = None

    def solver(self, trigger):
        """ В данной функции выбирается нужная операция """
        if trigger == '1':
            return self.sum_values()
        elif trigger == '2':
            return self.dif_values()
        elif trigger == '3':
            return self.mult_values()
        elif trigger == '4':
            return self.div_values()
        elif trigger == '5':
            return self.exp_values()
        else:
            raise NameError('Try again')


if __name__ == '__main__':
    calc = Calc()
    while True:
        try:
            print()
            print('############################################ \n')
            print('If you want to exit the program, type "exit" \n')
            # принимаем значения с клавиатуры
            calc.first_value = input('Enter first value: ')
            calc.second_value = input('Enter second value: ')
            while True:
                try:
                    print()
                    # выбираем операцию
                    print('1) + \n2) - \n3) * \n4) / \n5) ^\n')
                    result = calc.solver(input('Enter value: '))
                    break
                except NameError as error:
                    print(error)
                    continue
        except NameError as error:
            print(error)
            continue
        finally:
            calc.cleaner()
        print()
        print(result)
