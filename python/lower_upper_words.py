

name = str(input())
upper = []
lower = []


for count in name:
    if count.islower():
        lower.append(count)
    if count.isupper():
        upper.append(count)

if len(lower) > len(upper):
        print(name.lower)

if len(upper) > len(lower):
        print(name.upper())

else:
        print(name.lower())




