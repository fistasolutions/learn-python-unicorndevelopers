# 🚀 Lesson: Conditional Statements in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **conditional statements** are and why they are important.  
✅ Learn how to **use if, elif, and else** effectively in Python.  
✅ Develop a **real-world mini-project** using conditional statements.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Age-Based Movie Ticket Price Calculator  
🛠 **What we will build:** A program that calculates ticket prices based on age.  
📌 **Why?** To apply conditional statements in a real-world scenario.  
🔥 **Skills Gained:** Decision-making, user input handling, and logical operations.  

📷 **Suggested Image for Project:** *A movie ticket counter where different ticket prices are displayed based on age groups.*  

---

## 🔍 Understanding Conditional Statements with Simple Examples  

### 🧐 What are Conditional Statements?  
Imagine you're at an amusement park 🎢. If you're **taller than 4 feet**, you can go on the roller coaster. Otherwise, you cannot. This is a decision-making rule!  

In Python, **conditional statements** work the same way. They help the program make decisions based on conditions.  

📷 **Suggested Image for Explanation:** *A height-checking machine at an amusement park that determines whether a child can enter the ride.*  

---

### 🔢 Key Types of Conditional Statements  

📌 **1. The `if` Statement**  

```python
age = 18

if age >= 18:
    print("You are allowed to vote!")
```  

📌 **2. The `if-else` Statement**  

```python
age = 16

if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you are too young to vote.")
```  

📌 **3. The `if-elif-else` Statement**  

```python
age = 12

if age < 12:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
```  

📌 **4. Nested `if` Statements**  

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")
```  

📌 **5. Using Logical Operators in Conditions**  

```python
temp = 25

if temp > 30 or temp < 10:
    print("The weather is extreme!")
else:
    print("The weather is moderate.")
```  

---

## 🏗 Project: Age-Based Movie Ticket Price Calculator  

```python
# Movie Ticket Price Calculator

age = int(input("Enter your age: "))

if age < 5:
    price = 0  # Free ticket for toddlers
elif age < 18:
    price = 10  # Discounted price for children
elif age < 60:
    price = 15  # Standard price for adults
else:
    price = 12  # Discount for senior citizens

print(f"Your movie ticket price is: ${price}")
```  

📷 **Suggested Image for Project Steps:** *A movie theater pricing board showing different ticket rates for different age groups.*  

💡 **Try modifying the program** to offer **extra discounts** for students and veterans!  

---

## ✅ Summary of Conditional Statements  
✔ **Conditional statements** allow programs to make decisions.  
✔ Python uses **if, elif, and else** to control decision-making.  
✔ They are used in everyday applications like **login systems, recommendation engines, and automated responses**.  

### 🎯 **Mini-Challenge:**  
Write a program that checks if a number is **positive, negative, or zero**!  

⏭ **Next Lesson:** Loops in Python! 🚀  
