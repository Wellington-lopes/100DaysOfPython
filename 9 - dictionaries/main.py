student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score <= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score <= 71:
        student_scores[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

""" COMO EU FIZ

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

student_grades = student_scores
for key in student_grades:
    if student_grades[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_grades[key] >= 81 and student_grades[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_grades[key] >= 71 and student_grades[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


print(student_grades)"""
