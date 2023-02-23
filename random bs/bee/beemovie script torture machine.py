import pyautogui 
import time

time.sleep(4)
f=open(r'C:\Program Files\Python310\1 Python programmes\random bs\bee\beemovie.txt' ,'r', encoding='ascii')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(2)

f.close()

#    time.sleep(4)
#    text=open('beemovie')
#    for each_line in text:
#        pyautogui.typewrite(each_line)
#        pyautogui.press('enter')

#send_message()According to all known laws of aviation, there is no way a bee should bBarry! Breakfast is ready!