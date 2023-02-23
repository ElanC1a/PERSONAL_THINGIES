#4. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
# В исходном списке минимум 2 элемента.

list_number=[]
def change():      #why change(lst) - lst in brackets? why?
    n=int(input("amount of elements in a list: "))
    for imp in range(0, n):
        imp=int(input())
        list_number.append(imp)
    print(list_number)
    print("Now magic will happen...")
    first_number=list_number[0]
    list_number[0]=list_number[-1]
    list_number[-1]=first_number
    print(list_number)
change()
