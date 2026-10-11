def gardenareaplanner():
    print("Garden Area Planner :")

    garden_length = float(input("Enter garden length: "))
    garden_width = float(input("Enter garden width: "))

    if garden_length <= 0 or garden_width <= 0:
        print("Garden dimensions must be greater than zero.")
        return

    total_area = garden_length * garden_width

    flower_percentage = float(input("Enter percentage for flowers: "))
    lawn_percentage = float(input("Enter percentage for lawn: "))
    pathway_percentage = float(input("Enter percentage for pathways: "))

    if flower_percentage < 0 or lawn_percentage < 0 or pathway_percentage < 0:
        print("Percentages cannot be negative.")
        return

    total_percentage = flower_percentage + lawn_percentage + pathway_percentage

    if total_percentage > 100:
        print("Total percentage cannot exceed 100%.")
        return

    flower_area = total_area * flower_percentage / 100
    lawn_area = total_area * lawn_percentage / 100
    pathway_area = total_area * pathway_percentage / 100
    unused_area = total_area - flower_area - lawn_area - pathway_area

    print("\nGarden Area Plan :")
    print("Total Garden Area:", round(total_area, 2))
    print("Flower Area:", round(flower_area, 2))
    print("Lawn Area:", round(lawn_area, 2))
    print("Pathway Area:", round(pathway_area, 2))
    print("Unused Area:", round(unused_area, 2))

    if unused_area == 0:
        print("All garden space has been allocated.")
    else:
        print("Some garden space remains unallocated.")

gardenareaplanner()