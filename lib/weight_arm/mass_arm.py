import re

def mass_arm(diam):
    with open("GOST_5781_6727.txt",'r') as wq:

        a={}
        for line in wq:
            line=line.rstrip()
            x=line.split(' ')
            res=x[1:]
            ish=x[0]
            a[ish]=res
        return a


def find_mass_arm(d, l, n):
    mass_dict=mass_arm(d)
    res = mass_dict[str(d)]
    m = float(res[1])
    m=m*l/1000
    m=round(m,3)
    m1=m*n
    m1=round(m1,2)
    print ("\n"+str(n)+"d"+str(d)+"масса одного стержня,"+str(m)+" кг")
    print ("масса арматуры заданного диаметра=%.3f" % m1, "кг")

    
with open('arm.csv', encoding='UTF-8') as f:
    for line in f:
        string = line
        if re.search('AIII', line):
            arr = re.split('AIII L=',string)
        elif re.search('AI', line):
            arr = re.split('AI L=',string)
        dig = re.findall('\d',arr[0])
        diam = int(''.join(dig))
        arr2 = re.split('\t', arr[1].strip())
        length = int(arr2[0])
        n = int(arr2[1])
        print(diam, length, n)
        find_mass_arm(diam, length, n)
