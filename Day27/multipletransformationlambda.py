nums = [1, 2, 3, 4]
result = list(
    map(lambda x: str(x + 10),
        map(lambda x: x*x, nums)
    )
)
print(result)