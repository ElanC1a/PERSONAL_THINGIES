from main import *
from main import stat

while True:
        i=0
        while i < 5:
            time.sleep(0.2)
            i += 1
            cursor.execute(f"SELECT cookie_amount FROM progress WHERE user_id=1008")

        new_c_amount = cursor.fetchone()[0] + passive_income
            
        cursor.execute(f"UPDATE progress SET cookie_amount={new_c_amount} WHERE user_id=1008")
        cursor.commit()       
        
        stat.configure(text=f'Amount of cookies: {new_c_amount}')
    