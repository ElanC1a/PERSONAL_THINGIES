def hello(language):
    match language:
        case "English"|"english":
            print("Hello")
        case "Russian"|"russian":
            print("Привет")
        case "German"|"german":
            print("Hallo")
        case _:
            print("ERROR")
        
#hello(str(input()))

def calc(result,number_1,number_2):
    match result:
        case "+":
            return number_1+number_2
        case "-":
            return number_1-number_2
        case "*":
            return number_1*number_2
#x=calc(str(input()),int(input()),int(input()))
#print(x)


def massive(people):
    match people:
        case ["Joe","Brandli","Karim"]:
            print("from earth")
        case ["Joe",name,_]:
            print(name)
        case [rnd_1,rnd_2,rnd_3]:
            print(rnd_1,rnd_2,rnd_3)
        case [first,*other]:
            print(first,other)
massive(["JUnga","h","h","h","h","h"])