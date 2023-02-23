import pyjokes
list_of_jokes = pyjokes.get_jokes(language="en", category="twister")
  
# traversing through the generated list of jokes
# Range of i may change, depending on the number of jokes
# you want to display
for i in range(0, 4):
    print(list_of_jokes[i], sep='\n')