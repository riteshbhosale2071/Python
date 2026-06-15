def quadrilateral():
    rows = int(input("Enter number of rows: "))
        
    cols = int(input("Enter number of columns: "))

    rectangles = (rows * (rows + 1) * cols * (cols + 1)) // 4

    print("Total Quadrilaterals =", rectangles)

quadrilateral()