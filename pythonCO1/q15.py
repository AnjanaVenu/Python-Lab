# Print out all colors from color-list1 not contained in color-list2.

list1 = input("Enter colors for List 1, separated by commas: ").split(",")
list2 = input("Enter colors for List 2, separated by commas: ").split(",")
print("List 1:", list1)
print("List 2:", list2)
res = set(list1) - set(list2)
print("Print Colors in List 1 but not in List 2 as Set:", res)
print("Print as List:", list(res))
