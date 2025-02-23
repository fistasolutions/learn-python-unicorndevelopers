# 🚀 Lesson: Functions in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **functions** are and why they are important.  
✅ Learn how to **define and use functions** effectively in Python.  
✅ Develop a **real-world mini-project** using functions.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Simple Calculator using Functions  
🛠 **What we will build:** A calculator that performs addition, subtraction, multiplication, and division using functions.  
📌 **Why?** To practice defining and calling functions for reusable code.  
🔥 **Skills Gained:** Function design, parameter handling, and user input processing.  

📷 **Suggested Image for Project:** *A calculator with function blocks representing operations like add, subtract, multiply, and divide.*  

---

## 🔍 Understanding Functions with Simple Examples  

### 🧐 What are Functions?  
Imagine you're making **tea** 🍵. Instead of remembering every step each time, you can **write down a recipe** and follow it.  

A **function** in Python is like a **recipe**—you define it once and use it whenever needed!  

📷 **Suggested Image for Explanation:** *A recipe book with reusable steps for making tea.*  

---

### 🔢 Defining and Using Functions  

📌 **1. Defining a Function**  

```python
def greet():
    print("Hello, world!")

greet()  # Calling the function
```  

📌 **2. Functions with Parameters**  

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```  

📌 **3. Returning Values from Functions**  

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(f"Sum: {result}")
```  

📌 **4. Default Parameter Values**  

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       # Uses default value
greet("John") # Uses provided value
```  

📌 **5. Using Functions Inside Functions**  

```python
def multiply(a, b):
    return a * b

def square(n):
    return multiply(n, n)

print(square(4))  # 16
```  

---

## 🏗 Project: Simple Calculator  

```python
# Simple Calculator using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Operations: +, -, *, /")
operation = input("Choose an operation: ")

if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "*":
    print("Result:", multiply(num1, num2))
elif operation == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation!")
```  

📷 **Suggested Image for Project Steps:** *A simple calculator UI showing function calls for each operation.*  

💡 **Try modifying the program** to add more operations like exponentiation!  

---

## ✅ Summary of Functions  
✔ **Functions** allow us to **reuse code efficiently**.  
✔ Python functions can **take parameters**, **return values**, and **have default values**.  
✔ They are used in **data processing, automation, game development, and web applications**.  

### 🎯 **Mini-Challenge:**  
Write a function that **checks if a number is even or odd**!  

⏭ **Next Lesson:** File Handling in Python! 🚀  
