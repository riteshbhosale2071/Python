def counter():
    candles = int(input("Enter total candles: "))
    
    blown = int(input("Enter candles blown out: "))

    print("Remaining Candles =", candles - blown)

counter()