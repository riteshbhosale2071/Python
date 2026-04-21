D = {1:10, 2:20, 3:10, 4:30, 5:20}
print(D)
new_dict = {}
seen = set()
for k, v in D.items():
    if v not in seen:
        new_dict[k] = v
        seen.add(v)
print(new_dict)