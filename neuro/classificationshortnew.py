from numpy import exp, array, random, dot
#трен

input_training=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1],[0,1,0]])
answer_oftraining=array([[0,1,1,0,0]]).T

random.seed(1)  

weight=2*random.random((3,1))-1

for i in range(10000):
    sigmoid_output_number=1/(1+exp(-(dot(input_training,weight))))
    weight+=dot(input_training.T,(answer_oftraining-sigmoid_output_number)*(1-sigmoid_output_number)*sigmoid_output_number)

print(1/(1+exp(-(dot(array([1,0,0]),weight)))))