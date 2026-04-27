L=[{"id":3}, {"id":1}, {"id":2}]
print(L)
L.sort(key=lambda a: a["id"])
print(L)