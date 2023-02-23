from functools import reduce
cube=lambda x: x**3
# print(cube(int(input())))

a=[4,5,6,6,8,8]
A=list(filter(lambda x:(x%2==0),a))
# print(A)

a=['6','7','8','9']
b=list(map(int,a))
# print(b)

c=list(map(lambda x: x*2,b))
# print(c)

# reduce - 
sugma=reduce((lambda x, y: x+y),c)
# print(sugma)

d=[lambda x=x: x for x in range(1,11)]
#for i in d:
#     print (i())

z=[x for x in range(1,11)]
# print(z)

# d=list(map(lambda x: x+1, range(1,11)))
# print(d)

e=lambda x,y: f"{x} is bigger" if x>y else f"{y} is bigger"
#print(e(1,2))

spisok=[[8,7,6],[3,4,10,5],[6,7,9,8]]
f=lambda lisst: (sorted(i) for i in lisst)
g=lambda method,lissst: [j[-2] for j in method(lissst)]
result=g(f,spisok)
print(result)

def second(x):
    for i in x:
        i.sort()       
        print(i[-2])

#second(spisok)