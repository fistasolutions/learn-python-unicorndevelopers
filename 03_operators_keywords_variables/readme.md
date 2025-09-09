# Lesson 03: Operators, Keywords & Variables

## Table of Contents
1. [Operators and Operands](#operators-and-operands)
2. [Unary Operators](#unary-operators)
3. [Binary Operators](#binary-operators)
4. [Chained Comparison Operators](#chained-comparison-operators)
5. [Walrus Operator](#walrus-operator)
6. [Identity Operators](#identity-operators)
7. [Membership Operators](#membership-operators)
8. [Python Keywords](#python-keywords)
9. [Python Variables](#python-variables)
10. [Summary](#summary)

---

## Operators and Operands

### What are Operators and Operands?

**Operators** are special symbols that perform operations on values (operands). They are the building blocks of expressions in Python, allowing us to manipulate data and perform calculations.

**Operands** are the values that operators act upon. In the expression `5 + 3`, the `+` is the operator, and `5` and `3` are the operands.

### Python Operator Categories

```mermaid
graph TD
    A["Python Operators"] --> B["Unary Operators"]
    A --> C["Binary Operators"]
    A --> D["Ternary Operators"]
    
    B --> B1["Negative (-)"]
    B --> B2["Logical NOT (not)"]
    B --> B3["Bitwise NOT (~)"]
    
    C --> C1["Arithmetic"]
    C --> C2["Comparison"]
    C --> C3["Logical"]
    C --> C4["Assignment"]
    C --> C5["Identity"]
    C --> C6["Membership"]
    C --> C7["Bitwise"]
    
    C1 --> C1A["+, -, *, /, //, %, **"]
    C2 --> C2A["==, !=, <, >, <=, >="]
    C3 --> C3A["and, or, not"]
    C4 --> C4A["=, +=, -=, *=, /=, etc."]
    C5 --> C5A["is, is not"]
    C6 --> C6A["in, not in"]
    C7 --> C7A["&, |, ^, <<, >>"]
    
    D --> D1["Conditional Expression"]
    D1 --> D1A["value_if_true if condition else value_if_false"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

**Diagram Explanation**: This comprehensive diagram shows the complete hierarchy of Python operators. Unary operators work on a single operand, binary operators work on two operands, and ternary operators work on three operands. Each category contains specific operators with their symbols, making it easy to understand the operator taxonomy in Python.

---

## Unary Operators

Unary operators work on a single operand, performing operations like negation, logical inversion, or bitwise complement.

### Types of Unary Operators

```mermaid
graph LR
    A["Unary Operators"] --> B["Negative (-)"]
    A --> C["Logical NOT (not)"]
    A --> D["Bitwise NOT (~)"]
    
    B --> B1["Changes sign of number"]
    B --> B2["Example: -5"]
    
    C --> C1["Inverts boolean value"]
    C --> C2["Example: not True"]
    
    D --> D1["Inverts bits"]
    D --> D2["Example: ~5"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

**Diagram Explanation**: This diagram illustrates the three main unary operators in Python. The negative operator changes the sign of a number, logical NOT inverts boolean values, and bitwise NOT performs bitwise complement operations. Each operator has specific use cases and examples.

### 1. Negative Operator (-)

The negative operator changes the sign of a number.

```python
# Examples
x = 5
negative_x = -x  # Result: -5

y = -10
positive_y = -y  # Result: 10 (double negative)
```

### 2. Logical NOT Operator (not)

The logical NOT operator inverts boolean values.

```python
# Examples
is_raining = True
is_not_raining = not is_raining  # Result: False

is_sunny = False
is_not_sunny = not is_sunny  # Result: True
```

### 3. Bitwise NOT Operator (~)

The bitwise NOT operator inverts all bits in a number.

```python
# Examples
x = 5  # Binary: 101
result = ~x  # Result: -6 (binary: ...11111010)
```

---

## Binary Operators

Binary operators work on two operands and are the most commonly used operators in Python.

### Arithmetic Operators

```mermaid
graph TD
    A["Arithmetic Operators"] --> B["Addition (+)"]
    A --> C["Subtraction (-)"]
    A --> D["Multiplication (*)"]
    A --> E["Division (/)"]
    A --> F["Floor Division (//)"]
    A --> G["Modulus (%)"]
    A --> H["Exponentiation (**)"]
    
    B --> B1["5 + 3 = 8"]
    C --> C1["10 - 4 = 6"]
    D --> D1["3 * 4 = 12"]
    E --> E1["15 / 3 = 5.0"]
    F --> F1["15 // 4 = 3"]
    G --> G1["15 % 4 = 3"]
    H --> H1["2 ** 3 = 8"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ccff
    style D fill:#99ccff
    style E fill:#99ccff
    style F fill:#99ccff
    style G fill:#99ccff
    style H fill:#99ccff
```

**Diagram Explanation**: This diagram shows all arithmetic operators in Python with their symbols and examples. Each operator performs a specific mathematical operation, from basic addition and subtraction to more advanced operations like floor division and exponentiation.

### Comparison Operators

```mermaid
graph TD
    A["Comparison Operators"] --> B["Equal (==)"]
    A --> C["Not Equal (!=)"]
    A --> D["Less Than (<)"]
    A --> E["Greater Than (>)"]
    A --> F["Less Than or Equal (<=)"]
    A --> G["Greater Than or Equal (>=)"]
    
    B --> B1["5 == 5 → True"]
    C --> C1["5 != 3 → True"]
    D --> D1["3 < 5 → True"]
    E --> E1["5 > 3 → True"]
    F --> F1["3 <= 5 → True"]
    G --> G1["5 >= 3 → True"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ccff
    style D fill:#99ccff
    style E fill:#99ccff
    style F fill:#99ccff
    style G fill:#99ccff
```

**Diagram Explanation**: This diagram illustrates all comparison operators used to compare values in Python. These operators return boolean values (True or False) and are essential for conditional statements and logical flow control.

### Logical Operators

```mermaid
graph TD
    A["Logical Operators"] --> B["AND (and)"]
    A --> C["OR (or)"]
    A --> D["NOT (not)"]
    
    B --> B1["True and True → True"]
    B --> B2["True and False → False"]
    B --> B3["False and True → False"]
    B --> B4["False and False → False"]
    
    C --> C1["True or True → True"]
    C --> C2["True or False → True"]
    C --> C3["False or True → True"]
    C --> C4["False or False → False"]
    
    D --> D1["not True → False"]
    D --> D2["not False → True"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

**Diagram Explanation**: This diagram shows the logical operators and their truth tables. The AND operator returns True only when both operands are True, OR returns True when at least one operand is True, and NOT inverts the boolean value.

### Assignment Operators

```mermaid
graph TD
    A["Assignment Operators"] --> B["Simple Assignment (=)"]
    A --> C["Add and Assign (+=)"]
    A --> D["Subtract and Assign (-=)"]
    A --> E["Multiply and Assign (*=)"]
    A --> F["Divide and Assign (/=)"]
    A --> G["Floor Divide and Assign (//=)"]
    A --> H["Modulus and Assign (%=)"]
    A --> I["Exponentiate and Assign (**=)"]
    
    B --> B1["x = 5"]
    C --> C1["x += 3 (x = x + 3)"]
    D --> D1["x -= 2 (x = x - 2)"]
    E --> E1["x *= 4 (x = x * 4)"]
    F --> F1["x /= 2 (x = x / 2)"]
    G --> G1["x //= 3 (x = x // 3)"]
    H --> H1["x %= 2 (x = x % 2)"]
    I --> I1["x **= 2 (x = x ** 2)"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ccff
    style D fill:#99ccff
    style E fill:#99ccff
    style F fill:#99ccff
    style G fill:#99ccff
    style H fill:#99ccff
    style I fill:#99ccff
```

**Diagram Explanation**: This diagram shows all assignment operators in Python. The simple assignment operator (=) assigns a value, while compound assignment operators perform an operation and assign the result back to the variable, making code more concise.

---

## Chained Comparison Operators

Python allows chaining comparison operators for more readable and concise code.

### Chained Comparison Concept

```mermaid
graph LR
    A["Chained Comparisons"] --> B["Multiple Conditions"]
    A --> C["Readable Code"]
    A --> D["Short-Circuit Evaluation"]
    
    B --> B1["x < y < z"]
    B --> B2["Equivalent to: x < y and y < z"]
    
    C --> C1["More Natural Expression"]
    C --> C2["Mathematical Notation"]
    
    D --> D1["Stops at First False"]
    D --> D2["Efficient Evaluation"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

**Diagram Explanation**: This diagram illustrates the concept of chained comparisons in Python. Chained comparisons allow multiple conditions to be expressed in a more natural, mathematical way, and Python evaluates them efficiently using short-circuit evaluation.

### Examples

```python
# Chained comparisons
x = 5
y = 10
z = 15

# These are equivalent:
result1 = x < y < z  # True
result2 = x < y and y < z  # True

# More complex chained comparisons
age = 25
result = 18 <= age <= 65  # True (age is between 18 and 65)
```

---

## Walrus Operator

The walrus operator (:=) was introduced in Python 3.8 and allows assignment and expression evaluation in a single statement.

### Walrus Operator Concept

```mermaid
graph TD
    A["Walrus Operator (:=)"] --> B["Assignment + Expression"]
    A --> C["Python 3.8+"]
    A --> D["Use Cases"]
    
    B --> B1["Assigns and Returns Value"]
    B --> B2["Reduces Code Duplication"]
    
    C --> C1["New Feature"]
    C --> C2["Modern Python"]
    
    D --> D1["While Loops"]
    D --> D2["List Comprehensions"]
    D --> D3["Conditional Statements"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

**Diagram Explanation**: This diagram shows the walrus operator's key characteristics and use cases. It's a modern Python feature that combines assignment and expression evaluation, making code more concise and readable in specific scenarios.

### Examples

```python
# Traditional approach
user_input = input("Enter a number: ")
while user_input != "quit":
    print(f"You entered: {user_input}")
    user_input = input("Enter a number: ")

# Using walrus operator
while (user_input := input("Enter a number: ")) != "quit":
    print(f"You entered: {user_input}")

# In list comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [square := x**2 for x in numbers if (square := x**2) > 10]
```

---

## Identity Operators

Identity operators compare the memory locations of objects, not their values.

### Identity Operators Overview

```mermaid
graph TD
    A["Identity Operators"] --> B["is"]
    A --> C["is not"]
    
    B --> B1["Checks if Same Object"]
    B --> B2["Memory Location Comparison"]
    B --> B3["Example: x is y"]
    
    C --> C1["Checks if Different Objects"]
    C --> C2["Opposite of 'is'"]
    C --> C3["Example: x is not y"]
    
    D["Object Identity"] --> E["Same Memory Address"]
    D --> F["Different from Equality"]
    
    E --> E1["x is y → True"]
    F --> F1["x == y vs x is y"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#ffcc99
    style F fill:#ffcc99
```

**Diagram Explanation**: This diagram illustrates identity operators and their relationship to object identity. The 'is' operator checks if two variables refer to the same object in memory, while 'is not' checks if they refer to different objects. This is different from equality comparison which checks values.

### Examples

```python
# Identity vs Equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Equality comparison (values)
print(a == b)  # True (same values)
print(a == c)  # True (same values)

# Identity comparison (objects)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# Special case with small integers
x = 5
y = 5
print(x is y)  # True (Python optimizes small integers)
```

---

## Membership Operators

Membership operators test whether a value is a member of a sequence (like a list, tuple, or string).

### Membership Operators Overview

```mermaid
graph TD
    A["Membership Operators"] --> B["in"]
    A --> C["not in"]
    
    B --> B1["Checks if Value is Present"]
    B --> B2["Returns True if Found"]
    B --> B3["Example: 'a' in 'apple'"]
    
    C --> C1["Checks if Value is Absent"]
    C --> C2["Returns True if Not Found"]
    C --> C3["Example: 'z' not in 'apple'"]
    
    D["Works With"] --> E["Strings"]
    D --> F["Lists"]
    D --> G["Tuples"]
    D --> H["Sets"]
    D --> I["Dictionaries (keys)"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#ffcc99
    style F fill:#ffcc99
    style G fill:#ffcc99
    style H fill:#ffcc99
    style I fill:#ffcc99
```

**Diagram Explanation**: This diagram shows membership operators and the data types they work with. The 'in' operator checks if a value exists in a sequence, while 'not in' checks if it doesn't exist. These operators work with various Python data structures.

### Examples

```python
# String membership
text = "Hello, World!"
print('H' in text)      # True
print('hello' in text)  # False (case-sensitive)
print('z' not in text)  # True

# List membership
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)     # True
print(6 not in numbers) # True

# Dictionary membership (checks keys)
person = {'name': 'Alice', 'age': 30}
print('name' in person)    # True
print('salary' not in person)  # True
```

---

## Python Keywords

Keywords are reserved words in Python that have special meanings and cannot be used as variable names.

### Python Keywords Categories

```mermaid
graph TD
    A["Python Keywords"] --> B["Control Flow"]
    A --> C["Data Types"]
    A --> D["Functions & Classes"]
    A --> E["Exception Handling"]
    A --> F["Import & Modules"]
    A --> G["Logical Operations"]
    A --> H["Other"]
    
    B --> B1["if, elif, else"]
    B --> B2["for, while"]
    B --> B3["break, continue"]
    B --> B4["pass"]
    
    C --> C1["True, False"]
    C --> C2["None"]
    C --> C3["and, or, not"]
    
    D --> D1["def, class"]
    D --> D2["return, yield"]
    D --> D3["lambda"]
    
    E --> E1["try, except"]
    E --> E2["finally, raise"]
    E --> E3["assert"]
    
    F --> F1["import, from"]
    F --> F2["as"]
    
    G --> G1["and, or, not"]
    G --> G2["in, is"]
    
    H --> H1["del"]
    H --> H2["global, nonlocal"]
    H --> H3["with"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
    style F fill:#99ffcc
    style G fill:#ff99cc
    style H fill:#ffff99
```

**Diagram Explanation**: This comprehensive diagram categorizes Python keywords by their functionality. Keywords are organized into logical groups like control flow, data types, functions, exception handling, and more, making it easier to understand their purposes and usage.

### Complete List of Python Keywords

```python
# Python 3.11 keywords
keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield'
]

# Check if a word is a keyword
import keyword
print(keyword.iskeyword('if'))    # True
print(keyword.iskeyword('hello')) # False
```

### Important Keyword Examples

```python
# Control flow keywords
if True:
    print("This will execute")
elif False:
    print("This won't execute")
else:
    print("This won't execute either")

# Loop keywords
for i in range(5):
    if i == 3:
        break  # Exit loop
    if i == 1:
        continue  # Skip iteration
    print(i)

# Function and class keywords
def my_function():
    return "Hello"

class MyClass:
    pass  # Placeholder

# Exception handling keywords
try:
    risky_operation()
except ValueError:
    print("Value error occurred")
finally:
    print("This always executes")
```

---

## Python Variables

Variables are containers that store data values. Understanding variable naming rules and conventions is crucial for writing clean, maintainable Python code.

### Variable Naming Rules

```mermaid
graph TD
    A["Variable Naming Rules"] --> B["Must Start With"]
    A --> C["Can Contain"]
    A --> D["Cannot Be"]
    A --> E["Case Sensitive"]
    
    B --> B1["Letter (a-z, A-Z)"]
    B --> B2["Underscore (_)"]
    B --> B3["NOT: Number or Symbol"]
    
    C --> C1["Letters (a-z, A-Z)"]
    C --> C2["Numbers (0-9)"]
    C --> C3["Underscores (_)"]
    
    D --> D1["Python Keywords"]
    D --> D2["Special Characters"]
    D --> D3["Spaces"]
    
    E --> E1["age ≠ Age ≠ AGE"]
    E --> E2["Different Variables"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

**Diagram Explanation**: This diagram outlines the fundamental rules for naming variables in Python. Variables must start with a letter or underscore, can contain letters, numbers, and underscores, cannot be keywords or contain special characters, and are case-sensitive.

### Naming Conventions

```mermaid
graph TD
    A["Naming Conventions"] --> B["snake_case"]
    A --> C["CamelCase"]
    A --> D["UPPER_CASE"]
    A --> E["Special Cases"]
    
    B --> B1["Variables & Functions"]
    B --> B2["user_name, total_price"]
    B --> B3["PEP 8 Recommended"]
    
    C --> C1["Class Names"]
    C --> C2["BankAccount, DataModel"]
    C --> C3["PascalCase"]
    
    D --> D1["Constants"]
    D --> D2["MAX_SPEED, PI"]
    D --> D3["Global Constants"]
    
    E --> E1["Private Variables"]
    E --> E2["_internal_var"]
    E --> E3["Name Mangling"]
    E --> E4["__secret_key"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

**Diagram Explanation**: This diagram shows the different naming conventions used in Python. snake_case is used for variables and functions, CamelCase for classes, UPPER_CASE for constants, and special prefixes for private variables and name mangling.

### Variable Assignment and Operations

```mermaid
graph TD
    A["Variable Operations"] --> B["Simple Assignment"]
    A --> C["Multiple Assignment"]
    A --> D["Type Hints"]
    A --> E["Deletion"]
    
    B --> B1["x = 10"]
    B --> B2["name = 'Alice'"]
    
    C --> C1["x, y = 1, 2"]
    C --> C2["a = b = c = 0"]
    
    D --> D1["x: int = 10"]
    D --> D2["name: str = 'Alice'"]
    
    E --> E1["del variable_name"]
    E --> E2["Frees Memory"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

**Diagram Explanation**: This diagram illustrates different ways to work with variables in Python, from simple assignment to multiple assignments, type hints, and variable deletion. Each method serves specific purposes in Python programming.

### Examples

```python
# Simple assignment
age = 25
name = "Alice"
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0  # All variables get the same value

# Type hints
age: int = 25
name: str = "Alice"
scores: list[int] = [85, 90, 78]

# Variable deletion
temp_var = "temporary"
del temp_var
# print(temp_var)  # This would raise NameError

# Valid variable names
user_name = "john_doe"
total_price = 99.99
MAX_ATTEMPTS = 3
_internal_var = "private"

# Invalid variable names (would cause SyntaxError)
# 2name = "invalid"     # Starts with number
# class = "invalid"     # Python keyword
# user-name = "invalid" # Contains hyphen
```

---

## Summary

This lesson covered the fundamental building blocks of Python programming:

### Key Concepts Covered

```mermaid
mindmap
  root((Python Fundamentals))
    Operators
      Unary
        Negative
        Logical NOT
        Bitwise NOT
      Binary
        Arithmetic
        Comparison
        Logical
        Assignment
      Special
        Identity
        Membership
        Walrus
    Keywords
      Control Flow
      Data Types
      Functions
      Exceptions
      Import
    Variables
      Naming Rules
      Conventions
      Assignment
      Type Hints
      Deletion
```

**Diagram Explanation**: This mind map provides a comprehensive overview of all the topics covered in this lesson. It shows the hierarchical relationship between operators, keywords, and variables, making it easy to see how these fundamental concepts interconnect in Python programming.

### Best Practices

1. **Use descriptive variable names** that clearly indicate their purpose
2. **Follow PEP 8 naming conventions** for consistency
3. **Use type hints** to improve code readability and maintainability
4. **Understand operator precedence** to avoid unexpected results
5. **Use appropriate operators** for the task at hand
6. **Avoid using keywords** as variable names

### Next Steps

With a solid understanding of operators, keywords, and variables, you're ready to move on to more advanced Python concepts like:
- Control flow structures (if/else, loops)
- Functions and classes
- Data structures (lists, dictionaries, sets)
- File handling and modules

Remember: Practice is key to mastering these fundamental concepts. Try writing small programs that use different operators and variable types to reinforce your learning!
