
'''
# example one with Counter module Collections
count = 0
#from collections import OrderedDict
from collections import Counter
countray = input()
lst = []
for letter in range(0,int(countray)):
    name = input()
    lst.append(name)
    print(lst)

result = [[x,lst.count(x)] for x in set(lst)]
print(result)

5
sara
sara
ali
hamid
mostefa
[['sara', 2], ['ali', 1], ['mostefa', 1], ['hamid', 1]]

'''


# example two this program use count founction
count = 0
from collections import Counter
countray = input()
lst = []
for letter in range(0,int(countray)):
    name = input()
    lst.append(name)
    count+= 1

if letter:
    re = lst.count(name)
    count+= 1
    print(name,re)



'''

from collections import OrderedDict
n=int(input())
vote={}
vote1=OrderedDict({})

for i in range(n):
	s=input()	
	if s in list(vote.keys()):
		vote[s]+=1
	else:
		vote[s]=1

z=list(vote.keys())
z.sort()
for i in z:
	print(i,vote[i])

'''

