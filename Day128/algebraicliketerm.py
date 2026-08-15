def algebraicliketerm():
    term1 = input("Enter the first algebraic term: ").strip()
    term2 = input("Enter the second algebraic term: ").strip()

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

    variable1 = get_variable_part(term1)
    variable2 = get_variable_part(term2)

    exponent1 = get_exponent(term1)
    exponent2 = get_exponent(term2)

    if variable1 == variable2 and exponent1 == exponent2:
        print("The terms are Like Terms.")
    else:
        print("The terms are Unlike Terms.")

algebraicliketerm()