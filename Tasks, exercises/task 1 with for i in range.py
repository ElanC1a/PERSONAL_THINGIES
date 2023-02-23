def model_5(lst): #lst, whatever - передавать параметры
    new_list=[]
    for number in lst:
        if abs(number)>5: #abs - вычiсление по модули 
            new_list.append(number)
    return new_list
print(model_5([6,76,-21,-4, 100]))

