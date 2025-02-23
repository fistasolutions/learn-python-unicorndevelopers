# 🚀 Lesson: Lists in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **lists** are and why they are useful.  
✅ Learn how to **create, modify, and manipulate lists** in Python.  
✅ Develop a **real-world mini-project** using lists.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Task Manager using Lists  
🛠 **What we will build:** A simple to-do list program that allows users to add, remove, and display tasks.  
📌 **Why?** To understand how lists help in storing and managing collections of items dynamically.  
🔥 **Skills Gained:** List operations, user interaction, and basic CRUD functionality.  

📷 **Suggested Image for Project:** *A checklist with tasks being added and removed dynamically.*  

---

## 🔍 Understanding Lists with Simple Examples  

### 🧐 What are Lists?  
Imagine you have a **grocery list** 🛒. Instead of remembering all the items in your head, you **write them down in a list**.  

A **list** in Python is like a grocery list—it helps you **store multiple items together** and access them easily.  

📷 **Suggested Image for Explanation:** *A grocery list with items like "Milk, Bread, Eggs" stored in a notebook.*  

---

### 🔢 Creating and Using Lists  

📌 **1. Creating a List**  

```python
# Creating a list of fruits
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
```  

📌 **2. Accessing List Elements**  

```python
# Accessing items by index (starting from 0)
print(fruits[0])  # Apple
print(fruits[1])  # Banana
```  

📌 **3. Modifying List Elements**  

```python
# Changing an item in the list
fruits[1] = "Blueberry"
print(fruits)  # ['Apple', 'Blueberry', 'Cherry']
```  

📌 **4. Adding Elements to a List**  

```python
# Using append() to add a new item
fruits.append("Orange")
print(fruits)  # ['Apple', 'Blueberry', 'Cherry', 'Orange']
```  

📌 **5. Removing Elements from a List**  

```python
# Using remove() to delete an item
fruits.remove("Cherry")
print(fruits)  # ['Apple', 'Blueberry', 'Orange']
```  

📌 **6. Iterating Through a List**  

```python
# Using a loop to print all elements
for fruit in fruits:
    print(fruit)
```  

📌 **7. List Slicing (Extracting Portions)**  

```python
# Getting a sublist
print(fruits[:2])  # ['Apple', 'Blueberry']
```  

---

## 🏗 Project: Task Manager  

```python
# Simple Task Manager using Lists

tasks = []  # Empty list to store tasks

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print("Task not found!")

def show_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# User interaction
while True:
    print("
Options: 1-Add Task, 2-Remove Task, 3-Show Tasks, 4-Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Exiting Task Manager.")
        break
    else:
        print("Invalid choice!")
```  

📷 **Suggested Image for Project Steps:** *A simple task list being updated dynamically.*  

💡 **Try modifying the program** to allow task priority levels!  

---

## ✅ Summary of Lists  
✔ **Lists** allow us to **store multiple values in a single variable**.  
✔ They support **modifications, indexing, and iteration**.  
✔ Lists are used in **data storage, user interfaces, and dynamic content management**.  

### 🎯 **Mini-Challenge:**  
Create a list of your **5 favorite movies** and print them in reverse order!  

⏭ **Next Lesson:** Tuples in Python! 🚀  
