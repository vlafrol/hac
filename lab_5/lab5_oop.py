import argparse
from collections import Counter
from matplotlib import pyplot as plt


class MBox:
    def __init__(self, path):
        # путь до файла
        self.path = path
        self.container = []
        # читаем файл
        with open(self.path, 'r') as file:
            # разделяем файл по данной строке
            self.box = file.read().split('---------------------\nThis'
                                         ' automatic notification message was sent by Sakai Collab '
                                         '(https://collab.sakaiproject.org/portal) '
                                         'from the Source site.\nYou can modify how you receive '
                                         'notifications at My Workspace > Preferences.')
        self.box.pop(len(self.box) - 1)
        # разбираем данные
        self.box_parser()

    def box_parser(self):
        """ функция разбирает данные """
        for message in self.box:
            message = message.lstrip().split('\n')
            content = dict()
            content['email'] = message[0].split(' ')[1]
            for line in message:
                if 'X-DSPAM-Confidence:' in line:
                    content['confidence'] = float(line.split(' ')[1])
                if 'X-DSPAM-Result:' in line:
                    content['result'] = line.split(' ')[1]
                if 'X-DSPAM-Probability:' in line:
                    content['probability'] = float(line.split(' ')[1])
            self.container.append(content)

    @staticmethod
    def pass_fun():
        """ функция делает ничего """
        pass

    def get_spam_list(self):
        """ функция возвращает список кого нужно поместить в спам """
        return list(set(map(lambda x: x['email'] if x['result'] != 'Innocent' else self.pass_fun(), self.container)))

    def get_arithmetic_mean(self):
        """ функция возвращает среднюю арифметиескую параметра confidence """
        return sum(map(lambda x: x['confidence'], self.container)) / len(self)

    def __getitem__(self, item):
        # с помощью данной функции мы можем обращатся к объекту как к массиву
        return self.container[item]

    def __len__(self):
        # возвращает длинну объекта
        return len(self.container)

    def __str__(self):
        # возвращает объект в виде строки
        return str(self.container)


def make_hist(array):
    """ функция делает гистограмму """
    email = array
    coun = Counter()
    for i in email:
        coun[i] += 1
    arr = [coun[i] for i in coun.keys()]

    plt.figure('Histogram of senders')
    plt.title('Histogram of senders')
    plt.bar(range(len(coun.keys())), arr)
    plt.xticks(range(len(arr)), coun.keys(), size='small', rotation=90)
    plt.show()


if __name__ == '__main__':
    # разбираем аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True,
                        help='Path to input txt file.')

    namespace = parser.parse_args()

    mbox = MBox(namespace.path)
    print()
    print('Confidence arithmetic mean:', mbox.get_arithmetic_mean())
    print()
    print('Spam list:', *mbox.get_spam_list(), sep='\n')
    make_hist([i['email'] for i in mbox])


