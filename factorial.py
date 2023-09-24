import math

number = int(input("Enter a number:- "))
print("Math function:- ", math.factorial(number))


def facto(number):
    facto = 1
    for num in range (1, number + 1):
        facto *= num
    return facto


result = facto(number)
print("Function Call:- ", result)


def recursive_facto(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * recursive_facto(number - 1)

result = recursive_facto(number)
print("Recursive Factorial:", result)
