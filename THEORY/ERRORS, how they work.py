try: 
    number_1, number_2=int(input("Write your 1 and 2 numbers: ")),int(input())
    division=number_1/number_2
    print(division)
except ZeroDivisionError:
    print("No possible divide by zero")
except ValueError:
    print("Wrong value")
else: #only if there were no errors
    print("Everything went well")
finally: #executed anytime no matter the error
    print("Well this is the end, bye!")
