# x=5
# def factorial(number):
#     if number==1:
#         return number
#     else:
#         return number*factorial(number-1)

# def factorial_bad(number):
#     factorial=1
#     if number<0:
#         print('ERROR')
#     else:
#         for i in range(1,number+1):
#             factorial=factorial*i
#         print(factorial)
# print(factorial(x))
# factorial_bad(x)

def fibbonaci(number):
    if number==0 or number==1:
        return number
    else:
        return fibbonaci(number-1)+fibbonaci(number-2)

for i in range(10):
    print(fibbonaci(i))
