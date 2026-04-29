nums = [10, 20, 4, 45, 99, 99]
result = sorted(set(nums), key=lambda x: x)[-2]
print("Second largest:", result)