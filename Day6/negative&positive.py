L=[-4,-3,-2,-1,0,1,2,3]
C1=0
C2=0
print(L)
for i in L:
    if i>=0:
        C1+=1
    else:
        C2+=1
print(f"List has {C1} positive and {C2} negative values")