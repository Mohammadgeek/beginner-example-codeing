
count = 0
inpt = input()
result = count
for words in inpt:
    print('the char string is :',words,'the input user is :',result)
    result+= 1
    print(result)


TF = result>=0 and result>1 and result>2 and result>3 and result>4
print(TF)
if TF:
    print('yes is done!')
else:
    print('error not convert input name')










