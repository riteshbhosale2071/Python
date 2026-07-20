def arrangedecimals(numbers):
    numbers.sort()
    print("Decimals in Ascending Order:")
    
    for num in numbers:
        print(num)

count = int(input("How many decimal numbers? "))

decimallist = []

for i in range(count):
    decimal = float(input("Enter decimal number: "))
    decimallist.append(decimal)

arrangedecimals(decimallist)