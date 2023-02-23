#shell sorting easy

def shell_array(array,total_lenght_array):
    interval=total_lenght_array//2
    while interval>0:
        for i in range(interval,total_lenght_array):
            t=array[i]
            j=i
            while j>=interval and array[j-interval]>t:
                array[j]=array[j-interval]
                j-=interval
            array[j]=t
        interval=interval//2

array=[5,45,13,99,6,3,2,0]
array_lght=len(array)
print(array)
shell_array(array,array_lght)
print(array)