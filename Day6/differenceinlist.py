L1=[1,2,3,4,5]
L2=[3,4,5,6,7]
print(L1)
print(L2)
differ=(set(L1).difference(set(L2))).union(set(L2).difference(set(L1)))
print(differ)