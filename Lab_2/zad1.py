
def znajd():
    tab = []
    for i in range(500 , 3000):
        if i % 7 == 0 and i % 5 != 0:
            tab.append(i)
    return tab;

def convert(x):
    xd = [str(i) for i in x ]
    return  xd

def polocz(x):
    xd = "";
    for i in x:
        xd+=str(i)
    return xd;

def zamien(x):
    for i in range(1 , len(x)):
        if(x[i] == '2' and x[i-1] == '1'):
            x[i] = 'X';
            x[i-1] = 'X';
        return x

def zamien2(x):
    x.replace("21" , "XX");
    return x

if __name__ == '__main__':
    print(znajd())
    print(convert(znajd()))
    print(polocz(znajd()))

    xd = polocz(znajd());

    print(xd.replace("81" , "XX"))
