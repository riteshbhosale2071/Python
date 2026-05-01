prices = [100, 200, 300, 400]
discounted = list(map(lambda x: x - (x * 0.10), prices))
print(discounted)