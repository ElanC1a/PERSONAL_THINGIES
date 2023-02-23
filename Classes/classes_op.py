class Person(object):
    def metric(self):
        self.age=13
        self.weight=100
        self.height=70

jojo=Person()

class Elf(object):
    def __init__(self):
        self.attack=5
        self.hp=40
        self.attack_speed=4

elf=Elf() #экземпляр класса 
elf.hp+=5
elf.attack+=10

#print(elf.hp, elf.attack, elf.attack_speed)

class Animal(object):
    def __init__(self):
        self.age=10

class Dog(Animal):
    def dog_stats (self):
        print("woof-woof")

dog=Dog()

dog.dog_stats()

