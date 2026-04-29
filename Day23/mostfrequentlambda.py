nums = [1, 2, 2, 3, 3, 3, 4]
res = max(nums, key=lambda x: nums.count(x))
print("Most frequent element:", res)