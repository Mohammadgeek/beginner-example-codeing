#adverb remover
count = int(input('please enter count for convert adverb : \n'))
lst = []
for harf in range(0,int(count)):
    name = str(input())
    if name[-2:] == 'ly':
        print(f'the adverb list is : {name}')
        lst.append(name)
        newlist = [name.replace('ly',"")for name in lst]
        print(name)
    else: # if user enter adv or noun
        print(name)
        print(newlist)
        break
        
        
        



#lst.append(user)
#print(lst)

