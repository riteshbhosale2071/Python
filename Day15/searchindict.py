D = {1:10, 2:20, 3:30, 4:40, 5:50}
num = 3
for i in D:
    if i == num:
        print("Found")
        break
else:
    print("Not Found")