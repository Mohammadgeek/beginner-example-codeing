
import tkinter as tk

def bmi_cal(weight,height):
    bmi = weight / (height/100) **2 #bmi = weight/(height**2)
    print("body mass index equall is {:.2f}".format(bmi))
    print("ponderal index equall is {:.4f}".format(ponderal))

    
    if (bmi <= 18.5 and bmi == 18):
        print('Underwight body mass')
    if (bmi >= 18.5 and bmi <= 24.9):
        print("normal body mass.")
    elif ( bmi >= 25 and bmi < 30):
        print("overwight body mass")
    else:
        print("you need visit doctor! obsity two body index")

a = int(input('please enter your weight :\n'))
b = int(input('please enter your height:\n'))
print(bmi_cal(a,b))


#PI_adult = weight [kg]/ height [m]³ 
#PI_child = weight [g]/ height [cm]³ = 0.1 * PI_adult

def ponderal(age,wight,height):
    if age >= 4:
        print('calcualte ponderal adult ')
        pi_adult = wight / (height/100) **3
        if (pi_adult >= 11 and pi_adult <= 15):
             print("%.3f" % pi_adult)
             print('normalwight index ponderal')
             print('well done')
        elif (pi_adult >= 15 and pi_adult <= 24):
             print("%.3f" % pi_adult)
             print('overweight body ponderal')
             print('well done!')
        else:
              print('obese body ponderal')
    else:
        print('calcualte child ponderal')
        pi_child = (wight / 1000) / (height  / 100)
        pi_adult = wight / (height/100) **3
        result = 0.1 * pi_adult
        print("%3f" % result)
        if (result >= 2.2 and result <= 4.2):
            print('full health your newborn baby')
        else:
            print('your baby need visit doctor!!')
            #print("%.2f" % result)


age = int(input('please enter your age :?\n'))
wight = int(input('please enter your weight :\n'))
height = int(input('please enter your height:\n'))
print(ponderal(age,wight,height))






