import csv
list_week = {}


def find_csv():
    list_one = []
    FILENAME = "July2020.csv"
    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            list_one.append(row)
    return list_one

list_one=find_csv()


date_list = []
for items in list_one:
    if items[1] in date_list:
        continue
    else:
        date_list.append(items[1])
        
newarr = []
item_for_date = []
a = 0
for newitems in list_one:
    if newitems[1] == date_list[a]:
        item_for_date.append(newitems)
    else:
        newarr.append(item_for_date)
        item_for_date=[newitems]
        a+=1
print(newarr)

def printer_items(list):
    diction = {}
    for item in list:
        if item[8] not in diction:
            diction[item[8]]=float(item[11])
        else:
            diction[item[8]]+=float(item[11])
    newkey = 0
    for  key in sorted( diction.keys()):
        print(str(key) +"=" + str(diction[key]), "шт")
        newkey+=int(diction[key])
    print("всего изделий: ", newkey, "шт")
for values in newarr:
    print("\n на число " + values[0][1])
    printer_items(values)
