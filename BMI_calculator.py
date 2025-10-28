print("BODY MASS INDEX(BMI):")
print("~~~~~~~~~~~~~~~~~~~~~~")
print("                     ")

weight=int(input("ENTER YOUR WEIGHT(in kg):"))
height=int(input("ENTER YOUR HEIGHT(in cm):"))

BMI=(weight*10000/(height**2))

if BMI<18.5:
    print(f"your BMI={BMI}")
    print("you are in under weight")
    
elif BMI>=18.5 and BMI<=24.9:
    print(f"your BMI={BMI}")
    print("normal")
    
elif BMI>24.9 and BMI<=29.9:
    print(f"your BMI={BMI}")
    print("you are in overweight")
    
elif BMI>30:
    print(f"your BMI={BMI}")
    print("obesity")

else:
    print("please Enter valid details")
