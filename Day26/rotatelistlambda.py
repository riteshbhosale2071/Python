L = [1, 2, 3, 4, 5]
print(L)
rotate_left = lambda lst, k: lst[k:] + lst[:k]
print(rotate_left(L, 2))