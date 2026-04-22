D = {1:"", 2:"20", 3:"30", 4:"", 5:"50"}
print(D)
for i in list(D):
    if D[i] == "":
        D.pop(i)
print(D)