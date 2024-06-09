# EXAMPLE 4: Convert numeric grades to letter grades. Assume grades are between 0 to 100 (Research academic grades values).
grade = int(input("numeric grade: "))

if grade >= 90:
    print("A (Excellent)")
elif grade >= 80:
    print("B (Good)")
elif grade >= 70:
    print("C (Average)")
elif grade >= 60:
    print("D (Poor)")
else:
    print("F (Fail)")