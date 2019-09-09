import random
import statistics




def randit():
    tab = []
    for i in range(0 , 250):
        tab.append(random.randint(0,300))
    return tab

def mediana(a):
    b = 0
    for x in a:
        b += x
    return b/len(a)

def sortuj(a):
    a.sort()
    a.reverse()
    return a

def check(a):
    tab = []
    for x in range(0,len(a)-1):
        for y in range(0 , len(a)-1):
            if ((x != y) and a[x] == a[y]  ) :
               # print("sdsdsdds")
                tab.append(a[x])
    tab.sort()
    tab.reverse()
    tab = set(tab)
    tab = sorted(tab)

    return tab


#def mediana(a):
  #  if len(a) % 2 != 0:
  #     return a[(len(a)-1)/2]
   # else:
    #    return (a[len(a)/2]+a[(len(a)/2)-1])/2

def check_if_no(a):
    bb = check(a)
    tab = list(range(0,300))
    p = 0
    for i in tab:
        for x in bb:
            if i == x:
                tab.remove(i)
    return tab



if __name__ == '__main__':
    print(randit())
    print(mediana(randit()))
    print(sortuj(randit()))
    print(statistics.median(randit()))
    print(statistics.stdev(randit()))
    print(check(randit()))
    xd = randit()
    xd.sort()
    print(xd)
    print(check(xd))
    print(check_if_no(xd))



