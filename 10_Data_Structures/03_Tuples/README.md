# 🚀 Lesson: Tuples in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **tuples** are and how they differ from lists.  
✅ Learn how to **create, access, and use tuples** effectively in Python.  
✅ Develop a **real-world mini-project** using tuples.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Immutable Contact Book  
🛠 **What we will build:** A contact book that stores immutable contact details using tuples.  
📌 **Why?** To understand the importance of tuples in storing **fixed, unchangeable data**.  
🔥 **Skills Gained:** Data organization, tuple usage, and dictionary integration.  

📷 **Suggested Image for Project:** *A phonebook with fixed contact details (Name, Phone, Email).*  

---

## 🔍 Understanding Tuples with Simple Examples  

### 🧐 What are Tuples?  
Imagine you are designing **an ID card** 🎓. The information printed (Name, DOB, Blood Type) **cannot be changed** once printed.  
Similarly, **tuples** are like **frozen lists**—they store values **that should not change**.  

📷 **Suggested Image for Explanation:** *An ID card with details printed on it, showing immutability.*  

---

### 🔢 Creating and Using Tuples  

📌 **1. Creating a Tuple**  

```python
# Creating a tuple of colors
colors = ("Red", "Green", "Blue")
print(colors)
```  

📌 **2. Accessing Tuple Elements**  

```python
# Accessing items by index (starting from 0)
print(colors[0])  # Red
print(colors[1])  # Green
```  

📌 **3. Tuples are Immutable**  

```python
# This will cause an error because tuples cannot be modified
colors[1] = "Yellow"  # ❌ TypeError: 'tuple' object does not support item assignment
```  

📌 **4. Tuple Packing and Unpacking**  

```python
# Packing a tuple
person = ("Alice", 25, "Engineer")

# Unpacking a tuple
name, age, profession = person
print(name)       # Alice
print(age)        # 25
print(profession) # Engineer
```  

📌 **5. Tuple Methods**  

```python
# Count occurrences and find index
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))   # 3 (how many times 2 appears)
print(numbers.index(3))   # 2 (position of 3)
```  

---

## 🏗 Project: Immutable Contact Book  

```python
# Simple Contact Book using Tuples

contacts = (
    ("Alice", "alice@example.com", "123-456-7890"),
    ("Bob", "bob@example.com", "987-654-3210"),
    ("Charlie", "charlie@example.com", "456-789-0123")
)

def show_contacts():
    print("Contact List:")
    for name, email, phone in contacts:
        print(f"📌 Name: {name} | 📧 Email: {email} | 📞 Phone: {phone}")

# Display contacts
show_contacts()
```  

📷 **Suggested Image for Project Steps:** *A contact list displayed with tuple-based information.*  

💡 **Try modifying the program** to allow searching for a contact by name!  

---

## ✅ Summary of Tuples  
✔ **Tuples** store **immutable data** (cannot be changed).  
✔ They are used for **fixed collections like coordinates, database records, and settings**.  
✔ Tuples are **faster and more memory-efficient** than lists.  

### 🎯 **Mini-Challenge:**  
Create a tuple storing **the top 3 programming languages you like** and print them!  

⏭ **Next Lesson:** Dictionaries in Python! 🚀  
