base=float(input("Enter the base of triangle:"))
height=float(input("Enter the height of triangle:"))
hypo=float(input("Enter the hypo of triangle:"))
if hypo**2==((base**2)+(height**2)):
    print("The triangle is right angled triangle")
else:
    print("The triangle is not right angled triangle")