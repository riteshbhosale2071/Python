from functools import reduce
L1 = [1, 2, 3]
L2 = [3, 4, 5]
union = reduce(lambda acc, x: acc + [x] if x not in acc else acc, L1 + L2, [])
print(union)