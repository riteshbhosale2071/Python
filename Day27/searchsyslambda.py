data = ["Ritesh", "Amit", "Neha", "Karan", "Riya"]
while True:
    search = input("\nEnter name to search (or 'exit'): ").lower()
    if search == "exit":
        break
    result = list(filter(lambda x: search in x.lower(), data))
    if result:
        print("Found:", result)
    else:
        print("No match found")