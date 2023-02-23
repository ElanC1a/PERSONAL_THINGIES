from tkinter import *
import tkinter as tk
from keras.models import load_model
import numpy as np
import win32gui
from PIL import Image, ImageGrab
import cv2 as c
from numberrecognition import train_picture

model=load_model(r'C:\Program Files\Python310\1_Python_programmes\neuro\digit_drawing_ai\digit_recog.h5')

class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x=0    
        self.y=0
        self.window=tk.Canvas(self,height=300,width=300,bg='white',cursor='spraycan')
        self.window.grid(column=0,row=0,padx=5,pady=5)
        
        self.recognize=tk.Button(self,text='Identify',command=self.digit_identify) #add def
        self.erase=tk.Button(self,text='Erase',command=self.erase_drawing)
        self.label=tk.Label(self,text='Not yet identified')
        
        self.label.grid(column=1,row=2,padx=5,pady=5)
        self.recognize.grid(column=1,row=0,padx=5,pady=5)
        self.erase.grid(column=2,row=0,padx=5,pady=5)

        self.window.bind('<B1-Motion>',self.draw)
        
    def draw(self,coordinate):
        self.x=coordinate.x
        self.y=coordinate.y
        brush=5
        self.window.create_oval(self.x+brush,self.y+brush,self.x-brush,self.y-brush,fill='black')

    def erase_drawing(self):
        self.window.delete('all')

    def digit_identify(self):
        id_window=self.window.winfo_id()
        id_coordinates=win32gui.GetWindowRect(id_window)
        ImageGrab.grab(id_coordinates).save('digit_saved_img.png')
        digit,accuracy=predict_digit()
        self.label.configure(text=(str(digit)))

def predict_digit():
    picture_load=c.imread('digit_saved_img.png')
    picture_load=c.resize(picture_load,train_picture[0].shape,interpolation=c.INTER_AREA)
    picture_load=c.cvtColor(picture_load,c.COLOR_BGR2GRAY)
    picture_load=(255-picture_load)/255         #?????
    picture_load=np.expand_dims(picture_load,axis=0)        #?????
    
    result=model.predict(picture_load)  #???
    print(result)
    print(result.argmax())
    return np.argmax(result), max(result)

interface=Interface()

mainloop()