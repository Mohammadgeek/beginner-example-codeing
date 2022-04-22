'''
6
9
14
(6, 9, 14)
<class 'tuple'>
the min value is 3
the min two value is  5
8

#frist code

data_list = [ int(x) for x in input().split() ]
print(data_list)
data_list.sort()
c=max(data_list)
v=min(data_list)
n= c-v

print(n)

# example two code

result = [ int(x) for x in input().split() ]

if result:
    c= max(result)
    x = min(result)
    z = c - x
    print(z)


'''

'''
#result = int(num) , int(num2) , int(num3)
#result = [ int(x) for x in input().split() ]
#result2= [int(y) for x in input().split()]
num = int(input())
num2 = int(input())
num3 = int(input())
result = int(num) , int(num2) , int(num3)
print(result)
#print(type(result))

if result:
    min_num = num2 - num
    print(f'the min value is {min_num}')
    min_num2 = num3 - num2
    print(f'the min two value is  {min_num2}')
    sum_num = min_num + min_num2
    print(int(sum_num))
'''
# use function for this example
result = [ int(x) for x in input().split() ]
def mesafet():
        max_value = max(result)
        min_value = min(result)
        sum_value = max_value - min_value
        return sum_value


#print(mesafet(4,8,14))




