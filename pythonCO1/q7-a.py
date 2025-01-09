# Enter 2 lists of integers. Check Whether list are of same length

ls1=list(input("Enter values in list 1: ").split())
ls2=list(input("Enter values in list 2: ").split())
print("Length of list 1:",len(ls1))
print("Length of list 2:",len(ls2))
if(len(ls1)==len(ls2)):
 print("The list are same length of",len(ls1))
else:
 print("The list are not equal length")
