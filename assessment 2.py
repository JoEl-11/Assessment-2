import random
import itertools
l1=[]
def rand_no():
    for i in range(4):
        l1.append(random.randint(0,9))
    print(l1)
    return l1
def guess_no():
    no=input("\nguess the random number: ")
    l2=[int(no[0]),int(no[1]),int(no[2]),int(no[3])]
    return l2
def check():
    for (x,i) in zip(n2,n1):
            if x== i:
                print("R",end='')
            if x not in n1:
                print("B",end='')
            elif x!=i:
                print("Y",end='')
n=10
n1=rand_no()
while (n>0):
    n2= guess_no()
    n=n-1
    if(n1==n2):
        print("\nyou guessed it right")
        break
    check()
else:
    print("\nyou are out of chances")
    
