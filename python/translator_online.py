# transalte online english from persian
#example two

tedad_kalamat = int(input())
d = {}
for radif in range (0, tedad_kalamat):
    word = input()
    english = word.split(' ')
    d[english[0]] = english[1] # english word equall perisan word

jomle = input() # input paragraph for genertute transalte
jomle = jomle.split(' ')
jomle_jadid = ''
result = ''

for english in jomle:
   jomle_jadid = d.get(english, english)
   result+= jomle_jadid + ' '

print(result)



