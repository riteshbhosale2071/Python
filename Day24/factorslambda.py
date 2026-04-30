num = 12
factors=list(filter(lambda x: num % x == 0, range(1, num+1)))
print("Factors:", factors)