S1={1,2,3,4,5}
S2={4,5,6,7,8}
print(S1)
print(S2)
if S1.intersection(S2):
    print("Set has common values ",S1.intersection(S2))
else:
    print("Set has no common values")