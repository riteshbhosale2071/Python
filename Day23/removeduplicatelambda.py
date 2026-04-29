from functools import reduce
nums = [1, 2, 2, 3, 4, 4, 5]
result = reduce(lambda acc, x: acc + [x] if x not in acc else acc, nums, [])
print(result)