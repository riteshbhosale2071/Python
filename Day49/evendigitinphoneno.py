def find():
    count = 0
    num = input("Enter a phone no. :")
    for i in num:
        if int(i) % 2 == 0:
            count+=1
    print(f"{num} has {count} even digits")

find()