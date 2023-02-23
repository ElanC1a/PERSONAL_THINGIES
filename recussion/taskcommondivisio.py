def common_factor(x,y): #(4,1)->(1,0)
    if y==0:
        return x
    else:
        return common_factor(y,x%y) 
                            #(4,5%4)->(1,4%1)->(1)
x=int(input())
y=int(input())

z=common_factor(x,y)
print(z)