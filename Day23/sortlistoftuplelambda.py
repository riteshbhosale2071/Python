L=[(1,3),(2,1),(2,2),(1,2)]
print(L)
L.sort(key=lambda a: (a[0], -a[1]))
print(L)