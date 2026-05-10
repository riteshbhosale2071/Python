salary = float(input("Enter Salary: "))

hra = salary * 0.10
da = salary * 0.05
pf = salary * 0.03

if salary >= 500000 and salary <= 1000000:
    tax = salary * 0.10
elif salary >= 1100000 and salary <= 2000000:
    tax = salary * 0.20
elif salary >= 2000000 and salary <= 3000000:
    tax = salary * 0.30
elif salary >= 0 and salary <= 100000:
    print("k")
    tax = 0
else:
    tax = 0

in_hand = salary - (hra + da + pf + tax)

print("HRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Tax =", tax)
print("In-hand Salary =", in_hand)