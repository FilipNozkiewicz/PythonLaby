import csv
import operator

data = csv.reader(open('edit.csv') ,lineterminator = '\n')
repair = []


def convert_to_int():
    for row in data:
        try:
            p =  [int(row[0]) , row[1]]
            repair.append(p)
        except:
            pass



#for row in data:
 #   repair.append(convert_to_int(row))

def print_convert():
    for row in repair:
        print(row)
def sorting():
    sortowane = sorted(repair , key=operator.itemgetter(0) , reverse=False)
    return sortowane

def printuj():
    xd = sorting()
    for row in xd:
        print(row)

def zapis():
    xd = sorting()
    with open('edit4.csv' , 'w') as out:
        writer = csv.writer(out)
        for row in xd:
            writer.writerow(row)

def czytnik():
    with open('edit4.csv', 'r') as czyt:
        reader = csv.reader(czyt)
        for row in reader:
            print(row)

duplikaty = []

def dup_inc():
    i = 1
    for row in repair:
        p = [i  , row[1]]
        duplikaty.append(p)
        i+=1
    return duplikaty

def print_dup():
    for row in duplikaty:
        print(row)




if __name__ == '__main__':
    convert_to_int()
    printuj()   # kurwa nareszczie
    zapis()
    czytnik()
    dup_inc()
    print_dup()