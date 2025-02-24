# 🚀 Python Lessons: Variables, Data Types & Input Function  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **variables, data types, and input function** are.  
✅ Learn how to **store, manipulate, and collect user input** in Python.  
✅ Develop **real-world mini-projects** using these concepts.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

# 🏗 Lesson 1: Variables in Python  

## 🔍 Understanding Variables with Simple Examples  

### 🧐 What are Variables?  
Imagine a **labeled storage box** 📦 where you store different items.  
In Python, a **variable** is like that box—it holds a value that we can use later.  

📷 **Suggested Image for Explanation:** *A shelf with labeled boxes representing different variables like `name`, `age`, and `salary`.*  

### 🔢 Key Concepts of Variables  

📌 **Creating a Variable**  

```python
name = "Alice"  # Storing a string
age = 12        # Storing a number
height = 4.9    # Storing a decimal number
```

📌 **Using Variables in Calculations**  

```python
price = 100
tax = 0.08 * price  # 8% tax
total = price + tax
print("Total price:", total)
```

---

## 🏗 Project 1: Simple Expense Tracker  

```python
food = 500
transport = 300
entertainment = 200

total_expense = food + transport + entertainment
print("Today's Total Expense:", total_expense)
```

📷 **Suggested Image for Project Steps:** *A budget chart showing expenses broken into categories.*  

💡 **Try modifying the program** to include `savings` and subtract it from the total.  

---

# 🏗 Lesson 2: Data Types in Python  

## 🔍 Understanding Data Types  

### 🧐 What are Data Types?  
Think of different types of **containers** 🍶🥤🍜:  
- A **cup** for liquids → Strings (`"hello"`)  
- A **box** for books → Integers (`10`)  
- A **measuring jar** for precise amounts → Floats (`4.5`)  
- A **checklist** for items → Lists (`[1,2,3]`)  

📷 **Suggested Image for Explanation:** *Different containers labeled as data types (cup = string, box = integer, etc.).*  

### 🔢 Key Concepts of Data Types  

📌 **Basic Data Types**  

```python
name = "Alice"   # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean
```

📌 **Checking Data Types**  

```python
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(height)) # Output: <class 'float'>
```

📌 **Type Conversion**  

```python
age = "25"
age = int(age)  # Converts string to integer
```

---

## 🏗 Project 2: Convert Temperature  

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

📷 **Suggested Image for Project Steps:** *A thermometer showing Celsius to Fahrenheit conversion.*  

💡 **Try modifying the program** to convert Fahrenheit to Celsius!  

---

# 🏗 Lesson 3: Input Function in Python  

## 🔍 Understanding Input Function  

### 🧐 What is the Input Function?  
Imagine a **chatbot asking your name** 🤖:  
- You type your name → The chatbot stores it in a variable.  
- The chatbot responds using your input.  

📷 **Suggested Image for Explanation:** *A chatbot taking user input and responding.*  

### 🔢 Using `input()`  

📌 **Basic Input Usage**  

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

📌 **Taking Numeric Input**  

```python
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)
```

---

## 🏗 Project 3: Simple User Greeting  

```python
name = input("What's your name? ")
age = input("How old are you? ")

print("Hello " + name + "! You are " + age + " years old.")
```

📷 **Suggested Image for Project Steps:** *A friendly chatbot greeting the user after input.*  

💡 **Try modifying the program** to ask more questions and store more details!  

---

## ✅ Summary of Lessons  
✔ **Variables** store values like numbers, text, or decimals.  
✔ **Data types** define what kind of data a variable can hold.  
✔ **Input function** allows user interaction in programs.  

### 🎯 **Mini-Challenge:**  
Write a program that takes a **name, age, and favorite color** as input and prints a fun sentence using these values!  

⏭ **Next Lesson:** Conditional Statements in Python! 🚀  
