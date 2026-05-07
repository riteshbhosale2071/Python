t = (1, 2, 3, 2, 4, 5, 1, 6)

duplicates = set()

for i in t:
    if t.count(i) > 1:
        duplicates.add(i)

print("Duplicates:", duplicates)