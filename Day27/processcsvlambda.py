data = ["Ritesh,85,IT", "Amit,70,HR", "Neha,90,IT"]
result = list(filter(lambda x: int(x.split(",")[1]) > 75, data))
print(result)