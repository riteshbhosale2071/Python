def petrol():
    price_per_litre = float(input("Enter petrol price per litre: "))
    
    litres = float(input("Enter litres of petrol: "))

    cost = price_per_litre * litres

    print("Total Petrol Cost = ₹", cost)

petrol()