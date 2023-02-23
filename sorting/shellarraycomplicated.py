import math
#import random

array=[0,3423,5,6,7,76,87,45,70]
#n=100
#for i in range (0,n):
#    array.append(random.randint(0,100))
print(array)

def shell_array(list):
    n=len(list)
    k=int(math.log2(n))
    interval=2**k-1

    while interval>0:
        for i in range(interval,n):
            element=list[i]
            g=i
            while g>=interval and list[g-interval]>element:
                list[g]=list[g-interval]
                g-=interval
            list[g]=element
        k-=1
        interval=2**k-1
    return list
shell_array(array)
print(array)
