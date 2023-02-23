list=[1,2,4,5,6]

def addition(lisst,lenght):
    if lenght==0:
        return 0
    else:
        return addition(lisst,lenght-1)+lisst[lenght-1]

x=len(list)
y=addition(list,x)
print(y)