# Enter 2 lists of integers. Check whether list sums to same value

l1= [int(n) for n in input("Enter values in list 1: ").split()]
l2= [int(n) for n in input("Enter values in list 2: ").split()]
s1=sum(l1)
s2=sum(l2)
print("Sum of list1:",s1)
print("Sum of list2:",s2)
if(s1==s2):
 print("The sum of list1 & list2 are same value:",s1)
else:
 print("The sum are not equal")
