def giftbox():
    boxes = int(input("Enter number of gift boxes: "))
    
    gifts_per_box = int(input("Enter gifts in each box: "))

    total_gifts = boxes * gifts_per_box

    print("Total Gifts =", total_gifts)

giftbox()