from cProfile import label
from ctypes import sizeof
from tkinter import *
import time
from turtle import down

def button_operation():
    print("Click")
    label_1["bg"]="blue"

window=Tk() #Tk()- весь модуль
window.title("Start window")
window.geometry("1000x1000")
window["bg"]="white"
#button
button_1=Button(window, bg="red", text="PRESS THE BUTTON!", font=("Arial", 11, "italic"),  command=button_operation) #all colors with lowercase
button_1.place(x=400, y= 900) #pack() - allows the button the be placed

#label
label_1=Label(window, text="I am  the BUTTON! \n YES!", bg="purple", font=("Arial", 11, "bold"),fg="black", justify=CENTER) #justif - allows user the display the text in left, right, center 
label_1.place(x=390, y=770, width=210, height=100)

# canvas
painting=Canvas(bg="white")
painting.pack() #placed same way as the butto
painting["height"]=500
painting["width"]=500
#painting.create_line(0,0,50,50) #two starting points to two finishing ones
#painting.create_rectangle(70,70,140,140, fill="blue", outline="orange", width=3, activefill="white")
oval=painting.create_oval(100,100,150,150, fill="red")

# for i in range(40):
#    painting.move(oval,10,0)
#    painting.update()
#    time.sleep(0.05)

def moving_oval(event):
    if event.keysym=="Up":
        painting.move(oval,0,-5)
    elif event.keysym=="Down":
        painting.move(oval,0,5)
    elif event.keysym=="Right":
        painting.move(oval,5,0)
    elif event.keysym=="Left":
        painting.move(oval,-5,0)

painting.bind_all("<Up>", moving_oval)
painting.bind_all("<Down>", moving_oval)
painting.bind_all("<Left>", moving_oval)
painting.bind_all("<Right>", moving_oval)

print(painting["width"], painting["height"])
    
window.mainloop() 