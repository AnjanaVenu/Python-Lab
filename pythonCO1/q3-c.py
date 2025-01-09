# Form a list of vowels selected from a given word

word=input("Enter a Word:")
w1=[n for n in word]
print(w1)
v=['a','e','i','o','u']
l=[n for n in w1 if n.lower() in v]
print("Vowels:",l)
