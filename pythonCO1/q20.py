# From a list of integers, create a list removing even numbers

ls=[int(i) for i in input("Enter the integers :").split()]
nl=[i for i in ls if i%2!=0]
print("List of integers after removing even nos.:",nl)
