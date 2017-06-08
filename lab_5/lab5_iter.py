import argparse
from collections import Counter
from matplotlib import pyplot as plt


def pass_fun():
    """ функция делает ничего """
    pass


if __name__ == '__main__':
    # разбираем аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True,
                        help='Path to input txt file.')

    namespace = parser.parse_args()

    # читаем файл
    with open(namespace.path, 'r') as file:
        read = file.read()

    # разделяем файл по данной строке
    raw_data = read.split("""----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.""")
    # удаляем последний пустой элемент списка
    raw_data.pop(len(raw_data) - 1)
    container = []
    # разбираем данные
    for message in raw_data:
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
        container.append(content)
    print()
    mail = [i['email'] for i in container]

    # считаем количество повторений почтовых ящиков
    coun = Counter()
    for i in mail:
        coun[i] += 1

    conf = [i['confidence'] for i in container]
    middle = sum(conf)/len(conf)  # считаем среднюю арефметическую
    print('Arithmetic mean:', middle)
    print()

    # формируем список кого нужно поместить в спам
    spam = list(set(map(lambda x: x['email'] if x['result'] != 'Innocent' else pass_fun(), container)))

    print('Spam list:')
    print(*spam, sep='\n')

    arr = [coun[i] for i in coun.keys()]

    # делаем гистограмму
    plt.figure('Histogram of senders')
    plt.title('Histogram of senders')
    plt.bar(range(len(coun.keys())), arr)
    plt.xticks(range(len(arr)), coun.keys(), size='small', rotation=90)
    plt.show()