#Дано натуральное число. Определить:количество четных цифр в нем.

number=(int(input("Write your number: ")))
amount_even=0
amount_odd=0

while number>0:
    if number%2==0:
        amount_even+=1
    else:
        amount_odd+=1
    number=number//10   #// - это деление нацело-->с каждым циклом тебе нужно убирать разряд числа, чтобы разобрать следующее число
print("Even: %s"  %amount_even, "Odd: %s" %amount_odd)
