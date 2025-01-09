# Count the occurrences of each word in a line of text.

text=[word for word in input("Enter a text:").split()]
count=[(word, text.count(word)) for word in set(text)]
print("Word occurrences:")
for word, cnt in count:
    print(word + ":", cnt)
