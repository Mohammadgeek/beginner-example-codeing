import csv
from collections import OrderedDict
from statistics import mean
from operator import itemgetter

def calculate_averages(input_file_name,output_file_name):

   d = dict()
   with open(path,newline = '',encoding = 'utf-8') as file:
    reader = csv.reader(file)
    for person in reader:
        name = person[0]
        grade = list()

        for avarge in  person[1:]:
            grade.append(int(avarge)) # point every student append list 
        d[name] = mean(grade)  
    for user in d.items():
        print(user[0],user[1])
    

path = 'please enter your patch'
out = 'V:/testing/result.csv'
result = calculate_averages
print(result(path,out))



#loop outside control programmer

def calculate_sorted_averages(input_file_name,output_file_name):
    d = dict()
    with open(path,newline = '',encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for person in reader:
           name = person[0]
           grade = list()
           for avarge in  person[1:]:
               grade.append(int(avarge))
           d[name] = mean(grade)

    a = sorted(d.items(), key=lambda x: x[1])
    for user in a:
        print(user[0],user[1])


path = "please enter your patch"
out = 'V:/testing/result.csv'
print(calculate_sorted_averages(path,out))



def calculate_three_best(input_file_name, output_file_name):
    averages = {}
    with open(path) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = sum(scores) / len(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict(sorted (averages.items(), key=lambda x:(x[1], x[0])))
    with open (output_file_name, 'w') as out:
        worst = []
        for i in range (3):
            worst_avg = averages_ord.popitem (last=True)
            worst.append (worst_avg)
            print(worst_avg[0],worst_avg[1])


path = 'please enter your patch'
out = 'V:/testing/result.csv'
print(calculate_three_best(path,out))



def calculate_three_worst(input_file_name, output_file_name):
    averages = {}
    with open(path) as csv_file:
        csvfile = csv.reader(csv_file)
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = sum(scores) / len(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict(sorted (averages.items(), key=lambda x:(x[1], x[0])))
    with open (output_file_name, 'w') as out:
        worst = []
        for i in range (3):
            worst_avg = averages_ord.popitem (last=False)
            worst.append (worst_avg)
            print(worst_avg[1])
            #for name,avg in enumerate(worst_avg):
                #print(name,":",avg)


path = 'please enter your patch'
out = 'V:/testing/result.csv'
print(calculate_three_worst(path,out))



def calculate_average_of_averages(input_file_name,output_file_name):
    d = dict()
    with open(path,newline = '',encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for person in reader:
            name = person[0]
            grade = list()
            for avg in person[1:]:
                grade.append(int(avg))
                cul = sum(grade) / len(grade)
                d[name] = cul
            #d[name] = mean(grade)
        lst = list(d.values())
        print(mean(lst))

path = 'please enter your patch'
out = 'V:/testing/result.csv'
print(calculate_average_of_averages(path,out))
