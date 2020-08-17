import csv
from plotly.graph_objs import Bar
from plotly import offline

list_week = {}
def find_csv():
    list_one = []
    FILENAME = "July2020.csv"
    with open(FILENAME, "r", newline="",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            list_one.append(row)
    return list_one
list_one=find_csv()

diction = {}
for item in list_one:
    if item[8] not in diction:
        diction[item[8]]=float(item[11])
    else:
        diction[item[8]]+=float(item[11])
newkey=0

item_names, sum_of_products = [], []
for  keys, values in diction.items():
    item_names.append(keys)
    sum_of_products.append(values)

data = [{
    'type': 'bar',
    'x': item_names,
    'y': sum_of_products,
}]

my_layout = {
    'title': 'Количество изделий разных видов',
    'xaxis': {'title': 'Название изделий'},
    'yaxis': {'title': 'Количество изделий'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
