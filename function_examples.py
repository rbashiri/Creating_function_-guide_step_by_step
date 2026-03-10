"""Function examples moved from README for cleaner project documentation."""


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(result)


def add_numbers_verbose(a, b):
    result = a + b
    return result


print(add_numbers_verbose(4, 6))


def greet(name):
    print("Hello", name)


greet("Robabeh")


def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))


def calculate_area(length, width):
    return length * width


print(calculate_area(5, 3))
