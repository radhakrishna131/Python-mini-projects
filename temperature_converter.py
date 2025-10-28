print("c=celsius")
print("k=kelvin")
print("f=fahrenheit")
print("")
a=float(input("temperature:"))
b=input("units:")
c="c"
k="k"
f="f"
t=(9/5)*a+32
m=a+273.15
n=a-273.15
s=((a-273.15)*(9/5))+32
y=((a-32)*(5/9))+273.15
x=(a-32)*(5/9)
if b==c:
	print(f"temperature in faranheit={t}")
	print(f"temperature in kelvin={m}")
		
elif b==k:
	print(f"temperature in celsius={n}")
	print(f"temperature in fahrenheit={s}")

elif b==f:
	print(f"temperature in celsius={x}")
	print(f"temperature in kelvin={y}")
else:
	print("please give correct units")
