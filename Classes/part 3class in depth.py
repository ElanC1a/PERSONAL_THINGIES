class Person:
    def __init__(self,name):     #конструктор
        self.__name=name        #__->private
        self.__age=10
        self.rnd=5
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

class Life_expectancy:
    def __init__(self,time):
        self.time=time
    
class Work (Life_expectancy,Person):
    def __init__(self,name,time):
        Person.__init__(self,name)
        Life_expectancy.__init__(self,time)
    