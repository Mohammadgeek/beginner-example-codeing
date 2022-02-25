
lst = []
num = 0
inp = input('please enter number for start program : \n')
for i in range(0,int(inp)):
    get_num = str(input())
    y = list(map(lambda c2: c2, get_num))
    count = len(get_num)
    if count <= 99:
        out = str(count) + ':' + str(count) * count
        print(f'this length input number equall  : {out}')
    #select one charcter to reapt length
    if count <= 99:
        for i in y[0:]:
            num+= 0
            result = i + ':' + int(i) * i
            print(result)
    else:
        print('error runtime programs')
        break


