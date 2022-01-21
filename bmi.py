
'''
#bmi formule :  weight / (height/100)**2
#Ponderal Index : weight / (height/100) **3
# PI_child = weight [g]/ height [cm]³ = 0.1 * PI_adult
    #ponderal index parameter
    underweight index body when 0 to 11
    normalwight index ponderal between 11 to 15
    overweight body index when 15 to 24
    obese body index when incrace 15

'''
import tkinter as tk
'''
#bmi example
def bmi_cal(weight,height):
    bmi = weight / (height/100) **2 # si unit
    ponderal = weight / (height/100) **3 # si unit
    print("body mass index equall is {:.2f}".format(bmi))
    print("ponderal index equall is {:.4f}".format(ponderal))

    #bmi = weight/(height**2)
    if (bmi <= 18.5 and bmi == 18):
        print('Underwight body mass')
    if (bmi >= 18.5 and bmi <= 24.9):
        print("normal body mass.")
    elif ( bmi >= 25 and bmi < 30):
        print("overwight body mass")
    else:
        print("you need visit doctor! you are obesity ")

#print(bmi_cal(65,185))
'''
def ponderal(age,weight,height):
    x = str(input('if you are is adult enter a , or is chid enter ch \n'))
    if x == 'a':
        pi_adult = weight / (height/100) **3
        if (pi_adult > 0 and pi_adult < 11):
             print("%.3f" % pi_adult)
             #9.481277764278
             print('ponderal index is : underweight')
             print('well done!')
        elif (pi_adult >= 11 and pi_adult <= 15):
             print("%.3f" % pi_adult)
             print('normalwight index ponderal')
             print('well done')
        elif (pi_adult >= 15 and pi_adult <= 24):
             print("%.3f" % pi_adult)
             print('overweight body ponderal')
             print('well done!')
        else:
              print('obese body ponderal')
    if x == 'ch':
        pi_child =  weight / (height/100) **3
        if pi_child <= 3.5:
            print(pi_child)
            print('dear perants,your baby is normal pi index')
        else:
            print('error')

print(ponderal('a',3,50))

#body fat










'''
#weight = int(input('please enter your weight : \n'))
#height = float(input('please enter your height: \n'))
for i in range(1):

    #print(f'the bmi equall is :{bmi}')
    #print("{:.2f}".format(bmi))
    #print "%.2f" % (bmi)
    print(f'{bmi:.2f}')
    if bmi <= 18.4:
        print("You are underweight.")
    elif bmi <= 24.9:
        print("You are healthy.")
    elif bmi <= 29.9:
        print("You are over weight.")
    elif bmi <= 34.9:
        print("You are severely over weight.")
    elif bmi <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")
'''


