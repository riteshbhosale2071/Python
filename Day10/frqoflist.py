T=(1,2,2,3,4,5,5,6,7)
print(T)
freq={}
for i in T:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)