# Generate positive list of numbers from a given list of integers

l = [int(i) for i in input("Enter elements: ").split()]
l_p = [i for i in l if i>=0]
print("List of +ve numbers: " , l_p)
