import random
options=["rock","paper","scissors"]
user=input("enter (rock or paper or scissors):")
python=random.choice(options)

print(f"user choice:{user}")
print(f"python choice:{python}")

if user==python:
    print("game is tie")
    
elif (user=="rock" and python=="paper"):
    print("python is win")
elif (user=="rock" and python=="scissors"):
    print("user is winner")
elif(user=="paper" and python=="rock"):
    print("user is winner")
elif(user=="scissors" and python=="rock"):
    print("python is winner")
    
elif(user=="paper" and python=="scissors"):
    print("python is winner")
    
elif(user=="scissors" and python=="paper"):
    print("user is winner") 
    
elif user!=["rock","paper","scissors"]:
    print("please check input")             