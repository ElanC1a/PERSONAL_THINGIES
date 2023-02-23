#set_kg() and get_kg() method #1
class KgToPounds:
    def __init__(self,kg):
        self.__kg=kg
    def get_kg(self):
        return self.__kg
    def set_kg(self, kg):
        self.__kg=kg
    def to_pounds(self):
        pound=self.__kg*2.205
        print("In pounds:",pound) #why with comma prog is ok with int?/ put + or %s-->won't work 0_0? not all arguments converted during string formatting->sol. pound=str(pound)       

kg=KgToPounds(6)
kg.set_kg(7)
print("Your kg: ", kg.get_kg())
kg.to_pounds()

#@property and @kg.setter method #2
class KgToPounds:
    def __init__(self,kg):
        self.__kg=kg
    @property
    def kg(self):
        return self.__kg
    @kg.setter
    def kg(self,kg):
        self.__kg=kg
    def to_pounds(self):
        pound=self.__kg*2.205
        print("In pounds:",pound)

kg=KgToPounds(5)
kg.kg=6
kg.to_pounds()

#property() method #3
class KgToPounds:
    def __init__(self,kg):
        self.__kg=kg
    def get_kg(self):
        return self.__kg
    def set_kg(self, kg):
        self.__kg=kg
    # def del_kg(self): можно еще так
    #     del self.__kg
    def to_pounds(self):
        pound=self.__kg*2.205
        print("In pounds:",pound)
    weight=property(get_kg,set_kg)

kg=KgToPounds(0)
kg.weight=5
kg.to_pounds()