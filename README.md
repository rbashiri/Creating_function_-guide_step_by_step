# Creating Functions in Python: Step-by-Step Guide

This project introduces how to create and use functions in Python. It explains the process step by step, from defining a function to calling it with inputs and returning results.

## Files

- `practice.ipynb`: Notebook with examples and practice exercises.
- `README.md`: Project overview and function guide.

## Project Overview

Functions help beginners write cleaner and more reusable code. In this project, you will learn how to:

- Define a function
- Pass values as parameters
- Return results
- Call a function in different scenarios

## Why Functions Are Important

Functions help programmers:

- Reuse code instead of repeating the same logic
- Make programs easier to read and maintain
- Break large problems into smaller tasks
- Improve code organization

## Function Structure in Python

```python
def function_name(parameters):
    # code block
    return result
```

Example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)
```

Output:

```text
8
```

## Steps to Create a Function

1. Define the task
2. Choose a clear function name
3. Identify inputs (parameters)
4. Write the function body
5. Call the function and check the output

Example:

```python
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(4, 6))
```

## Example Functions

### Greeting Function

```python
def greet(name):
    print("Hello", name)

greet("Robabeh")
```

### Check if a Number Is Even

```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
```

### Calculate Rectangle Area

```python
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))
```

## Key Concepts

| Concept | Explanation |
|---|---|
| `def` | Keyword used to define a function |
| `parameters` | Inputs passed into a function |
| `return` | Sends the result back from a function |
| `function call` | Executing the function |

## Conclusion

Functions are a fundamental concept in Python programming. Learning how to create and use them helps developers write cleaner, reusable, and more efficient code.
