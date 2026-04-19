import math
a=float(input("Enter number:"))
b=float(input("Enter a number:"))
c=abs(a-b)
print(c)
if c<0.001:
   print("close")
else:
   print("Not close")
