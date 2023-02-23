# class Soda:
#     def __init__(self, drink):
#         self.drink=drink
#     def show_my_drink(self):
#         if self.drink=="":
#             print("Обычная газировка")
#         else:
#             print("Газировка %s" %self.drink)
# soda=Soda(input())
# soda.show_my_drink()
class TriangleChecker:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_triangle(self):
        if (self.a and self.b and self.c)>0:
            if ((self.a+self.b)<self.c):
                print("Жаль, но из этого треугольник не сделать.")
            else:
                print("Ура, можно построить треугольник!")
        elif (self.a and self.b and self.c)<0:
            print("С отрицательными числами ничего не выйдет!")
        
try:
    a=int(input())
    b=int(input())
    c=int(input())
except:
    print("Нужно вводить только числа!")
    quit()
    
tr=TriangleChecker(a,b,c)
tr.is_triangle()