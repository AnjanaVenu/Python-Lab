# Enter 2 lists of integers. Check whether any value occur in both

l1=list(input("Enter values in list 1: ").split())
l2=list(input("Enter values in list 2: ").split())
value=set(l1)&set(l2)
if value:
 print("Common values between the lists:",value)
else: 
 print("No common values")
