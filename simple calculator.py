 def sum(m, n):
    return f"the sum of the numbers is {m+n}"


def sub(m, n):
    return f"the subtraction of the numbers is {m-n}"


def multi(m, n):
    return f"the multiplication of the numbers is {m*n}"


def div(m, n):
    return f"the division of the numbers is {m/n}"


def expo(m, n):
    return f"the power of the numbers is {m**n}"


def fact(m):
    if m == 0:
        return 1
    else:
        return m * fact(m - 1)


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
opp = input("Choose the operator(+,-,*,/,**,!):")

if opp == "+":
    print(sum(num1, num2))
elif opp == "-":
    print(sub(num1, num2))
elif opp == "*":
    print(multi(num1, num2))
elif opp == "/":
    print(div(num1, num2))
elif opp == "**":
    print(expo(num1, num2))
elif opp == "!":
    print(
        f"the factorial of fist number is {fact(num1)}\nthe factorial of second number is {fact(num2)}"
    )
else:
    print("please choose the correct opperator")
																	
