#Определить четность числа

def even(number):
    if number<2:
        return (number%2==0)
    return even(number-2)
num=int(input())
x=even(num)
print(x)
