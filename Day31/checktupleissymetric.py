t = (1, 2, 3, 1, 2, 3)

mid = len(t) // 2

first_half = t[:mid]
second_half = t[mid:]

print("Tuple:", t)

if first_half == second_half:
    print("Tuple is Symmetric")
else:
    print("Tuple is Not Symmetric")

print("First Half:", first_half)
print("Second Half:", second_half)