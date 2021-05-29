#программка для перевода текстового файла в таблицу Эксель
#есть недоработки с регулярками
import re
import pandas as pd

number_ferm = []
name = []
emails = []
adresses = []
management = []
phones = []
f = open('test.txt', 'r', encoding="utf-8")


def printer(some):
    for name in some:
        print(name)


for line in f:
    a = re.search(r'^\d{10}\s[^\s]*', line)
    if re.findall(r'\«.*', line):
        name.append(line.rstrip())
    elif a != None:
        number_ferm.append(line.rstrip())
    elif re.findall(r'@', line):
        emails.append(line.rstrip())
    elif re.findall(r'^АДРЕС', line):
        adresses.append(line[6:].rstrip())
    elif re.findall(r'\(\d+\)', line):
        phones.append(line[9:].rstrip())
    elif re.findall(r'^РУКОВОДИТЕЛЬ', line):
        management.append(line[13:].rstrip())

arr_of_data = [number_ferm, management, phones, adresses, emails]


def creater_pd(data):
    df = pd.DataFrame(data)
    return df


df = pd.DataFrame(name)
for item in arr_of_data:
    df = pd.concat([df, creater_pd(item)], ignore_index=True, axis=1)
try:
    df.to_excel('farm.xls')
except:
    print("закрой файл эксель!!!!")
