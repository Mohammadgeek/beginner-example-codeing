#age_kandiad = []
'''
while True:
    age = int(input())
    result = age
    #age_kandiad.append(age)
    if result > 10 and result < 90:
        continue
    if result >= 90:
        break
    elif result == -1:
        print(max(result)) #TypeError: 'int' object is not iterable
        break
'''
'''
age_kandiad = []
while True:
    age = int(input())
    age_kandiad.append(age)
    if age > 10 and age < 90:
        #continue
        print(age_kandiad)
    if age >= 90:
        break
    elif age == -1:
        print(max(age_kandiad))
        break

'''
while True:
    age = int(input())
    age_kandiad = age
    if age > 10 and age < 90:
        print(age_kandiad)
    else:
        break
    if age == -1:
        print(max(age))
        break




