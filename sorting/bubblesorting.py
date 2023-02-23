import random
#bubble sorting/ sinking sort/ Пузырьковая сортировка
list=[]
n=10
for i in range(n):
    list.append(random.randint(0,100))
print(list)

def bubble(total):
    for i in range(n-1):
        for g in range(n-i-1):
            if total[g]>total[g+1]:
                total[g],total[g+1]=total[g+1],total[g]
    return(total)
bubble(list)
print(list)

