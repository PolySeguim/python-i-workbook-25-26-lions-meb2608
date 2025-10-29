"""
Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade
points in the following manner:
Letter Grade points
A+ 4.0
A 4.0
A- 3.7
B+ 3.3
B 3.0
B- 2.7
C+ 2.3
C 2.0
C- 1.7
D+ 1.3
D 1.0
F 0
Write a program that begins by reading a letter grade from the
user. Then your program should compute and display the equivalent
number of grade points. Ensure that your program generates an
appropriate error message if the user enters an invalid letter
grade.
"""
def get_grade_points(letter):
    grade_mapping = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }
    return grade_mapping.get(letter, None)
letter_grade = input("Enter a letter grade: ")
grade_points = get_grade_points(letter_grade)
if grade_points is not None:
    print(f"The equivalent grade points for {letter_grade} is {grade_points}.")
else:
    print("Error: Invalid letter grade entered.")
            

"""
Exercise 52: In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade. Ensure that your program handles grade point values that fall
between letter grades. These should be rounded to the closes letter
grade. Your program should report A+ for a 4.0 (or greater) grade
point average.
"""
def get_letter_grade(grade_points):
    if grade_points >= 4.0:
        return "A+"
    elif grade_points >= 3.85:
        return "A"
    elif grade_points >= 3.5:
        return "A-"
    elif grade_points >= 3.15:
        return "B+"
    elif grade_points >= 2.85:
        return "B"
    elif grade_points >= 2.5:
        return "B-"
    elif grade_points >= 2.15:
        return "C+"
    elif grade_points >= 1.85:
        return "C"
    elif grade_points >= 1.5:
        return "C-"
    elif grade_points >= 1.15:
        return "D+"
    elif grade_points >= 0.85:
        return "D"
    else:
        return "F"
grade_points_input = float(input("Enter grade points: "))
letter_grade_output = get_letter_grade(grade_points_input)
print(f"The equivalent letter grade for {grade_points_input} is {letter_grade_output}.")

"""
Exercise 66: Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution. In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user. The user will enter a blank
line to indicate that all of the grades have been provided. For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this
exercise. Your program does not need to do any error checking. It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""
def calculate_gpa():
    total_points = 0.0
    count = 0
    while True:
        letter_grade = input("Enter a letter grade (or press Enter to finish): ")
        if letter_grade == "":
            break
        grade_points = get_grade_points(letter_grade)
        total_points += grade_points
        count += 1
    if count > 0:
        gpa = total_points / count
        print(f"The grade point average is {gpa:.2f}.")
    else:
        print("No grades were entered.")
calculate_gpa()
