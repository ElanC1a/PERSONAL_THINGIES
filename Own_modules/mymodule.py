from cmath import pi


name="max"

def max_number(a,b,c):
    if a>b and a>c:
        print(a," maximum")
    elif b>a and b>c:
        print(b," maximum")
    else:
        print(c," maximum")

def trapeze(base_top, base_bottom, height):
    return(((base_top+base_bottom)/2)*height)
def triangle(height, base):
    return((base*height)/2)
def circle(radius):
    return(pi*radius**2)