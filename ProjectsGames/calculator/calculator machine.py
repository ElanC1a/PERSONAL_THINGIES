from tkinter import *

window=Tk()
window.title("ultra-calculator-machine")

e=Entry(window, width=35, borderwidth=5)  # Entry widget which allows displaying simple text. 
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #? each mean what???


#def 
def button_add():
    return

#button general

button_1=Button(window, text="1", padx=40, pady=20, command=button_add)
button_2=Button(window, text="2", padx=40, pady=20, command=button_add)
button_3=Button(window, text="3", padx=40, pady=20, command=button_add)
button_4=Button(window, text="4", padx=40, pady=20, command=button_add)
button_5=Button(window, text="5", padx=40, pady=20, command=button_add)
button_6=Button(window, text="6", padx=40, pady=20, command=button_add)
button_7=Button(window, text="7", padx=40, pady=20, command=button_add)
button_8=Button(window, text="8", padx=40, pady=20, command=button_add)
button_9=Button(window, text="9", padx=40, pady=20, command=button_add)
button_0=Button(window, text="0", padx=40, pady=20, command=button_add)


real_button_add=Button(window, text="+", padx=39, pady=20,command=button_add)
button_equal=Button(window, text="=", padx=40, pady=20, command=button_add)


#button screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

window.mainloop()