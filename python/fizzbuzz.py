#fizzbuzz project
from collections import Counter

def fizzbuzz(n):
    if n % 15 == 0 and n % 3 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)

print("\n".join(fizzbuzz(n) for n in range(1, 50)))


# use conditon
count = 0
lst = []
count_inp = 8
for i in range(0,int(count_inp)):
    y = int(input())
    if y %3 == 0:
       # print('fizz')
        continue
    elif y %5 == 0:
        print('buzz')
        continue
    elif y %3 == 0 and y %5 == 0:
        print('fizzbuzz')
        continue
    else:
        print('not_divisable')
        print('happy enjoy it!')



