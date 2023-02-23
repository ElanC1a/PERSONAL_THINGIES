import math 
print("Note it is 1 land/2 land")
first_land=int(input("1 land: "))
second_land=int(input("2 land: "))

number_in_brakets=(first_land/second_land)

base_number=float(input("write the base number: "))
print(math.log(number_in_brakets, base_number))