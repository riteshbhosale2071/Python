nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
longest = max(map(lambda x: sum(1 for i in range(x, x+len(nums)) if i in s), s))
print("Longest consecutive length:", longest)