from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(
    lambda a, b: a + b,
    map(lambda x: x*x,
        filter(lambda x: x % 2 == 0, nums)
    )
)
print(result)