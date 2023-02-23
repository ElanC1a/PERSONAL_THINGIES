import random
# Selection sort in Python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:           # to sort in descending order, change > to < in this line
                min_idx = i                         # select the minimum element in each loop
         
        # put min at the correct position
        array[step], array[min_idx]=array[min_idx], array[step]


lisst = []
n=10
for i in range(n):
    lisst.append(random.randint(0,100))
size = len(lisst)
print(lisst)

selectionSort(lisst, size)
print('Sorted Array in Ascending Order:')
print(lisst)