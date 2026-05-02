L = [4, 1, 3, 2, 5]
print(L)
key_func = lambda x: x
for i in range(len(L)):
    for j in range(0, len(L)-i-1):
        if key_func(L[j]) > key_func(L[j+1]):
            L[j], L[j+1] = L[j+1], L[j]
print(L)