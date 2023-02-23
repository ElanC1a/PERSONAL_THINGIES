numeral_min, numeral_max=int(input("Write your max and min: ")),int(input())

for i in range(numeral_min, numeral_max+1): #third numeral is the a.k.a steps/ by how much it is added
    if i>1:
        for t in range (2, i):          #get back to it 
            if (i%t)==0:
                break
        else:
            print(i)
