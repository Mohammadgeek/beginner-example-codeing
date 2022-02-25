'''
win = 0
equall = 0
loss = 0
total = 0

match_count = 30
for i in range(0,int(match_count)):
    y = int(input())
    total+= y
    if y != 0 and y != 3 and y != 1:
        print('your can not enter this number!!')
        break
        # number y not show result
    if y == 3:
        win+= 1
    if y == 0:
        loss+= 1
    if y == 1:
        equall+= 1


print(total,equall)
print(f'the club win point is : {win}')
print(f'the loss club in session : {loss}')
'''

def match_count(club):
    win = 0
    equall = 0
    loss = 0
    total = 0
    win_lst = []
    equall_lst = []
    total_lst = []
    with open(path,'r') as file:
        reader = file.read()
        g = [ int(x) for x in reader.split() ]
        print(type(g))
        for i in range(len(g)):
            print(g)
            break
        for i in g[0:]:
            win = list(filter(lambda x:x == 3 ,g))
            equall = list(filter(lambda x:x == 1,g))
            victory = win.copy()
            eq = equall.copy()
            print(victory)
            print(eq)
            result = sum(victory)
            result_b = sum(eq)
            total = result + result_b
            print(f'the all point team is {total} , the sum equall game is :{result_b}')
            break
    
path = "address your patch"
print(match_count(path))
