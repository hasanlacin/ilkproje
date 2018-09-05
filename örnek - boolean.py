import math

def isDivisible(x,y):

    if(x%y==0):
        return True
    else:
        return False

def karekok(x,a):
    while  True:
        print(x)
        y= (x+a/x)/2
        if y==x :
            break
        x=y
    return x


def faktoriel(x):
    if(x==0):
        return 1
    else:
        return x* faktoriel(x-1)


print (karekok(16,8))

print (isDivisible(4,2))

print (faktoriel(4))