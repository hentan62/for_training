import re
import sys
import pandas as pd

needed_rows = ['vvod.txt', 'vvod.txt']  # сюда вводим название файлов с рядами блоков


def row_block(input_rows):
    # считалка блоков из txt файла
    def sch(input_data):
        f = open(input_data, 'r', encoding="utf-8")
        a = {}
        for line in f:
            n = line.rstrip()
            if n not in a:
                a[n] = 1
            else:
                a[n] += 1
        f.close()
        return a

    def sum_dict(d1, d2):  # функция для суммирования значений словарей
        d = {}
        for k in (set(d1.keys()) | set(d2.keys())):
            d[k] = d1.get(k, 0) + d2.get(k, 0)
        return d

    nblock = {}
    for item in input_rows:
        nblock = sum_dict(nblock, sch(item))
    print(nblock)

    h1 = int(input("Введите высоту ряда блоков,мм: "))
    h = int(round(h1 / 100, 0))
    n = 0

    # перевод вычисленных значений при помощи
    # регулярных выражений к строке-спецификации
    result_arr = []
    for k in sorted(nblock.keys()):
        digit = re.findall('\d+', k)[0]
        try:
            letter = re.findall('\D+', k)[0]
        except IndexError:
            letter = ""
        print("количество блоков ", k, "равно ", nblock[k], "шт.")
        name = "П " + str(digit) + ".4." + str(h) + letter
        length = int(digit) * 100
        width = 400
        v1 = round(length * width * h1 / 10 ** 9, 2)
        vtotal = round(nblock[k] * v1, 2)
        n += 1
        result_arr.append([k, name, length, width, h1, nblock[k], v1, vtotal])
    df = pd.DataFrame(result_arr, columns=['short_name', 'full_name', 'length',
                                           'width', 'height', 'number', 'V1', 'Vfull'])
    return df


csv_dataset = row_block(needed_rows).to_csv('res_block.csv')
