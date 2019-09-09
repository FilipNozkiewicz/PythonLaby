

plansza1 = list(range(0,9))
#print(plansza1)
plansza1[:9] = [0] * 9
#print(plansza1)
zajete = list(range(0,9))
zajete[:9] = [False] * 9


def draw(x):
    if(x == 0):
        return ' '
    if(x == 1):
        return 'O'
    if(x == 2):
        return 'X'

def plansza():
    print("                     -------")
    print("                     |"+draw(plansza1[0])+"|"+draw(plansza1[1])+"|"+draw(plansza1[2])+"|" )
    print("                     -------" )
    print("                     |"+draw(plansza1[3])+"|"+draw(plansza1[4])+"|"+draw(plansza1[5])+"|" )
    print("                     -------" )
    print("                     |"+draw(plansza1[6])+"|"+draw(plansza1[7])+"|"+draw(plansza1[8])+"|" )
    print("                     -------" )

def check(x):

    if x >= 0 and x < 9:
        if(zajete[x] == False):
            zajete[x] = True
            return True;
        else:
            print("Pole zajete")
            return False
    else:
         print("od 0 do 8")
         return False

def play():

    for i in range(0,9):
        xd = False
        while(xd != True):

            print ( "Your move on Pole nr: " );
            x = input ()
            try:
               x =  int(x)
               if (check ( x ) == True):
                   if i % 2 == 0:
                     xd = True
                     plansza1[x] = 1
                     plansza()
                     if(result()):
                         print ( "Winner is " + draw ( plansza1[x] ) )
                         return
                   else:
                      xd = True
                      plansza1[x] = 2
                      plansza()
                      if (result ()):
                          print ( "Winner is " + draw ( plansza1[x] ) )
                          return
               else:
                   print("od 0 do 9")


            except:
                print("od 0 do 9")


def result():
    if(plansza1[0] != 0  and plansza1[0] == plansza1[1] and plansza1[0] == plansza1[2]):
      return True
    if (plansza1[3] != 0 and plansza1[3] == plansza1[4] and plansza1[3] == plansza1[5]):
        return True
    if (plansza1[6] != 0 and plansza1[6] == plansza1[7] and plansza1[6] == plansza1[8]):
        return True
    if (plansza1[0] != 0 and plansza1[0] == plansza1[3] and plansza1[0] == plansza1[6]):
        return True
    if (plansza1[1] != 0 and plansza1[1] == plansza1[4] and plansza1[1] == plansza1[7]):
        return True
    if (plansza1[2] != 0 and plansza1[2] == plansza1[5] and plansza1[2] == plansza1[8]):
        return True
    if (plansza1[0] != 0 and plansza1[0] == plansza1[4] and plansza1[0] == plansza1[8]):
        return True
    if (plansza1[6] != 0 and plansza1[6] == plansza1[4] and plansza1[6] == plansza1[2]):
        return True
    else:
        return False


if __name__ == '__main__':
     print("TIC TAC TOE")
     play()