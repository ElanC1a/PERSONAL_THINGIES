#3. Попробовать расположить элементы в таком же порядке, как на картинке (кнопка слева, любой элемент по центру, в моем случае это элемент Text, и располагаем кнопку справа) 
# функционал создать не требуется, но если сможешь, то будет вообще идеально. 
# Правда придется изучить этот момент самому
# left change text  middle input right clear

# change text - saves the text-->pastes it in

from tkinter import *
from tkinter.font import BOLD

window=Tk()
window.geometry("700x700")
window["bg"]="white"

def clear():
    text.delete("1.0","end")   #from first index to the end (index)
    text["fg"]="black"
    text["bg"]="white"

def change_bg():
    text["bg"]="skyblue"

def change_fg():
    text["fg"]="violet"

def button_additional():
    button_bg=Button(window, bg="gray", text="Change bg", font=("Arial", 11, BOLD), command=change_bg)
    button_bg.place(x=70, y=150)

    button_font=Button(window, bg="gray", text="Change font \n color", font=("Arial", 11, BOLD), justify=LEFT, command=change_fg)
    button_font.place(x=70,y=200)

button_change_text=Button(window, bg="gray", text="PRESS ME", font=("Arial", 11, BOLD), command=button_additional) #add command
button_change_text.place(x=70, y=100)    #(x=55, y=100) #(relx=.075, rely=.1)   

button_clear=Button(window, bg="gray", text="CLEAR", font=("Arial", 12, BOLD), command=clear) #add command
button_clear.place(x=570, y=100)

text=Text(window, bg="white", font=("Times New Roman", 11))
text.place(x=190,y=100)
text["height"]=27
text["width"]=40

window.mainloop()