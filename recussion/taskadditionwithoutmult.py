#adding numbers without addition only using recussion

def addition(x,y):
    if(y==0):
        return x
    else:
        return (1+(addition(x,y-1)))

x=int(input())
y=int(input())
print(addition(x,y))