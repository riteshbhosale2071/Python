def find():
    festival = input("Enter festival name: ").lower()

    holidays = ["diwali", "holi", "eid", "christmas", "ganesh chaturthi"]

    if festival in holidays:
        print("Holiday")

    else:
        print("Not a Holiday")

find()