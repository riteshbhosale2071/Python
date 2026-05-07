t = (1, 2, 3, 2, 4, 1, 5, 2, 3, 1)

frequency = {}

for i in t:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Tuple Elements:")
print(t)

print("\nFrequency of Elements:")

for key, value in frequency.items():
    print(key, "appears", value, "times")