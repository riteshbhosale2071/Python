def find():
    heads = int(input("Enter total heads: "))
    legs = int(input("Enter total legs: "))
    dogs = (legs - 2 * heads) // 2
    chickens = heads - dogs
    print("Dogs =", dogs)
    print("Chickens =", chickens)

find()