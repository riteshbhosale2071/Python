L=[45,23,89,56,75,11,5]
print(L)
maxval=0
for i in L:
    if i > maxval:
        maxval=i
print(f"{maxval} is maximum value in list")