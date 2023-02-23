x=0
k=1
a=10
#while x<66 and a<90:
#    a+=1
#    x+=1    
#    print (x,a)

i=0

#while i<40:
#    i+=1
#    if i==30:
#        continue
#    print(i)
#else:
#    print("cycle ended")


#task

enter=input("Write your nickname: ")
nickname=["Gr", "Tr", "Hu"]
        
while enter not in nickname:
    print ("Invalid, retry again ")
    enter=input()
else:
    print("Access granted, dear %s" %enter)
