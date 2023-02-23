import numpy as nu
"""
array_1=[1,0,1]#1->0
array_2=[1,0,1]
array_3=[0,1,0]#0->1
array_4=[0,1,0]
"""

def sigmoid(x,p=False):
    if p:
        return x*(1-x)
    return 1/(1+nu.exp(-x))

array=nu.array([[1,0,1],[1,0,1],[0,1,0],[0,1,0]])
#print(array)
output=nu.array([[0,0,1,1]]).T
#print(output)
nu.random.seed(1)

sin=2*nu.random.random((3,1)) #весы

test_array=[]

for i in range(100000):
    ss=array
    test_array=sigmoid(nu.dot(ss,sin))
    error=output-test_array
    delta=error*sigmoid(test_array,True)
    sin+=nu.dot(ss.T,delta)
print(test_array)

new_array=nu.array([1,1,1])
new_sigmoid=sigmoid(nu.dot(new_array,sin))
print("New test: ",new_sigmoid)