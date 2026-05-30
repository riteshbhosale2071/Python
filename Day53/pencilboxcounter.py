def counter():
    pencils = int(input("Enter total pencils: "))

    boxes = pencils // 10
    left = pencils % 10

    print("Pencil Boxes =", boxes)
    print("Loose Pencils =", left)

counter()