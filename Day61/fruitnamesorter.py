def fruit():
    fruits = input("Enter fruit names separated by space: ").split()

    fruits.sort()

    print("Sorted Fruits:")
    
    for fruit in fruits:
        print(fruit)

fruit()