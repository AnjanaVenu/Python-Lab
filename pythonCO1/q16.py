# Create a single string separated with space from two strings by swapping the character at position 1.

s1=input("Enter string1:")
s2=input("Enter string2:")
s3=s2[0]+s1[1:]+" "+s1[0]+s2[1:]
print("Modified string:",s3)
