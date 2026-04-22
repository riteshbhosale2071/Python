D = {1:10, 2:50, 3:30, 4:20}
print(D)
max_key = max(D, key=D.get)
print("Key with maximum value:", max_key)