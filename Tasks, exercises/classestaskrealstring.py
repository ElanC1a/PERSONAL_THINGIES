class RealString:
    def __init__(self,first_word,second_word):
        self.first_word=str(first_word)
        self.second_word=str(second_word)
    def by_amount(self):
        word_1=len(self.first_word)
        word_2=len(self.second_word)
        print("First word:", word_1)
        print("Second word:" ,word_2)
        if word_1>word_2:
            print(self.first_word,"is bigger")
        else:
            print(self.second_word,"is bigger")
    def by_index(self):
        list_1=list(self.first_word)
        list_2=list(self.second_word)
        amount_1=0
        amount_2=0
        for i in list_1:
            x=ord(i)
            amount_1+=x
        for j in list_2:
            y=ord(j)
            amount_2+=y
        if amount_1>amount_2:
            print(self.first_word,"has a bigger index")
        elif amount_1<amount_2:
            print(self.second_word,"has a bigger index")

string=RealString("Hello","Bonjour")
string.by_amount()
string.by_index()


