# 🚀 Lesson: File Handling in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **file handling** is and why it is important.  
✅ Learn how to **read, write, and append** data to files in Python.  
✅ Develop a **real-world mini-project** using file handling.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** To-Do List with File Storage  
🛠 **What we will build:** A program that allows users to add tasks, view tasks, and save them persistently.  
📌 **Why?** To understand how to store and retrieve data using files.  
🔥 **Skills Gained:** File operations, data persistence, input handling.  

📷 **Suggested Image for Project:** *A digital notepad with tasks listed.*  

---

## 🔍 Understanding File Handling with Simple Examples  

### 🧐 What is File Handling?  
Imagine writing your daily tasks in a **notebook** 📖. Even if you close it, your notes stay there when you open it again.  
In the same way, Python allows us to **save data in files**, so our programs remember information even after closing.  

📷 **Suggested Image for Explanation:** *A notebook with written tasks.*  

---

### 🔢 File Handling in Python  

📌 **1. Writing to a File**  

```python
# Open file in write mode ('w')
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first file write!")
print("✅ File written successfully!")
```  

📌 **2. Reading from a File**  

```python
# Open file in read mode ('r')
with open("notes.txt", "r") as file:
    content = file.read()
    print("📖 File Content:")
    print(content)
```  

📌 **3. Appending to a File**  

```python
# Open file in append mode ('a')
with open("notes.txt", "a") as file:
    file.write("\nAdding another line!")
print("✅ Text appended successfully!")
```  

📌 **4. Handling File Errors (Try-Except)**  

```python
try:
    with open("unknown.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ Error: File not found!")
```  

---

## 🏗 Project: To-Do List with File Storage  

```python
# To-Do List with File Handling

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added!")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("📌 Your Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("📭 No tasks found!")
    except FileNotFoundError:
        print("❌ No tasks file found!")

# Main Program
while True:
    print("\n📝 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
```  

📷 **Suggested Image for Project Steps:** *A console-based to-do list in action.*  

💡 **Try modifying the program** to allow **task deletion or editing!**  

---

## ✅ Summary of File Handling  
✔ **File Handling** allows data to persist even after program execution.  
✔ Use **write ('w')**, **read ('r')**, and **append ('a')** modes.  
✔ **Error handling** prevents program crashes.  

### 🎯 **Mini-Challenge:**  
Modify the to-do list to **mark tasks as completed** by storing them separately!  

⏭ **Next Lesson:** Working with Modules in Python! 🚀  
