L=[45,23,89,56,75,11,5]
print(L)
minval=L[0]
for i in L:
    if i < minval:
        minval=i
print(f"{minval} is minimum value in list")