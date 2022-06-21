"""
    Write a program that calculates sum of all even numbers between 1 and 100 both included.
"""
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# OR

total2 = 0
for number2 in range(1, 101):
    if number2 % 2 == 0:
        total2 += number2
print(total2)