"""
    Instruction:
        Write a program that calculates highest total from the score list.
        
        example scores: 78, 65, 89, 86, 55, 99, 91, 64, 89, 87, 73
"""

student_scores = input("Input the list of students score: ").split(", ")
highest_score = 0
for score in range(0, len(student_scores)):
    student_scores[score] = int(student_scores[score])
# print(student_scores)

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}")