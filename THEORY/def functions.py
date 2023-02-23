# name_input=input("Please enter your name: ")

# def name(argument): #def x() - in () it is a varible
#    print("Welcome: %s" %argument)

# name(name_input)
#-----------------------------------------

#calculator programme

def calculator(first_number, second_number, operator):
    if operator=="+":
        print(first_number+second_number)
    elif operator=="-":
        print(first_number-second_number)
    elif operator=="/":
        print(first_number/second_number)       #change the prog with error
    elif operator=="*":
        print(first_number*second_number)
    else:
        print("error")
        
while True:
    first_number, second_number=int(input("Write your 1 and 2 number: ")), int(input())
    operator=(input("Choose your operator '+' , '-' , '/' , '*' or 'quit' "))
    if operator=="quit":
        print("Goodbye!")
        break
    else:
        calculator(first_number, second_number, operator)
