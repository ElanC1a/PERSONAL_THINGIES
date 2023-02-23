#method hoare

array=[5,6,7,3,62,66,12,4,123]
bread=len(array)-1
def division(array,first,last):
    point=array[((first+last)//2)+1]
    i=first-1 #aka the last element
    j=last+1 #aka the first element

    while True:
        i+=1
        while array[i]<point:
            i+=1
        j-=1
        while array[j]>point:
            j-=1
        if i>=j:
            return j
        array[i],array[j]=array[j],array[i]
def sorting(array):
    def _sorting(t,first,last):
        if first<last:
            sheep=division(array,first,last)
            _sorting(t,first,sheep)
            _sorting(t,sheep+1,last)
    _sorting(array,0,bread)
sorting(array)
print(array)