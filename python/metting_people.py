'''
example code 
6
9
14
(6, 9, 14)
<class 'tuple'>
the min value is 3
the min two value is  5
8
'''
# use function for this example
result = [ int(x) for x in input().split() ]
def mesafet():
        max_value = max(result)
        min_value = min(result)
        sum_value = max_value - min_value
        return sum_value





