#Преобразовать список, состоящий из списков, в обычный список
# [[5,6,7],["Hello"]]-->[5,6,7,"Hello"]/ isinstance()
def spisok(x):
    if x==[]:
        return x
    elif isinstance(x[0],list):
        return spisok(x[0])+spisok(x[1:])
    else:       
        return (x[:1]+spisok(x[1:]))
s=[[5,6,7],["Hello"],6,9,"h"]
z=spisok(s)
print(z)