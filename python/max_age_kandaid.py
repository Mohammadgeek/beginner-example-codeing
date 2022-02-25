
age_kandiad = []
while True:
    age = int(input())
    result = age
    age_kandiad.append(age)
    if age > 10 and age < 90:
        print('well done!')
        continue

    if result != age:
       print('error,repeat number please try agine number')
    elif age == age_kandiad:
        break
    if age == -1:
        result = max(age_kandiad)
        age_kandiad.remove(result)
        second_max = max(age_kandiad)
        print(result , second_max)
        break













