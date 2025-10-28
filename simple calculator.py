while True:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.power")
	
    operator=input("choose the operator:")

    if operator=="1":
    	print(f"addition of this two numbers is {num1+num2}")
	
    elif operator=="2":
    	print(f"subtraction of this two numbers is {num1-num2}")
	
    elif operator=="3":
    			print(f"multiplication of this two numbers is {num1*num2}")
			
    elif operator=="4":
		    	print(f"division of this two numbers is {num1/num2}")
			
    elif operator=="5":
    	print(f"power of this two numbers is {num1**num2}")
	
    else:
    	print("invalid operator")	
	
							
													
																			
																									
    print("[Thank you for using this calculator]")																	