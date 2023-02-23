class Factory(object):
    name="Ford"                     #статическое поле
    def __init__(self, view, color, age):       #абстракция / динамическое поле
        self.view=view
        self.color=color
        self.age=age
    def __drive(self):
        print("BIP-BIP")
        
factory=Factory("bright","red",17)
factory.color="blue"

#Factory.name="Ferrari"
#print(Factory.name)
#factory._Factory__drive()


class Rectangle(object):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return (self.height*self.width)

def general_width():
    width_enter=int(input("width: "))
    return (width_enter)
def general_height():
    height_enter=int(input("height: "))
    return(height_enter)
    
rectangle_1=Rectangle(general_width(),general_height())
print("Your area: %s" %rectangle_1.area())  

rectangle_2=Rectangle(general_width(),general_height())
print("Your area: %s" %rectangle_2.area()) 

rectangle_3=rectangle_1

test_1=rectangle_1==rectangle_2
test_2=rectangle_1==rectangle_3

print(test_1)
print(test_2)



