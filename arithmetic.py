"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return float(num1 + num2)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return float(num1 - num2)

def multiply(num1, num2):
    """Multiply the two inputs together."""

    return float(num1 * num2)

def divide(num1, num2):
    """Divide the first input by the second and return the result."""


def square(num1):
    """Return the square of the input."""


def cube(num1):
    """Return the cube of the input."""


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

user_entry = input()

problem = user_entry.split(' ') #creates a list of strings

def calculator(problem):
    operator = problem[0]
    num1 = int(problem[1])
    num2 = int(problem[2])

    if operator == '+':
        return add(num1, num2)

    elif operator == '-':
        return subtract(num1, num2)

    elif operator == '*':
        return multiply(num1, num2)

print(calculator(problem))
# get mathematical operator and numbers from user input



#if operator == '+':
 #   print(add(num1, num2))
# map operators to their function
# call the right function
# return correct value in float