
'''
inp = int(input()) # input user for count fibonachi sequence
one = 0 #start zero fibonachi sequence
second = 1
count = 0
lst = []
if inp <= 0:
    print('error')
elif inp == 1:
    print('okey')
    #print(x)
else:
    print("This Fibonacci sequence has {} elements".format(inp), ":")
    while count < inp:
        print(one, end=', ')
        fib = one + second # sum two value
        one = second
        second = z
        count += 1
'''
#daynamic fibo
count = 0
def fibo(num):
    if num < 2:
        return num
    first = 0
    second = 1
    for i in range(0,num+1):
        total = first + second
        first = second
        second = total
        print(total)

print(fibo(9))






