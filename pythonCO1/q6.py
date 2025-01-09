# Store a list of first names. Count the occurrences of ‘a’ within the list.

a = input("Enter a list of first names separated by spaces: ").split()
c = 0
for name in a:
 c+= name.lower().count('a')
 print("The total occurrences of 'a':", c)
