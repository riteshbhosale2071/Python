# 1
# 1 2 
# 1 2 3 
# 1 2 3 4

for i in range(1,5):
    num=1
    for k in range(1,i+1):
        print(f"{num} ",end="")
        num+=1
    print("")