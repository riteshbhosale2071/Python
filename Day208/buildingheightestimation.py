import math


def buildingheightestimation():
    print("Building Height Estimation System")

    try:
        distance = float(input("Enter distance from building (meters): "))
        angle = float(input("Enter angle of elevation (degrees): "))
        observer_height = float(input("Enter observer's height (meters): "))

        if distance <= 0:
            print("Error: Distance must be greater than zero.")
            return

        if not 0 < angle < 90:
            print("Error: Angle must be between 0 and 90 degrees.")
            return

        if observer_height < 0:
            print("Error: Observer height cannot be negative.")
            return

        angle_radians = math.radians(angle)
        building_height = distance * math.tan(angle_radians)
        total_height = building_height + observer_height

        print("\nBuilding Height Estimation")
        print("Horizontal Distance:", distance, "meters")
        print("Angle of Elevation:", angle, "degrees")
        print("Observer Height:", observer_height, "meters")
        print("Height Above Observer:", round(building_height, 2), "meters")
        print("Estimated Building Height:", round(total_height, 2), "meters")

    except ValueError:
        print("Error: Please enter valid numeric values.")

buildingheightestimation()