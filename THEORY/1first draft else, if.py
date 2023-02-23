num_1=float(input("Write your first number: "))
num_2=float(input("Write your second number: "))

result=input("Write arm: ")

if result=="+":
    prim=num_1+num_2
    print(f"Your result: {prim}")
    
    
elif result=="-":
    prim=num_1-num_2
    print("Your result: " + str(prim))
    
elif result=="*":
    prim=num_1*num_2
    print("Your result: " + str(prim))
elif result=="/":
    prim=num_1/num_2
    print("Your result: " + str(prim))
else:
    print("error")
