L=[1, 2, 3, 4, 5]
is_sorted=all(map(lambda i: L[i] <= L[i+1], range(len(L)-1)))
print(is_sorted)