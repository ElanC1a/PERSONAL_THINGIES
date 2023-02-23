def reverse(word):
    if len(word)==0:
        return word
    else:
        return reverse(word[1:])+word[0]

word=str(input()) #dog->god
z=reverse(word)
print(z)


