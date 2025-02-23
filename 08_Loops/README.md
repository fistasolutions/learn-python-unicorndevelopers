# 🚀 Lesson: Loops in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **loops** are and why they are important.  
✅ Learn how to **use for loops and while loops** effectively in Python.  
✅ Develop a **real-world mini-project** using loops.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Multiplication Table Generator  
🛠 **What we will build:** A program that prints multiplication tables for any number.  
📌 **Why?** To practice loops and iteration in Python.  
🔥 **Skills Gained:** Repetition handling, number manipulation, and formatted output.  

📷 **Suggested Image for Project:** *A notebook page with multiplication tables written in a structured manner.*  

---

## 🔍 Understanding Loops with Simple Examples  

### 🧐 What are Loops?  
Imagine you're **practicing basketball shots** 🎯. Instead of shooting just once, you repeat it **multiple times** until you get better.  

In Python, loops allow a program to **repeat a task** multiple times **without writing the same code again and again**.  

📷 **Suggested Image for Explanation:** *A child practicing basketball shots repeatedly.*  

---

### 🔢 Types of Loops in Python  

📌 **1. The `for` Loop**  

```python
for i in range(5):
    print("Hello, world!")
```  
📌 **2. The `while` Loop**  

```python
x = 1
while x <= 5:
    print(f"Number: {x}")
    x += 1
```  

📌 **3. Looping Through Lists**  

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```  

📌 **4. The `break` Statement** (Stop the loop early)  

```python
for num in range(10):
    if num == 5:
        break  # Stop when num reaches 5
    print(num)
```  

📌 **5. The `continue` Statement** (Skip an iteration)  

```python
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```  

---

## 🏗 Project: Multiplication Table Generator  

```python
# Multiplication Table Generator

num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```  

📷 **Suggested Image for Project Steps:** *A multiplication table being printed step by step.*  

💡 **Try modifying the program** to allow the user to generate tables for multiple numbers!  

---

## ✅ Summary of Loops  
✔ **Loops** allow us to **repeat tasks** efficiently.  
✔ Python has **for loops** (for iterating over sequences) and **while loops** (for conditional repetition).  
✔ They are used in **automation, gaming, data processing, and AI training**.  

### 🎯 **Mini-Challenge:**  
Write a program that prints the **first 10 numbers in the Fibonacci sequence**!  

⏭ **Next Lesson:** Functions in Python! 🚀  
