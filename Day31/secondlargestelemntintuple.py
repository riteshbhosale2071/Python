t = (12, 45, 7, 89, 34, 89, 23)

largest = second = float('-inf')

for num in t:
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Tuple:", t)
print("Largest Number:", largest)
print("Second Largest Number:", second)