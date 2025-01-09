# list of integers for all values greater than 100 store 'over' instead use list comprehension.

u = input("Enter the list of integers separated by spaces:") 
result=['over' if int(num) > 100 else int(num) for num in u.split()]
print(result)
