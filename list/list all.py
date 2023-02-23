import random

#////
#def total(list):
#    sum=1
#    for i in list:
#        sum*=i
#    return sum

#print(total([1,5,6,7,8]))

#/////
#def max(list):
#    max_number=list[0]
#    for i in list:
#        if i>max_number:
#            max_number=i
#    return max_number
#print(max([1,5,67,4]))

#////
#list_old=[4,5,6,1,23,4,4,5]
#list_new=[]
#multiple=set(list_old) #множество 

#for i in list_old:
    #if i not in multiple:
    #    multiple.add(i)
    #    list_new.append(i)
#print(multiple)   can also be written as multiple=set(list_old) already sorted 
#print(list_new)
  
#comb 
#bra=[4,6,7,7,8,8,9]
#mul=list(set(bra))
#print (mul)


#/////
#matrix
matrix=[[4,4,3],[6,7,4],[8,4,3]]
#def output_matrix(matrix):
#    for i in range(len(matrix)):
#        for g in range(len(matrix[i])):
#            print("{:10d}".format(matrix[i][g]), end="")
#        print()
#output_matrix(matrix)

#def output_matrix(matrix):             #same/ but different way
#    for i in matrix:
#        for g in i:
#            print("{:4d}".format(g), end="")
#        print()
#output_matrix(matrix)

#cool
#m,n=3,4
#massive=[[random.randint(1,10) for g in range(n)] for i in range(m)]
#print(massive)
#def output_matrix(massive):             #same/ but different way
#    multiple=1
#    for g in range(m):
#        for i in range(n):
#            print("{:4d}".format(massive[g][i]), end="")
#            multiple*=massive[g][i]
#        print(" ", multiple)   
#        print()
#output_matrix(massive)

#task

#list=[4]
#if not list:
#    print("nothing")

#list_1=[1,3,5,6]
#number=""
#for i in list_1:
#    number+=str(i)
#print(number)
#number=int(number)
#print(number+10)

list_old=[3,9,5,6,7]
list_new=list(set(list_old))
print(list_new[-2])

#carthege
