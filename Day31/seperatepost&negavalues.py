t = (10, -5, 20, -8, 0, 15, -2, 7)

positive = []
negative = []

for num in t:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

positive_tuple = tuple(positive)
negative_tuple = tuple(negative)

print("Original Tuple:", t)
print("Positive Numbers:", positive_tuple)
print("Negative Numbers:", negative_tuple)