x=int(input("Write the sequence: "))

sequence_1,sequence_2=1,3

counter=0

if x<0:
    print ("Write a positive number")
elif x==1:
    print(sequence_1)
else:
    while counter<x:
        print(sequence_1)
        combo=sequence_1+sequence_2
        sequence_1=sequence_2
        sequence_2=combo
        counter+=1
    print ("End")
        
