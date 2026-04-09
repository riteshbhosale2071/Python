# 1
# 2 2
# 3 3 3 
# 4 4 4 4

num=1
for i in range(1,5):
    for k in range(1,i+1):
        print(f"{num} ",end="")
    num+=1
    print("")
    