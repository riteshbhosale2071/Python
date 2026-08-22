def chapatirequiremet():
    people = int(input("Enter number of people: "))
    chapatis_per_person = int(input("Enter chapatis required per person: "))

    if people <= 0 or chapatis_per_person <= 0:
        print("Enter positive values.")
        return

    total_chapatis = people * chapatis_per_person

    print("Total Chapatis Required:", total_chapatis)

chapatirequiremet()