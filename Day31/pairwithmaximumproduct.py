t = (3, 5, -10, -20, 7)

max_product = float('-inf')
pair = ()

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        product = t[i] * t[j]

        if product > max_product:
            max_product = product
            pair = (t[i], t[j])

print("Pair:", pair)
print("Maximum Product:", max_product)