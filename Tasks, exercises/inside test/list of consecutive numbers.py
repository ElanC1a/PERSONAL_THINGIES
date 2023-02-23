# В файле в столбик записаны целые числа. 
# Напиши программу, которая определяет длину самой длинной цепочки идущих подряд одинаковых чисел и выводит результат в другой файл.

file=open(r"C:\Program Files\Python310\1 Python programmes\Tasks, exercises\inside test\whole.txt",'r')

list_number=[]

for line in file:
    list_number.append(line.strip())
print(list_number)

count=0
number=list_number[0]
for line in list_number[1:]:  
    if line==number:
        number=line
        count+=1
    else:
        number=line
        count=1
print(count)


