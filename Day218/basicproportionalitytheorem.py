import math

def basicproportionalitytheorem():
    print("Basic Proportionality Theorem :")

    print("\nEnter the sides of the triangle:")
    ab = float(input("Enter AB: "))
    ac = float(input("Enter AC: "))

    print("\nEnter the divided side lengths:")
    ad = float(input("Enter AD: "))
    ae = float(input("Enter AE: "))
    db = float(input("Enter DB: "))
    ec = float(input("Enter EC: "))

    if min(ab, ac, ad, ae, db, ec) <= 0:
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

    print("\nBasic Proportionality Theorem Verification:")
    print("AD / DB =", round(ratio1, 4))
    print("AE / EC =", round(ratio2, 4))

    if math.isclose(ratio1, ratio2, rel_tol=1e-9):
        print("Result: Basic Proportionality Theorem is verified.")
        print("DE is parallel to BC.")
    else:
        print("Result: Basic Proportionality Theorem is not verified.")
        print("DE is not parallel to BC.")

basicproportionalitytheorem()