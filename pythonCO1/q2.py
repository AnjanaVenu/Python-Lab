# Display future leap years from current year to a final year

yr1 = int(input("Enter first year:"))
yr2 = int(input("Enter second year:"))
print("Leap year between",yr1,"and",yr2,"is")
for i in range(yr1,yr2+1):
 if (i%4==0 and i%100!=0) or (i%400==0):
   print(i)
