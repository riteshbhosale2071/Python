D = {1:30, 2:10, 3:50, 4:20}
print(D)
sorted_dict = dict(sorted(D.items(), key=lambda x: x[1]))
print(sorted_dict)