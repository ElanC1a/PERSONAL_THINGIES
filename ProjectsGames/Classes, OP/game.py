import re
from secrets import choice
from unicodedata import name
from venv import create
import time 
import random
import os

class Character(object):
    def __init__(self, name, hp, attack):
        self.name=name
        self.hp=hp
        self.attack=attack

class Player(Character):
    def __init__(self, name, hp, attack, exp, lvl):
        super().__init__(name, hp, attack) #super - regiving the element            #add random encounters/ bosses/ 
        self.exp=exp
        self.lvl=lvl

    def attack_player(self, victime):
        victime.hp-=self.attack
        if victime.hp<=0:
            print(victime.name, "is down")
            self.exp+=10
            print("Your exp:", self.exp)
            weapon_or_heal=[0,1]
            rnd_choice=weapon_or_heal[random.randint(0,len(weapon_or_heal)-1)]
            if rnd_choice==0:
                getting_weapon=weapon_func()
                print("new weapon :) %s %s" %(getting_weapon[0], getting_weapon[1]))
                time.sleep(1)
            elif rnd_choice==1:
                getting_heal=heal_func()
                print("drink up :0 %s" %(getting_heal))
                time.sleep(1)
            if self.exp==100:
                self.exp=0
                self.lvl+=1
                print("Lvl up, your lvl: ", self.lvl)
                self.attack+=3
                self.hp+=3
            victime.hp=100
            return False #?
        else:
            print(victime.name,  victime.hp, "damage done: ", self.attack)
            return True

class Enemy(Character):
    def __init__(self,name, hp, attack):
        super().__init__(name, hp, attack)
    
    def attack_enemy(self, victime):
        victime.hp-=self.attack
        if victime.hp<=0:
            print(victime.name, "game over")
            quit()
        else:
            print(victime.name,  victime.hp, "damage done:", self.attack)

def create_person(name, class_player, class_race):
    hp=0
    attack=0   
    if class_player==class_type_list[0]:
        hp+=45
        attack+=25
    elif class_player==class_type_list[1]:
        hp+=30
        attack+=20
    elif class_player==class_type_list[2]:
        hp+=25
        attack+=25
    else:
        print("ERROR")
        quit()

    if class_race==race_character[0]:
        hp-=5
        attack+=10
        return Player(name, hp, attack, 0, 0)
    elif class_race==race_character[1]:
        hp+=5
        attack-=10
        return Player(name, hp, attack, 0, 0)
    elif class_race==race_character[2]:
        hp+=20
        attack-=10
        return Player(name, hp, attack, 0, 0)

def create_monster():
    name=monster_list[random.randint(0,len(monster_list)-1)]
    hp=monster_hp[random.randint(0, len(monster_hp)-1)] + (player.lvl+3)
    attack=monster_attack[random.randint(0, len(monster_attack)-1)] + (player.lvl*1.5)
    return Enemy(name, hp, attack)

def decision():
    answer=input("Attack or flee:").lower()
    if answer=="attack":
        win_lose=player.attack_player(monster)
        if win_lose:
            time.sleep(1)
            monster.attack_enemy(player)
            decision()
    elif answer=="flee":
        print("you loser 😎")
        answer_1=random.randint(0,1)
        if answer_1==0:
            print("you sore loser, you did not escape")
            monster.attack_enemy(player)
            decision()
        elif answer_1==1:
            print("well done, you saved your ass...")
    else:
        print("error, %s" %("retry the input"))
        decision()

weapon=["diamond-sword", "bow", "revolver", "magical-wand"]
rarity={2:"legendary", 1.5:"rare", 1:"average"}

def weapon_func():
    rnd_wpn_type=weapon[random.randint(0,len(weapon)-1)] #?
    rnd_rare_type=choice(list(rarity.keys())) #random output in dictionary 
    if rnd_wpn_type==weapon[0]:
        player.attack+=7*rnd_rare_type
    elif rnd_wpn_type==weapon[1]:
        player.attack+=4*rnd_rare_type
    elif rnd_wpn_type==weapon[2]:
        player.attack+=6*rnd_rare_type
    elif rnd_wpn_type==weapon[3]:
        player.attack+=8*rnd_rare_type
    return rarity[rnd_rare_type], rnd_wpn_type

heal={5:"small potion", 10:"medium potion", 15:"large potion"}

def heal_func():
    rnd_heal_type=choice(list(heal.keys()))
    player.hp+=rnd_heal_type
    return heal[rnd_heal_type]


ppl=["witch", "bandit", "mage"]
def ppl_encounter():
    rnd_ppl_type=ppl[random.randint(0,len(ppl)-1)] #problem
    if rnd_ppl_type==ppl[0]:
        evil_good=[0,1]
        rnd_choice_evil_good=evil_good(random.randint(0,len(evil_good)-1))  #problem
        if rnd_choice_evil_good==0:
            print("you are lucky, you met a rightiuos witch")    
            player.hp+=4
            print("she gives you apple %s" %player.hp)
            time.sleep(1)
            return player.hp
        elif rnd_choice_evil_good==1:
            print("too bad, you met an evil witch")
            player.hp-=4
            print("she gives you rotten apple %s" %player.hp)
            time.sleep(1)
            return player.hp                                    
    elif rnd_ppl_type==ppl[1]:
        give_weapon=weapon_func()
        print("you've met a bandit, he gives you stole weapon %s" %give_weapon)
    elif rnd_ppl_type==ppl[2]:
        print("you've met a beautiful mage")
        print("she gives you magical buff 😏")   #make temporary buff!!!
        player.hp+=5
        print("Hp %s" %player.hp)
        player.attack+=5
        print("Attack %s" %player.attack)
        return player.hp, player.attack
        #add !!!

#####################
class_type_list=["swordsman", "archer", "alchemist"]
class_character_list=[] #name, type_list
race_character=["elf", "dwarf", "beast" ]

monster_list=["ghoul", "skeleton", "zombie", "creeper", "enderman"]
monster_hp=[30, 20, 40, 35, 15]
monster_attack=[10, 25, 20, 15, 30]

print("YOU'VE ENTERED THE DUNGEON OF DOOM!")
time.sleep(1)   
class_character_list.append(input("What is your name: "))

print("Choose your character: ", end=" ")
for i in class_type_list:
    print( i, end=" ")
    
class_character_list.append(input().lower())

print("Choose your race: ", end=" ")
for k in race_character:
    print( k, end=" ")

class_character_list.append(input().lower())

player=create_person(class_character_list[0], class_character_list[1], class_character_list[2])
##########################

while True:
    encounter=random.choice([0,1,2])
    if encounter==0: #no encounter
        print("there is nobody here...")
    elif encounter==1:  #encounter with a monster
        print("monster is infront of you 0_0")
        monster=create_monster()
        os.system("CLS")
        print("name: %s, health: %s, attack: %s, exp: %s, lvl: %s" %(player.name, player.hp, player.attack, player.exp, player.lvl))
        print("name: %s, health: %s, attack: %s" %(monster.name, monster.hp, monster.attack ))
        decision()
    elif encounter==2:
        print("there is a stranger in front ◉_◉")
        time.sleep(2)
        os.system("CLS")
        ppl=ppl_encounter()
        ppl
    time.sleep(2)

#lower - работа со строками/ все с мал. бук
#answer="ARBuZ"
#answer=answer.lower()
#print(answer)

#for i in range(100):
#    i+=1
#    player.attack_player(enemy)

#print(enemy.name, enemy.hp, enemy.attack, enemy.attack_speed, enemy.type)
#print(player.hp, player.name)