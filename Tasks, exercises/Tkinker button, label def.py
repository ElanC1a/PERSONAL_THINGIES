# 2. Написать программу с использованием модуля tkinter,
# которая при нажатии кнопки будет менять цвет уже отрисованного квадрата (Всего можно 3 цвета сделать)
from tkinter import *
from cProfile import label
from ctypes import sizeof

def button_operation_blue():
    canvas["bg"]="blue"

def button_operation_red():
    canvas["bg"]="red"

def button_operation_green():
    canvas["bg"]="green"

window=Tk()
window.title("Start window")
window.geometry("1000x1000")
window["bg"]="white"

button_1=Button(window, bg="blue", text="color blue", font=("Arial", 11), comman=button_operation_blue)
button_1.place(x=450, y=100)

button_1=Button(window, bg="red", text="color red", font=("Arial", 11), comman=button_operation_red)
button_1.place(x=350, y=100)

button_1=Button(window, bg="green", text="color green", font=("Arial", 11), comman=button_operation_green)
button_1.place(x=550, y=100) #did not change name button_1-->still works, why? weird...

#canvas
canvas=Canvas(bg="white")
canvas.place(x=250, y=300)
canvas["height"]=500
canvas["width"]=500

window.mainloop()