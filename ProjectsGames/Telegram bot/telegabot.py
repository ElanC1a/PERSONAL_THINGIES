from telebot import *
import random
from os import *
from secrets import choice
hp=0
damage=0
exp=0
lvl=1
max=0
monster_list=["ghoul", "skeleton", "zombie", "creeper", "enderman"]
monster_hp=[5, 20, 17, 6, 15]
monster_damage=[10, 20, 15, 12]
monster=[]


bot=telebot.TeleBot("5564429631:AAGrDfkh51VO43t62pLMFUtOjnsGU3E96uI")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "This is a function menu \n These functions can be used: /start")

@bot.message_handler(commands=["start"])
def start(message):
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start=types.KeyboardButton("Start the journey")
    button_about=types.KeyboardButton("About")
    button_exit=types.KeyboardButton("Exit")
    keyboard.add(button_start,button_about,button_exit)
    bot.send_message(message.chat.id,"Welcome, my dear traveller! This is dungeon bot 🧙‍♀️", reply_markup=keyboard)

#@bot.message_handler(content_types=["text"])

#def repeat(message):
#    bot.send_message(message.chat.id,message.text)

def create_monster():
    name_monster=monster_list[random.randint(0,len(monster_list)-1)]
    hp_monster=monster_hp[random.randint(0, len(monster_hp)-1)]*lvl#add according to player lvl
    damage_monster=monster_damage[random.randint(0, len(monster_damage)-1)]*lvl #add according to player lvl
    return name_monster, hp_monster, damage_monster

@bot.message_handler(content_types=["text"])
def create_character(message):
    global hp,damage,exp,lvl, monster,max
    monster_tuple=create_monster()
    if len(monster)!=3:
        monster=list(monster_tuple)
    #starting menu
    if (message.text=="Start the journey"):
        hp=0
        damage=0
        lvl=1
        exp=0
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_elf=types.KeyboardButton("Elf")
        button_dwarf=types.KeyboardButton("Dwarf")
        button_beast=types.KeyboardButton("Beast")
        keyboard.add(button_elf,button_dwarf,button_beast)
        bot.send_message(message.chat.id,"Choose your race", reply_markup=keyboard)
    elif (message.text=="About"):
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_start=types.KeyboardButton("Start the journey")
        button_about=types.KeyboardButton("About")
        button_exit=types.KeyboardButton("Exit")
        keyboard.add(button_start,button_about,button_exit)
        bot.send_message(message.chat.id, "This is game bot in development, create by Murat. A\nIt is sort of like old pokemon game, just without graphics and less features.\nEnjoy it, I guess...", reply_markup=keyboard)
    elif (message.text=="Exit"):
        hp=0
        damage=0
        lvl=1
        exp=0
        keyboard=telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "It is sad to see you go \nDungeon will be waiting for your return", reply_markup=keyboard)
    #races
    elif (message.text=="Elf"):
        hp+=15
        damage+=10      
        bot.send_photo(message.chat.id, photo="https://www.kindpng.com/picc/m/94-948643_soul-knight-elf-pixel-art-hd-png-download.png")
        #img=open('C:\Program Files\Python310\1 Python programmes\ProjectsGames\Telegram bot\elf.png', 'rb')
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_swordsman=types.KeyboardButton("Swordsman")
        button_archer=types.KeyboardButton("Archer")
        button_alchemist=types.KeyboardButton("Alchemist")
        keyboard.add(button_swordsman,button_archer,button_alchemist)
        bot.send_message(message.chat.id, "Choose your class", reply_markup=keyboard)
    elif (message.text=="Dwarf"):
        hp+=13
        damage+=12
        bot.send_photo(message.chat.id, photo="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e6668f34-087f-446f-a6ca-af81c02fc336/d67wt1r-195c6787-3e47-4a75-885b-38acfd98ffc8.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2U2NjY4ZjM0LTA4N2YtNDQ2Zi1hNmNhLWFmODFjMDJmYzMzNlwvZDY3d3Qxci0xOTVjNjc4Ny0zZTQ3LTRhNzUtODg1Yi0zOGFjZmQ5OGZmYzguanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7XCotz_gRVtMAtOrF_jKcYlYoC_EixzbwkdQKADdzw8")
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_swordsman=types.KeyboardButton("Swordsman")
        button_archer=types.KeyboardButton("Archer")
        button_alchemist=types.KeyboardButton("Alchemist")
        keyboard.add(button_swordsman,button_archer,button_alchemist)
        bot.send_message(message.chat.id, "Choose your class", reply_markup=keyboard)
    elif (message.text=="Beast"):
        hp+=15
        damage+=15
        bot.send_photo(message.chat.id, photo="https://www.nicepng.com/png/detail/440-4406506_werewolf-pixel-werewolf.png")
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_swordsman=types.KeyboardButton("Swordsman")
        button_archer=types.KeyboardButton("Archer")
        button_alchemist=types.KeyboardButton("Alchemist")
        keyboard.add(button_swordsman,button_archer,button_alchemist)
        bot.send_message(message.chat.id, "Choose your class", reply_markup=keyboard)
    #classes
    elif (message.text=="Swordsman"):
        hp+=3
        damage+=7
        max=hp
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_explore=types.KeyboardButton("Explore")
        button_leave=types.KeyboardButton("Leave")
        keyboard.add(button_explore, button_leave)
        bot.send_message(message.chat.id, f"Hp: {hp} \nDamage: {damage} \nYour action:",reply_markup=keyboard)
    elif (message.text=="Archer"):
        hp+=4
        damage+=4
        max=hp
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_explore=types.KeyboardButton("Explore")
        button_leave=types.KeyboardButton("Leave")
        keyboard.add(button_explore, button_leave)
        bot.send_message(message.chat.id, f"Hp: {hp} \nDamage: {damage} \nYour action:",reply_markup=keyboard)
    elif (message.text=="Alchemist"):
        hp+=7
        damage+=3
        max=hp
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_explore=types.KeyboardButton("Explore")
        button_leave=types.KeyboardButton("Leave")
        keyboard.add(button_explore, button_leave)
        bot.send_message(message.chat.id, f"Hp: {hp} \nDamage: {damage} \nYour action:",reply_markup=keyboard)
    #explore or leave
    elif (message.text=="Explore" or message.text=="Re-enter the dungeon"):           #maybe add creating monster here + put every action under elif???
        encounter=random.randint(0,1) #0 - nobody, 1 - enemy in front 
        if encounter==0: #nobody-->2 options
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_explore=types.KeyboardButton("Explore")
            button_fresh_air=types.KeyboardButton("Get fresh air")                  
            keyboard.add(button_explore, button_fresh_air)
            bot.send_message(message.chat.id, "there is nobody, just wind...", reply_markup=keyboard)
        elif encounter==1: #enemy !!!! get back to it
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_attack=types.KeyboardButton("Attack")
            button_flee=types.KeyboardButton("Flee")
            keyboard.add(button_attack, button_flee)                                    
            #creating a monster
            bot.send_message(message.chat.id, f"There is an enemy in front \nMonster: {monster[0]}   Monster Hp: {monster[1]}   Monster Damage: {monster[2]}\nYour Hp: {hp}   Damage: {damage}\nYour action:",reply_markup=keyboard)
    elif (message.text=="Attack"):
        monster[1]-=damage
        if monster[1]>0: #still alive (monster)
            hp-=monster[2]
            if hp<=0:
                hp=0
                damage=0
                exp=0
                lvl=1
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_start=types.KeyboardButton("Start the journey")
                button_about=types.KeyboardButton("About")
                button_exit=types.KeyboardButton("Exit")
                keyboard.add(button_start,button_about,button_exit)
                bot.send_message(message.chat.id, "Game Over", reply_markup=keyboard)
            else:
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_attack=types.KeyboardButton("Attack")
                button_flee=types.KeyboardButton("Flee")
                keyboard.add(button_attack, button_flee)
                bot.send_message(message.chat.id, f"Monster Hp: {monster[1]}   Monster Damage: {monster[1]}\nHp: {hp}   Damage: {damage} \nYour action:", reply_markup=keyboard)
        elif monster[1]<=0:
            exp+=10
            monster=[]
            rnd_nm=random.randint(0,4)
            heal_potions={3:"small potion", 5:"medium potion",7:"large potion"}
            heal=choice(list(heal_potions.keys()))
            if rnd_nm==2 and not hp==max:
                hp+=heal    
                if hp>max:
                    difference=hp-max
                    hp-=difference
            bot.send_message(message.chat.id, f"Lucky you, you found a {heal_potions[heal]}")
            #bot.send_message(message.chat.id, f"Your exp: {exp}")
            if exp%50==0:
                exp=0
                lvl+=1
                max+=4
                damage+=5
                bot.send_message(message.chat.id, f"Lvl up\nYour hp: {hp}   Damage: {damage}   Lvl: {lvl}")
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_explore=types.KeyboardButton("Explore")
            button_fresh_air=types.KeyboardButton("Get fresh air")
            keyboard.add(button_explore, button_fresh_air)
            bot.send_message(message.chat.id,f"Congrats, you've defeated the monster\nYour exp: {exp}\nYour move: ", reply_markup=keyboard)
    elif (message.text=="Flee"):
        luck=random.randint(0,1)
        if luck==0:
            monster=[]
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_explore=types.KeyboardButton("Explore")
            button_leave=types.KeyboardButton("Leave")
            keyboard.add(button_explore,button_leave)
            bot.send_message(message.chat.id, "You've escaped... for now", reply_markup=keyboard)
        elif luck==1:
            hp-=monster[2]
            keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_attack=types.KeyboardButton("Attack")
            button_flee=types.KeyboardButton("Flee")
            keyboard.add(button_attack, button_flee)
            bot.send_message(message.chat.id, f"Oops, unlucky...\nMonster Hp: {monster[1]}   Damage: {monster[2]}\nYour Hp: {hp}   Damage: {damage}\nYour move: ", reply_markup=keyboard)
            if hp<=0:
                hp=0
                damage=0
                exp=0
                lvl=1
                max=hp
                keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_start=types.KeyboardButton("Start the journey")
                button_about=types.KeyboardButton("About")
                button_exit=types.KeyboardButton("Exit")
                keyboard.add(button_start,button_about,button_exit)
                bot.send_message(message.chat.id, "Game Over", reply_markup=keyboard)
    elif (message.text=="Leave"):
        monster=[]
        hp=0
        damage=0
        exp=0
        lvl=1
        max=hp
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_start=types.KeyboardButton("Start the journey")
        button_about=types.KeyboardButton("About")
        button_exit=types.KeyboardButton("Exit")   #write when exit 
        keyboard.add(button_start,button_about,button_exit)
        bot.send_message(message.chat.id, "The dungeon will be waiting🗻",reply_markup=keyboard)
    elif (message.text=="Get fresh air"):
        monster=[]
        keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_reenter_dungeon=types.KeyboardButton("Re-enter the dungeon")
        button_leave=types.KeyboardButton("Leave")
        keyboard.add(button_reenter_dungeon,button_leave)
        bot.send_message(message.chat.id, "Your action padawan: ",reply_markup=keyboard)
    
@bot.message_handler(content_types = ['photo'])
def handle_docs_photo(message):
    file_id = message.photo[-1].file_id
    print(file_id)
    file_info = bot.get_file(file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image", 'wb') as new_file:
        new_file.write(downloaded_file)
    photo = open('image', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    remove('image')
    
bot.polling(non_stop=True)