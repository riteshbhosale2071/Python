data = [10, 15, 20, 25, 30, 35, 40]
filters = {
    1: ("Even numbers", lambda x: x % 2 == 0),
    2: ("Odd numbers", lambda x: x % 2 != 0),
    3: ("Greater than 20", lambda x: x > 20),
    4: ("Less than 30", lambda x: x < 30)
}
while True:
    print("\nFilter Menu")
    for key, value in filters.items():
        print(f"{key}. {value[0]}")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting...")
        break
    if choice in filters:
        result = list(filter(filters[choice][1], data))
        print("Filtered result:", result)
    else:
        print("Invalid choice!")