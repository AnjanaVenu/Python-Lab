# Create a list of colors from comma-separated color names entered by user. Display first and last colors.

ls=input("Enter list of colors with comma-separated color:").split(",")
print("Display the first color: ",ls[0])
print("Display the last color: ",ls[-1])
