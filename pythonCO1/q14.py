# Accept an integer n and compute n+nn+nnn.

n = int(input("Enter the value for n: "))
nn = int(str(n)*2)
nnn = int(str(n)*3)
result = n + nn + nnn
print("n + nn + nnn =",n,"+",nn,"+",nnn,"=", result)
