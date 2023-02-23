from string import ascii_letters
import numpy

#новый_список = [«операция» for «элемент списка» in «список»]
price=[355,500,6000,540,420,1337,55555,88005553535,337]
sale=0.8
final_price=[round((i*sale),2) for i in price]
#print(final_price)

#новый_список = [«операция» for «элемент списка» in «список» if «условие»]
initial=[5,11,111,0,23,44,51,11111]
answer=[i for i in initial if i%11==0]
#print(answer)

#списковое включ
#новый_список = [«операция» if «условие» for «элемент списка» in «список»]
text='hghtgbgugngjgjаррввраргкимгпипгшÖööääöäöäüüü'
english_letters=[f'{i} DA' if i in ascii_letters else f'{i} NET' for i in text]
#print(english_letters)

#разделение
p=['bo','ho','ham']
single_letter=[j for i in p for j in i]
#print(single_letter)

#multiplication table
table_ofmultiplication=[[i*j for i in range(1,6)] for j in range(1,6)]
new=numpy.array(table_ofmultiplication)
#print(new)

old_list=[2, 77, 12, 3, 0, 112, 4, -987]
new_list=[(i*2) if i<5 else (i-2) for i in old_list]
#print(new_list)

citi=['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
consonant=['бвгджзйклмнпрстфхцчшщ']
new_spisk=[j.upper() for i in (m.lower() for m in citi) for j in i if j in (k for l in consonant for k in l)]
print(new_spisk)

# citi=['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
# citi_lower=[m.lower() for m in citi]
# consonant=['бвгджзйклмнпрстфхцчшщ']

# consonant_list=[k for l in consonant for k in l]
# new_spisk=[j.upper() for i in citi() for j in i if j in consonant_list]
# print(new_spisk)