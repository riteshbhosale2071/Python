import math

def converseofbasicproportionality():
    print("Converse of Basic Proportionality Theorem Checker")

    print("\nEnter the side lengths of the triangle:")
    ab = float(input("Enter AB: "))
    ac = float(input("Enter AC: "))

    print("\nEnter the divided side lengths:")
    ad = float(input("Enter AD: "))
    db = float(input("Enter DB: "))
    ae = float(input("Enter AE: "))
    ec = float(input("Enter EC: "))

    if min(ab, ac, ad, db, ae, ec) <= 0:
        print("All side lengths must be positive.")
        return

    if not math.isclose(ad + db, ab, rel_tol=1e-9):
        print("Invalid data: AD + DB must equal AB.")
        return

    if not math.isclose(ae + ec, ac, rel_tol=1e-9):
        print("Invalid data: AE + EC must equal AC.")
        return

    ratio1 = ad / db
    ratio2 = ae / ec

    print("\nConverse of BPT Verification:")
    print("AD / DB =", round(ratio1, 4))
    print("AE / EC =", round(ratio2, 4))

    if math.isclose(ratio1, ratio2, rel_tol=1e-9):
        print("Result: The ratios are equal.")
        print("The Converse of Basic Proportionality Theorem is verified.")
        print("DE is parallel to BC, assuming D and E lie on sides AB and AC.")
    else:
        print("Result: The ratios are not equal.")
        print("The Converse of Basic Proportionality Theorem is not verified.")

converseofbasicproportionality()