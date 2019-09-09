import csv
import operator
import pandas as pd

import cursor as cursor


def wczytaj():
    with open('zadanie2.csv' , newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(str(row))

def usun():
    with open('zadanie2.csv' , 'r') as xd ,open('edit.csv' , 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(xd):
            if len(row[1]) < 2:
                continue
            else:
                writer.writerow(row)
def reading():
    with open('edit.csv' , newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(str(row))
'''
def sortuj():
    with open('edit.csv' , 'r') as czytaj , open('edit2.csv' , 'w') as out:
        writer = csv.writer(out)
        lista = list()
        for row in csv.reader(czytaj):
            lista.append(row)
        for i in range(0 , len(lista) - 1):
           for j in range(0 , len(lista) - 1):
               if lista[j+1][0] < lista[j][0]:
                   buff = lista[j+1]
                   lista[j+1] = lista[j]
                   lista[j] = buff
        for row in list:
            writer.writerow(row)
'''
def wlasciwy_sort():
    with open('edit.csv', 'r') as czytaj, open('edit2.csv', 'w') as out:
        pass
    sample = open('edit.csv' , 'r')
    csv1 = csv.reader(sample , delimiter = ',')  # read sample delimiter
    sort = sorted(csv1 , key=operator.itemgetter(0))
    for eachline in sort:
        print(eachline)
def convert_to_int():
    with open('edit.csv', 'r') as czytaj, open('edit3.csv', 'w') as out:
        reader = csv.reader(czytaj)
        writer = csv.writer(out)
        for row in reader:
            try:
                row[0] = int(row[0])
                writer.writerow(row)
            except:
                writer.writerow(row)
        with open('edit3.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

            sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
            for row in sortedlist:
                print(row)
def zczytajedit():
    with open('edit3.csv', 'r') as czytaj:
        for row in czytaj:
            print(str(row))



def sorcik():
   # reader = csv.reader(open("edit.csv"), delimiter=",")
    #header = next(reader)
    #rows = [header + [[row[0],int(row[0]) ] for row in reader]
   with open('edit.csv', 'r') as f:
    reader = csv.reader(f , delimiter = ',')

    sortedlist = sorted(reader , key=operator.itemgetter(0) ,reverse=False)
    for row in sortedlist:
        print(row)
def readedit2():
    with open('edit.csv' , 'r') as out:
        for row in csv.reader(out):
            print(str(row))


if __name__ == '__main__':
    wczytaj()
    usun()
   # reading()htop
    #reading()
    #sortuj()
    #wlasciwy_sort()

   # readedit2()
   # reading()
    #sorcik()
    convert_to_int()
   # zczytajedit()
    #posortujedit()


