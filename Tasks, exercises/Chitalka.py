# Напишите программу «Считалка», которая бы считала по просьбе пользователя. 
# Надо позволить пользователю ввести начало и конец счета, а также интервал между называемыми целыми числами. 
# (на самом деле эта задачка простенькая, тут нужно вспомнить про цикл for и "шаги" в нем)

start_number, end_number=int(input("Type your start number: ")), int(input())
interval=float(input("Write your desired interval: ")) #как довабить дробные числа? с float-->не работает 

format_print=(input("Column - [0], Row - [1]: ")) #задал тип данных int-->а в if ты сравниваешь ее со строкой

if format_print=="0":
    for i in range(start_number, end_number+1, interval):
        print(i)
elif format_print=="1":
    for i in range(start_number, end_number+1, interval):
        print(i, end=" ")   #end - passing the space to the end parameter indicates that the end character has to be identified by space and not a newline. 

