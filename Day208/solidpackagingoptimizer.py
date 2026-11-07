import math


def solidpackagingoptimizer():
    print("Solid Packaging Optimizer")

    try:
        length = float(input("Enter solid length (cm): "))
        width = float(input("Enter solid width (cm): "))
        height = float(input("Enter solid height (cm): "))

        box_length = float(input("Enter packaging box length (cm): "))
        box_width = float(input("Enter packaging box width (cm): "))
        box_height = float(input("Enter packaging box height (cm): "))

        if min(length, width, height, box_length, box_width, box_height) <= 0:
            print("Error: All dimensions must be greater than zero.")
            return

        solid_volume = length * width * height
        box_volume = box_length * box_width * box_height

        orientations = [
            (length, width, height),
            (length, height, width),
            (width, length, height),
            (width, height, length),
            (height, length, width),
            (height, width, length)
        ]

        fitting_orientations = []

        for orientation in orientations:
            if (
                orientation[0] <= box_length
                and orientation[1] <= box_width
                and orientation[2] <= box_height
            ):
                if orientation not in fitting_orientations:
                    fitting_orientations.append(orientation)

        print("\nPackaging Optimization Results")
        print("Solid Volume:", round(solid_volume, 2), "cm³")
        print("Box Volume:", round(box_volume, 2), "cm³")

        if fitting_orientations:
            best_orientation = min(
                fitting_orientations,
                key=lambda x: box_volume - solid_volume
            )

            print("Packaging Status: Solid fits inside the box.")
            print("Possible Orientations:", len(fitting_orientations))
            print("Selected Orientation:", best_orientation)

            space_used = (solid_volume / box_volume) * 100
            unused_space = 100 - space_used

            print("Space Utilization:", round(space_used, 2), "%")
            print("Unused Space:", round(unused_space, 2), "%")
        else:
            print("Packaging Status: Solid does not fit inside the box.")
            print("Suggestion: Use a larger packaging box.")

    except ValueError:
        print("Error: Please enter valid numeric dimensions.")

solidpackagingoptimizer()