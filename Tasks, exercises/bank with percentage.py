# За каждый месяц банк начисляет к сумме вклада 7% от суммы. 
# Напишите консольную программу, в которую пользователь вводит сумму вклада и количество месяцев. 
# А банк вычисляет конечную сумму вклада с учетом начисления процентов за каждый месяц.

month=(int(input("Write amount of months: ")))
amount_money=(float(input("Write amount of money: ")))

for i in range (month):
     amount_money+=amount_money*0.07 

print(round(amount_money,1))