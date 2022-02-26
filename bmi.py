weight = float(input("enter the weight(kg):"))
height = float(input("enter the height(m):"))
bmi =weight/height**2
if bmi <18.5:
    print("underweight")
elif bmi <24.9 and bmi >= 18.5:
    print ("normal")
elif bmi <29.9 and bmi >=25:
    print("overweight")
elif bmi <35 and bmi >=30:    
    print("obese")
elif bmi>=35:
    print("extremely obese ")            