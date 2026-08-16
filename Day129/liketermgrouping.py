def liketermgrouping():
    terms = input("Enter algebraic terms separated by spaces: ").split()

    if not terms:
        print("Please enter at least one term.")
        return

    def get_variable_part(term):
        variable = ""
        for char in term:
            if char.isalpha():
                variable += char
        return variable

    def get_exponent(term):
        if "^" in term:
            return term.split("^")[-1]
        return "1"

    groups = {}

    for term in terms:
        variable = get_variable_part(term)
        exponent = get_exponent(term)

        key = (variable, exponent)

        if key not in groups:
            groups[key] = []

        groups[key].append(term)

    print("\nLike-Term Groups:")

    for key, group in groups.items():
        print(f"{key[0]}^{key[1]} :", group)

liketermgrouping()