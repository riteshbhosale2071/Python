flatten = lambda L: [item for x in L for item in (flatten(x) if isinstance(x, list) else [x])]
nested = [1, [2, [3, 4], 5], [6, 7], 8]
result = flatten(nested)
print(result)