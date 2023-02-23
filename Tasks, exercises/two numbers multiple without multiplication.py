# Напишите программу, которая вводит два целых числа и находит их произведение, не ис-пользуя операцию умножения.
#  Учтите, что числа могут быть отрицательными
number_1=int(input("number 1: "))
number_2=int(input("number 2: "))
total=0
i=0

if (number_1 or number_2)<0 or (number_2, number_1)<0:
    for i in range (abs(number_1)):
        total= total + abs(number_2)
    total= - total
    print(total)

else:
    for i in range (abs(number_1)):
        total= total + abs(number_2)
    print(total)

#def product():
 #   result=0
  #  for i in range (abs(number_1)):
   #     result= result + abs(number_2)
    #print(result)

#if number_1>0 and number_2>0:
#    product() 

#elif number_1<0 or number_2<0:
#    product()

            