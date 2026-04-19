S={1,2,3,4,5,6,7,8,9}
print(S)
S2=set()
for i in S:
    if i%2==1:
        S2.add(i)
print(S2)