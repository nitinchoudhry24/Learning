'''
Created on 01-Dec-2016

@author: nitinchoudhry
'''
def main():
    
    MYLIST=1
    T=[MYLIST]*2
    print T
    T[1]=100
    print T
    k=map(j, T)
    print k
    
def j(x):
    return x+1


main()