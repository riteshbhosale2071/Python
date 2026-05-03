grade = lambda m: (
    "A" if m >= 90 else
    "B" if m >= 75 else
    "C" if m >= 60 else
    "D" if m >= 40 else
    "F"
)
marks = 82
print("Grade:", grade(marks))