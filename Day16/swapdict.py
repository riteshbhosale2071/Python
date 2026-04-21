D = {1:10, 2:20, 3:30}
print(D)
swapped = {}
for k, v in D.items():
    swapped[v] = k
print(swapped)