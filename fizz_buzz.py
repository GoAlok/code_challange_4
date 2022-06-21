"""
    Instruction:
        - Write a program that a automatically print the solution of the fizz buzz game.
        
            - Your program should print the each number form 1 to 100 in turn
            - When the number is divisible by 3, then instead of printing eg.: 3 print "Fizz"
            - & when the number is divisible by 5, then instead of printing eg.: 5 print "Buzz"
            - & when the number is divisible by 3, 5 both then instead of printing eg.: 15 print "FizzBuzz".
"""

for number in range(1, 101):
    if not number % (3 * 5):
        print("FizzBuzz")
    elif not number % 5:
        print("Buzz")
    elif not number % 3:
        print("Fizz")
    else: print(number)
    
    # OR
print("---------- METHOD 2 ----------")
    
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)