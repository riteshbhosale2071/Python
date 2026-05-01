prices = [100, 200, 300, 400]
final_prices = list(map(lambda x: x + (x * 0.18), prices))
print(final_prices)