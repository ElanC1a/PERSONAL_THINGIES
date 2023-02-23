import os
from pydoc import plain
import time 
import smtplib as smt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#регистрация
my_email='murat.unoff@gmail.com'
password='aumlapcngmhklhsk'
def welcome():
    global my_email, password
    list_of_users=[]
    admin=Admin('valera', 'valera', 'valera', 'valera', 'valera')

    while True:
        print('Welcome, do you wish to register, login, reset password or leave:')
        answer=input('Enter: ').strip()
        answer=answer.lower()
        os.system('cls')
        if answer=='register':
            print('Please state your name, surname, login and password')
            registration(list_of_users)
            #print(list_of_users)
            os.system('cls')
        elif answer=='login':
            print('Please state your login and password')
            login(list_of_users, admin)
            time.sleep(2)
            os.system('cls')
        elif answer=='reset password':
            user_input_login=input('Your login: ')
            for i in list_of_users:
                if i.login==user_input_login:
                    message=MIMEMultipart()
                    message['From']=my_email
                    message['To']=i.email
                    message['Subject']='PERSONAL PASSWORD'
                    text_message=i.password
                    message.attach(MIMEText(text_message, 'plain'))
                    server=smt.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(my_email, password)
                    server.send_message(message)
                    server.quit()
        elif answer=='leave': 
            print('Goodbye')
            time.sleep(2)
            os.system('cls')
            break
        else:
            print('Error, wrong syntax')

def registration(list_user_add):
    user_name=input('Name: ')
    user_surname=input('Surname: ')
    user_login=input('Login: ')
    user_password=input('Password: ')
    user_email=input('Email: ')
    users=Users(user_name, user_surname, user_login, user_password, user_email)
    list_user_add.append(users)

def admin_window(list_of_user, admin):
    while True:    
        admin_answer=input('Do you wish to view all users? (yes/ no): ').strip()
        admin_answer=admin_answer.lower()
        if admin_answer=='yes' or admin_answer=='y':     
            admin.show_all(list_of_user)
            if not list_of_user:
                print('No users detected')
                break
            else:
                admin_sec_answer=input('Do you wish to make changes? (yes/no): ').strip()
                admin_sec_answer=admin_sec_answer.lower()
                if admin_sec_answer=='yes' or admin_sec_answer=='y':
                    admin_third_answer=input('Remove all users (1) or remove users by index (2): ')
                    if admin_third_answer=='1':
                        admin.delete_all(list_of_user)
                    elif admin_third_answer=='2':
                        admin.delete_by_index(list_of_user)
                    else:
                        print('Syntax error')
                elif admin_sec_answer=='no' or admin_sec_answer=='n':
                    print('Returning to the main menu')
                    break

        elif admin_answer=='no' or admin_answer=='n':
            print('Returning to the main menu')
            break
        else:
            print('Syntax error')
    
def login(list_of_users, admin):
    user_login=input('Login: ')
    user_password=input('Password: ')
    r_w=True
    if user_login==admin.login and user_password==admin.password:
        admin_window(list_of_users, admin)  
    if user_login!=admin.login or user_password!=admin.password:    
        for i in list_of_users:
            if user_login==i.login:
                if user_password==i.password:
                    print('Login succesfull')
                    r_w=False
                    i.data()
                    time.sleep(2)
                    os.system('cls')
                else:
                    print('Password is incorrect')
                    r_w=False
        if r_w==True:
            print('Login is incorrect')
            time.sleep(2)
            os.system('cls')
        
class Users:
    def __init__(self, name, surname, login, password, email):
        self.name=name
        self.surname=surname
        self.login=login
        self.password=password
        self.email=email
    def data(self):
        print(f'Name: {self.name}, surname: {self.surname}, login: {self.login}, password: {self.password}')
        
class Admin(Users):
    def __init__(self, name, surname, login, password, email):
        super().__init__(name, surname, login, password, email)
    def show_all(self, list_of_users):
        count=0
        for i in list_of_users:
            print(f'id: {count}', end=' ')
            i.data()
            count+=1
    def delete_all(self, list_of_users):
        print('Deletion completed')
        list_of_users.clear()
        time.sleep(2)
        os.system('cls')
    def delete_by_index(self, list_of_users):
        try:
            admin_index_answer=int(input('Which user to remove: '))
            if admin_index_answer in range(len(list_of_users)):
                del list_of_users[admin_index_answer]
            else:
                print('Wrong index')

        except:
            print('Syntax error')
welcome()