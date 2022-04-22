# price range pc and laptap for contract website , i hope enqualityoy it
'''
pc_count = [int(x) for x in input()]
print(pc_count)
price = [int(x) for x in input()]
quality = [int(y) for y in input()]

while pc_count True:
    if price_one < and price_two and quality_one > and quality_two:
        print('happy find laptap')
    if price > and quality:
        print('not find')
    else:
        print('')
  '''
#problem code
#compare more 2 number input
'''
price=[]
quality=[]
count= 0
pc_count =input()
for i in range(0,int(pc_count)):
    y= input()

print(type(y))
 i = price.append(y[:2])
print(price)
k = quality.append(y[:2])
print(quality)

for one in range(0,len(price)):
 for two in range(0,len(price)):
     if int(price[one])<int(price[two]) and int(quality[one])>int(quality[two]): # true / true
         print('happy irsa')
      # true / true
         count+= 1
         print('poor irsa')
'''


laptop_buy = int(input())
pc_lst = []
for rate in range(0,int(laptop_buy)):
    y = input()
    result = y.split(' ')
    print(result)
    pc_lst.append((int(result[0]), int(result[1])))

#print(laptop_buy)
#print(tuple(pc_lst))
#print(type(pc_lst))
#[(1, 5), (4, 2), (3, 6), (5, 5)]

found = False
for price in range(len(pc_lst)):
    for quality in range(len(pc_lst)):
        if pc_lst[price][0] < pc_lst[quality][0] and (pc_lst[price][1]) > (pc_lst[quality][1]):
            found = True
            if pc_lst[quality][0] > pc_lst[price][0] and (pc_lst[price][1] < pc_lst[quality][1]):
                found = True
            if found:
                break


if found:
    print('happy irsa')
else:
    print('poor irsa')


'''
2
1 5
4 2
2
<class 'list'>
poor irsa

2
5 6
20 30
#pooor











'''

'''
def prices_pricersa(laptop):
    for i in range(len(laptop)):
        for quality in range(len(laptop)):
            if ((laptop[i][0] < laptop[quality][0] and (laptop[i][1] > laptop[quality][1])) or (laptop[i][0] > laptop[quality][0]) and (laptop[i][1] and laptop[quality][i])):
                return True
            return False

count = int(input())
laptop = []
for i in range(count):
    result = input()
    output = result
    laptop.append((int(output[0], int(output[1]))))

print(type(output)) # ValueError: invalid literal for int() with base 3: '4'

if(is_irsa(laptop)):
    print('happy irsa')
else:
    print('poor irsa')

'''





