matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = list(map(lambda x: list(x), zip(*matrix)))
print(transpose)