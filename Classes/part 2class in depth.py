class Person:
    def __init__(self,name):     #конструктор
        self.__name=name        #__->private
        self.__age=10
        #self.rnd=5
    @property
    def age(self):      #get_age
        return self.__age 
    @property
    def name(self):     #get_name
        return self.__name
    @age.setter
    def age(self,age):      #set_age
        if 105>age>1:
            self.__age=age
        else:
            print("error")
    def output_text(self,message):  #метод класса
        print("Send your message: ")
        print(message)

class Life_expectancy:
    def __init__(self,time):
        self.time=time
    def test(self):
        print("TEST")

class Work (Life_expectancy,Person):
    def __init__(self,name,time):
        Person.__init__(self,name)
        Life_expectancy.__init__(self,time)
    def text(self):
        print(self.name, "works")

# @property
#person=Person("huh") #объект класса/ конструктор 
#person.age=50
#print(person.age)

# without @property 
# person.set_age(6)
# print(person.get_age())

# print(person.name, person.age)
# person.output_text(input())

# person.catch="Popov"
# print(person.catch)

work=Work("hu",60)
print(work.mro())
