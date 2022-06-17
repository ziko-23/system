# exercice 1
# qst1
from cgi import print_exception


def multiplede(x):
    for i in range(10):
        print(i , " * ", x," = ", i*x)
# multiplede(9)
# ex2
def existOuNon(L,a):
    if a in L:
        return True
    else :
        return False

# qst3
def multiparn(L,n):
    list = []
    for i in range(len(L)):
        list.append(L[i]*n)
    return list

# qst4
def positionde(L,a):
    for i in range(len(L)):
        if L[i] != a and i != len(L)-1:
            pass
        elif L[i] == a:
            return i+1
        elif L[i] != a and  i == len(L)-1:
            return -1
# qst5
def pairInpair(L):
    dict = {}
    for i in range(len(L)):
        if i%2 == 0 :
            dict[L[i]] = "pair"
        else:
            dict[L[i]] = "impair"
    return dict



# qst6

def fun(L):
    M = list(())
    for i in range(len(L)):
        t = tuple((L[i] , L.count(L[i])))
        if M.count(t) == 0:
            M.append(t)
        else:
            pass
    print(M)
# fun([22 , 7 , 14 , 22 , 7 , 14 , 7 , 14 , 11 , 7])






# exercice 2
class Book:
    def __init__(self,title, author, price):
        self.title = title
        self.autor = author
        self.price = price
    
    def view(self):
        print("Title : ",self.title)
        print("Author : ",self.autor)
        print("Price : ",self.price)
book = Book("GOT","george rr martin",999)
book.view()