# 🚀 Lesson: Operators in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **operators** are and why they are essential in Python.  
✅ Learn how to **perform different operations** using various types of operators.  
✅ Develop a **real-world mini-project** that applies operators.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Simple Calculator  
🛠 **What we will build:** A calculator that performs basic arithmetic operations.  
📌 **Why?** To apply different types of operators in a real-world scenario.  
🔥 **Skills Gained:** Arithmetic operations, user input handling, and decision-making.  

📷 **Suggested Image for Project:** *An interactive calculator interface displaying results dynamically.*  

---

## 🔍 Understanding Operators with Simple Examples  

### 🧐 What are Operators?  
Think of operators like **tools in a toolbox** 🛠️. Each tool (operator) has a special job:  

- **Arithmetic Operators** ➝ Add, subtract, multiply, and divide numbers.  
- **Comparison Operators** ➝ Compare two values (like checking if two things are equal).  
- **Logical Operators** ➝ Combine conditions (like asking if both conditions are true).  

📷 **Suggested Image for Explanation:** *A toolbox with different tools labeled as different operators (e.g., +, -, *, /).*  

### 🔢 Key Types of Operators  

📌 **1. Arithmetic Operators**  

```python
a = 10
b = 3

print(a + b)  # Addition -> 13
print(a - b)  # Subtraction -> 7
print(a * b)  # Multiplication -> 30
print(a / b)  # Division -> 3.33
print(a // b) # Floor Division -> 3
print(a % b)  # Modulus (Remainder) -> 1
print(a ** b) # Exponentiation -> 1000
```  

📌 **2. Comparison Operators**  

```python
x = 5
y = 10

print(x == y)  # False (Is x equal to y?)
print(x != y)  # True  (Is x NOT equal to y?)
print(x > y)   # False (Is x greater than y?)
print(x < y)   # True  (Is x less than y?)
print(x >= y)  # False (Is x greater than or equal to y?)
print(x <= y)  # True  (Is x less than or equal to y?)
```  

📌 **3. Logical Operators**  

```python
a = True
b = False

print(a and b)  # False (Both must be true)
print(a or b)   # True  (At least one must be true)
print(not a)    # False (Reverses the condition)
```  

📌 **4. Assignment Operators**  

```python
x = 10
x += 5  # Same as x = x + 5
x -= 2  # Same as x = x - 2
x *= 3  # Same as x = x * 3
x /= 2  # Same as x = x / 2

print(x)  # Result after applying operators step by step
```  

📌 **5. Membership & Identity Operators**  

```python
list1 = [1, 2, 3, 4]
print(3 in list1)   # True (Is 3 present in the list?)
print(5 not in list1)  # True (Is 5 NOT in the list?)

a = [10, 20, 30]
b = a

print(a is b)   # True (Both point to the same object)
print(a == b)   # True (Both have the same values)
```  

---

## 🏗 Project: Simple Calculator  

```python
# Simple Calculator Using Operators

num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
else:
    result = "Invalid Operator!"

print(f"Result: {result}")
```  

📷 **Suggested Image for Project Steps:** *A simple user interface where a user enters numbers and selects an operator.*  

💡 **Try modifying the program** to include **exponentiation (**) and floor division (//).**  

---

## ✅ Summary of Operators  
✔ Operators help us perform **mathematical and logical** operations.  
✔ Different types of operators include **Arithmetic, Comparison, Logical, Assignment, Membership, and Identity Operators**.  
✔ Operators are fundamental in programming and appear in **almost every Python program**.  

### 🎯 **Mini-Challenge:**  
Write a program that asks the user for **two numbers** and checks if the first number is greater, smaller, or equal to the second number!  

⏭ **Next Lesson:** Conditional Statements in Python! 🚀  
