# Accept a file name from user and print extension of that.

filename=input("Enter a file name:")
ext=filename.split('.')[-1]
print("The extension of the file is:", ext)
