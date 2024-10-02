weight=float(input("enter weights in kgs:"))
h=float(input("enter height in feets:"))
height=h*0.305
def BMI(weight,height):
    bmi=weight/ (height**2)
    if bmi<18.5:
        return "under weight",bmi
    elif bmi<25:
        return "normal",bmi
    elif bmi>=25 and bmi<30:
       return "overweight",bmi
    else:
        return "obesity",bmi
a=BMI(weight,height)
print(a)
