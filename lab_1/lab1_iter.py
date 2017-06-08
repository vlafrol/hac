from sys import exit

if __name__ == '__main__':
    while True:
        print()
        print('############################################\n')
        print('If you want to exit the program, type "exit"')
        while True:
            try:
                print()
                # принимаем значения с клавиатуры
                first_input_str = input('Enter first value: ')
                first_value = float(first_input_str)
                second_input_str = input('Enter second value: ')
                second_value = float(second_input_str)
            except ValueError:
                # если ввели exit, то выход
                if first_input_str.lower() == 'exit':
                    exit(0)
                elif second_input_str.lower() == 'exit':
                    exit(0)
                continue
            print()
            break
        while True:
            # выбираем операцию
            print('1) + \n2) - \n3) * \n4) / \n5) ^\n')
            input_value = input("Enter value: ")
            print()
            if input_value == '1':
                print(first_value + second_value)
            elif input_value == '2':
                print(first_value - second_value)
            elif input_value == '3':
                print(first_value * second_value)
            elif input_value == '4':
                print(first_value / second_value)
            elif input_value == '5':
                print(first_value ** second_value)
            else:
                if input_value.lower() == 'exit':
                    exit(0)
                continue
            break
