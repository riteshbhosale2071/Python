def planet():
    planet_no = int(input("Enter planet number (1-8): "))

    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }

    print("Planet Name =", planets.get(planet_no, "Invalid Number"))

planet()