nums = [1, 2, 4, 6, 7]
print(nums)
missing = list(filter(lambda x: x not in nums, range(min(nums), max(nums)+1)))
print(missing)