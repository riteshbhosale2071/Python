str1="hello"
print(str1)
S=set(str1)
count=0
print(S)
for i in S:
    count+=1
print(f"String has {count} unique values")