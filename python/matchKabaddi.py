# math Kabaddi iran for tournoment eroupa and time for watch people
'''
6
4 3 5 0 1 2
1

6
4 4 5 6 8 9
2
'''
n=int(input())
data_list = [ int(x) for x in input().split() ]
new_list=[] # use list
for i in data_list:
    if i >= 2:
        new_list.append(i)
        data_list = new_list

l=len(new_list)
j= (l//3) # limit team 3 player
print(j)

