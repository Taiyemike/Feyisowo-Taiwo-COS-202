# PERSONAL POCKET CGPA CALCULATOR (PP)

print("PERSONAL POCKET CGPA CALCULATOR")

courses = int(input("Enter number of courses: "))

total_points = 0
total_units = 0

for i in range(courses):
    print("\nCourse", i + 1)

    score = float(input("Enter score: "))
    unit = int(input("Enter course unit: "))

    # Selection Control Statement
    if score >= 70:
        gp = 5
    elif score >= 60:
        gp = 4
    elif score >= 50:
        gp = 3
    elif score >= 45:
        gp = 2
    elif score >= 40:
        gp = 1
    else:
        gp = 0

    total_points += gp * unit
    total_units += unit

cgpa = total_points / total_units

print("\nYour CGPA is:", round(cgpa, 2))

# Classification
if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")