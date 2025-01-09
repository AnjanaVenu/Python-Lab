# Find biggest of 3 numbers entered

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
 print("a is greater than b and c")
elif b>a and b>c:
 print("b is greater than a and c")
else:
 print("c is greater than a and b")
