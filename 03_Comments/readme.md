# Comments in Python

## What are Comments?
Comments are lines in a program that are ignored by the Python interpreter. They are used to explain the code, make it more readable, and provide context for other developers or your future self.

### Why Use Comments?
- Explain the purpose of the code.
- Debug or temporarily disable parts of the code.
- Enhance code readability and maintainability.

---

## Single-Line Comments
Single-line comments begin with the `#` symbol. Everything after the `#` on that line is treated as a comment.

### Example:
```python
# This is a single-line comment
print("Hello, World!")  # This prints a message to the console
```

### Output:
```
Hello, World!
```

---

## Multi-Line Comments
Python does not have a specific syntax for multi-line comments. However, you can use triple quotes (`'''` or `"""`) to create a block of text that acts as a comment. Note that this is technically a string and is not treated as a comment unless it is not assigned to a variable.

### Example:
```python
"""
This is a multi-line comment.
You can use it to explain larger pieces of code.
"""
print("Python supports multi-line comments using triple quotes.")
```

### Output:
```
Python supports multi-line comments using triple quotes.
```

---

## Best Practices for Comments
1. **Keep Comments Relevant:** Write comments that explain the *why*, not the *what*, of your code.
   ```python
   # Fetch user data from the database
   user_data = fetch_data()
   ```

2. **Update Comments:** Ensure comments stay up-to-date with code changes.

3. **Avoid Redundant Comments:** Do not write comments that repeat what the code already clearly states.
   ```python
   # Increment the counter by 1  (Redundant)
   counter += 1
   ```

4. **Use Proper Formatting:** Use capitalization and punctuation for clarity.
   ```python
   # This function calculates the factorial of a number.
   ```

---

## Running Python with Comments
Comments are ignored by the Python interpreter and do not affect program execution. Feel free to use them liberally to improve code quality and documentation.
