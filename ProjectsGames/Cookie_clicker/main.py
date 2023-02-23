from  tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import tkinter
from PIL import ImageTk, Image
import pyodbc 
import time 
import math


db_connection=pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-US7PAC1I;Database=wix_cookie_clicker;Trusted_Connection=yes;')
cursor=db_connection.cursor()

flag=False
id=0
passive_income=0

def initial_building_price(user_id):
    cursor.execute(f"SELECT owned_building_id, owned_building_amount, building_price FROM owned_building INNER JOIN building ON owned_building_id=building_id WHERE user_id={user_id}")  #carthage [(1,2,price), (2,3)]
    owned_buildings_survey=cursor.fetchall()

    for carthage in owned_buildings_survey:
        custom_price=carthage[2]*1.15**carthage[1] #price*1.15**amount
        cursor.execute(f"UPDATE building SET custom_building_price={custom_price} WHERE building_id={carthage[0]}")
        cursor.commit()

def button_command(user_id, building_id, window, repeat):
    global passive_income
    cursor.execute(f"SELECT cookie_amount FROM progress WHERE user_id={user_id}")
    user_money=cursor.fetchone()[0]

    cursor.execute(f"SELECT custom_building_price FROM building WHERE building_id={building_id}")
    building_cost=cursor.fetchone()[0]

    if user_money>=building_cost:
        #вычесть разницу в progress имея специфик user_id
        new_user_balance=user_money-building_cost
        cursor.execute(f"UPDATE progress SET cookie_amount={new_user_balance} WHERE user_id={user_id}")
        cursor.commit()

        #добавить в owned_building и изменить кол с специфик user_id
        cursor.execute(f"SELECT owned_building_amount FROM owned_building WHERE user_id={user_id} and owned_building_id={building_id}")
        no_build=cursor.fetchone()[0]+1
        
        cursor.execute(f"UPDATE owned_building SET owned_building_amount={no_build} WHERE user_id={user_id} and owned_building_id={building_id}")
        cursor.commit()

        #изменить цену в building, custom_building_price
        cursor.execute(f"SELECT building_price FROM building WHERE building_id={building_id}")
        b_price=cursor.fetchone()[0]

        new_build_price=b_price*1.15**no_build
        cursor.execute(f"UPDATE building SET custom_building_price={new_build_price} WHERE building_id={building_id}")
        cursor.commit()
        #price*1.15**amount building_cost*1.15**no_build
        passive_income=passive_cookie(user_id)
        window.update()
    else:
        showinfo("NO POSSIBLE", "NOT ENOUGH COOKIE")

def passive_cookie(user_id):
    global passive_income
    cursor.execute(f"SELECT owned_building_id, owned_building_amount FROM owned_building WHERE user_id={user_id}")
    owned_buildings_survey=cursor.fetchall() 

    for carthage in owned_buildings_survey:
        cursor.execute(f"SELECT building_power FROM building WHERE building_id={carthage[0]}")
        power=cursor.fetchone()[0]*carthage[1]
        passive_income+=power 
    return passive_income

def game(user_id):
    window=Toplevel()
    window.title('Wix Cookie clicker')
    window.geometry('1420x890')

    initial_building_price(user_id)

    potato_image=ImageTk.PhotoImage(Image.open('potato.png').resize((230,230)))

    cookie_button=Button(window, image=potato_image, command=lambda: update_amount(stat, user_id))
    cookie_button.place(x=150, y=175)

    cursor.execute(f"SELECT cookie_amount FROM progress WHERE user_id={user_id}")
    fetched_cookie=cursor.fetchone()

    stat=Label(window, text=f'Amount of cookies: {fetched_cookie.cookie_amount}', font=('Arial', 13)) #adjust the font and etc.
    stat.place(x=120, y=100)

    canvas=Canvas(window, width=400, height=700, bg='white')
    canvas.place(x=900, y=100)

    build_cursor=Button(canvas, text='Cursor',  bg='gray', command=lambda: button_command(user_id, 1, window, repeat))
    #build_cursor.grid(column=0, row=0)

    canvas.create_window(0,0, anchor=NW, window=build_cursor, width=400, height=70)

    build_grandma=Button(canvas, text='Grandma', width=10, height=5, bg='blue', command=lambda: button_command(user_id, 2, window, repeat))
    #build_grandma.grid(column=0, row=1)

    passive_income=passive_cookie(user_id)

    def repeat():
        cursor.execute(f"SELECT cookie_amount FROM progress WHERE user_id={user_id}")

        new_c_amount = cursor.fetchone()[0] + passive_income
            
        cursor.execute(f"UPDATE progress SET cookie_amount={new_c_amount} WHERE user_id={user_id}")
        cursor.commit()       
        
        stat.configure(text=f'Amount of cookies: {new_c_amount}')
        window.after(1000, repeat)

    window.after(0, repeat)

    window.mainloop() 

def update_amount(stat, l_id):
    cursor.execute(f"SELECT cookie_amount FROM progress WHERE user_id={l_id}")
    fetched_cookie=cursor.fetchone()

    no_cookie=fetched_cookie[0]+1
    print(no_cookie)

    stat.configure(text=f'Amount of cookies: {no_cookie}')
  
    cursor.execute(f"UPDATE progress SET cookie_amount={no_cookie} WHERE user_id={l_id}")
    cursor.commit()

#//////////////////
 
def login(login_entry, password_entry, u_login_window):
    global flag, id
    #verification part
    input_login_entry=login_entry.get().strip()
    input_password_entry=password_entry.get().strip()
    cursor.execute(f"SELECT id FROM user_info WHERE login='{input_login_entry}' and password='{input_password_entry}' ")
    res_cur=cursor.fetchone()[0]
    if res_cur!=None and (input_login_entry!="") and (input_password_entry!=""):
        flag=True
        id=res_cur
        first_window = Tk()
        first_window.title("Verification")
        first_window.geometry("250x200")
        verification_label=Label(first_window, text='Verification successful', font=('Arial', 13))
        verification_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        close_button = ttk.Button(first_window, text="Close window", command=lambda: [first_window.destroy(), u_login_window.withdraw(), game(id)])   
        close_button.place(relx=0.5, rely=0.5, anchor=CENTER)       #close_button-->first_window.destroy() is written
        
    else:
        showerror("Syntax error", "Wrong login or password")    

def user_add_to_db(u_login, u_password, u_conf_password, u_window):
    input_login=u_login.get().strip()
    input_password=u_password.get().strip()
    input_password_conf=u_conf_password.get().strip()
    if (input_login!="") and (input_password!="") and (input_password==input_password_conf):
        cursor.execute(f"INSERT INTO user_info (login, password) VALUES ('{input_login}', '{input_password}')")      #ACHTUG ACHTUG FUNKTIONIERT NICHT  #add the addition of users to db
        cursor.commit()
        cursor.execute(f"SELECT id FROM user_info WHERE login='{input_login}' and password='{input_password}'")
        saved_id=cursor.fetchone()[0]
        cursor.execute(f"INSERT INTO progress (user_id, cookie_amount) VALUES ({saved_id}, 0)")
        cursor.commit()

        showinfo('Registration', "You've successfully registered")
        u_window.destroy()
        login_window.deiconify()
    else:
        showerror("Wrong syntax", "Something wrong, better fix it :)")

def register():
    global login_image_b
    register_window=Toplevel()
    register_window.title(" R E G I S T E R ")
    register_window.geometry("350x500")
    register_window.resizable(0, 0)
    
    for_font=('Consolas', 13)

    #gradient frame
    j=0
    r=10
    for i in range(100):
        c=str(222222+r)
        Frame(register_window, width=10, height=500, bg="#"+c).place(x=j,y=0)   
        j=j+10                                                  
        r=r+1

    Frame(register_window, width=250, height=415, bg='white').place(x=50,y=50)

    #username label
    u_reg_label=Label(register_window, text='Username', bg='white')
    u_reg_label.config(font=for_font)
    u_reg_label.place(x=80, y=200)

    #username entry
    u_reg_entry=Entry(register_window, width=19, border=0)
    u_reg_entry.config(font=for_font)
    u_reg_entry.place(x=80, y=230)

    #password label
    p_reg_label=Label(register_window, text='Password', bg='white')
    p_reg_label.config(font=for_font)
    p_reg_label.place(x=80, y=280)

    #password entry
    p_reg_entry=Entry(register_window, width=19, border=0, show='*')
    p_reg_entry.config(font=for_font)
    p_reg_entry.place(x=80, y=310)
 
    def click(event):
        p_reg_entry_conf.config(state=NORMAL, font=for_font, show='*')
        p_reg_entry_conf.delete(0, END)

    #password entry re-confirmation
    p_reg_entry_conf=Entry(register_window, width=19, border=0)
    p_reg_entry_conf.insert(0, 'Confirmation')
    p_reg_entry_conf.config(state=DISABLED, font=('Consolas', 12))
    
    p_reg_entry_conf.bind("<Button-1>", click)
    p_reg_entry_conf.place(x=80, y=350)

    #lineframe on entry
    Frame(register_window, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(register_window, width=170, height=2, bg='#141414').place(x=80, y=252)
    Frame(register_window, width=180, height=2, bg='#141414').place(x=80, y=372)
    
    #register picture
    # login_image_a=Image.open("log_reg.png")         #PROBLEM PICTURE NOT SHOWING
    # login_image_b=PhotoImage(file="log_reg.png")

    login_picture=Label(register_window, image=login_image_b, border=0, justify=CENTER)
    login_picture.place(x=115, y=50)

    #login button    
    sign_up_button=Button(register_window,
    text='S I G N  U P',
    width=20,
    height=2,
    fg='white', 
    bg='#994422', 
    border=0, 
    activeforeground='#994422', 
    activebackground='white',
    command=lambda: user_add_to_db(u_reg_entry, p_reg_entry, p_reg_entry_conf, register_window))

    sign_up_button.place(x=90, y=400)   

# def on_enter(enter_button):
#         enter_button['background']='white'
#         enter_button['foreground']='#994422'

# def on_leave(leave_button):
#     leave_button['background']='#994422'
#     leave_button['foreground']='white'

# def login_window():
    
login_window = Tk()

login_image_a=Image.open("log_reg.png")
login_image_b=ImageTk.PhotoImage(login_image_a)

login_window.title(" L O G I N ")
login_window.geometry("350x500")
login_window.resizable(0, 0)

for_font=('Consolas', 13)

#gradient frame
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(login_window, width=10, height=500, bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

Frame(login_window, width=250, height=415, bg='white').place(x=50,y=50)

#username label
u_label=Label(login_window, text='Username', bg='white')
u_label.config(font=for_font)
u_label.place(x=80, y=200)

#username entry
u_entry=Entry(login_window, width=19, border=0)
u_entry.config(font=for_font)
u_entry.place(x=80, y=230)

#password label
p_label=Label(login_window, text='Password', bg='white')
p_label.config(font=for_font)
p_label.place(x=80, y=280)

#password entry
p_entry=Entry(login_window, width=19, border=0, show='*')
p_entry.config(font=for_font)
p_entry.place(x=80, y=310)

#lineframe on entry
Frame(login_window, width=180, height=2, bg='#141414').place(x=80,y=332)
Frame(login_window, width=180, height=2, bg='#141414').place(x=80,y=252)

#login picture
# login_image_a=Image.open("log.png")             #put in a function!!!!
# login_image_b=ImageTk.PhotoImage(login_image_a)

login_picture=Label(image=login_image_b, border=0, justify=CENTER)
login_picture.place(x=115, y=50)

#login button    
l_button=Button(login_window, 
text='L O G I N',
width=20,
height=2,
fg='white', 
bg='#994422', 
border=0, 
activeforeground='#994422', 
activebackground='white', 
command=lambda: login(u_entry, p_entry, login_window))

l_button.place(x=90, y=345)
# l_button.bind("<Enter>", on_enter(l_button))
# l_button.bind("<Leave>", on_leave(l_button))

#register button
r_button=Button(login_window,
text='R E G I S T E R',
width=20,
height=2,
fg='white', 
bg='#994422',
border=0, 
activeforeground='#994422', 
activebackground='white', 
command=lambda: [register(), login_window.withdraw()]) #, login_window.destroy()

r_button.place(x=90, y=400)
# r_button.bind("<Enter>", on_enter(r_button))
# r_button.bind("<Leave>", on_leave(r_button))

# login_window()
login_window.mainloop()

#//////////////////

if flag==True:
    game(id)