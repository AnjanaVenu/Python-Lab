# Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.

s=input("Enter a string:").lower()
s1=s[0]+s[1:-1].replace(s[0],'$')
print(s1)
