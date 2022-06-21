"""
    Instruction-
        Write a program that calculate avg height of student height from a list of heights.
    
    --> average height  = sum of all height / total numbers of height.
    
    - and avg height to be rounded to nearest whole number.
    
    - example input: 180, 145, 165, 198, 136, 175, 169, 184, 137, 195, 166, 132, 147, 190
"""
student_heights = input("Input the list of student heights: \n").split(", ")
avg_height = 0
total_student_height = 0
for student_height in student_heights:
    student_height = int(student_height)
    # total_student_height = total_student_height + student_height  # ----- OR -----
    total_student_height += student_height
avg_height = total_student_height / len(student_heights)
print("Final total student height:",total_student_height)
print(round(avg_height))

# finding no. of students in student_heights using "FOR LOOP".
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)