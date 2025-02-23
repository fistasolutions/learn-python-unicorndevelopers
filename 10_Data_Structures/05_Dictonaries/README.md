# 🚀 Lesson: Dictionaries in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **dictionaries** are and why they are useful.  
✅ Learn how to **create, modify, and use dictionaries** in Python.  
✅ Develop a **real-world mini-project** using dictionaries.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Contact List Manager  
🛠 **What we will build:** A simple phonebook using dictionaries to store names and phone numbers.  
📌 **Why?** To understand the importance of **key-value pairs in storing and retrieving data efficiently**.  
🔥 **Skills Gained:** Data organization, quick lookups, dictionary operations.  

📷 **Suggested Image for Project:** *A contact book interface with names and numbers listed.*  

---

## 🔍 Understanding Dictionaries with Simple Examples  

### 🧐 What are Dictionaries?  
Imagine you have a **real-world dictionary** 📖. You look up a **word (key)** to find its **definition (value)**.  
A **Python dictionary** works the same way: it stores **key-value pairs**!  

📷 **Suggested Image for Explanation:** *An open dictionary book showing words and their definitions.*  

---

### 🔢 Creating and Using Dictionaries  

📌 **1. Creating a Dictionary**  

```python
# Creating a dictionary of countries and their capitals
capitals = {
    "Pakistan": "Islamabad",
    "France": "Paris",
    "Japan": "Tokyo"
}

print(capitals)
```  

📌 **2. Accessing Values by Key**  

```python
print(capitals["Pakistan"])  # Output: Islamabad
```  

📌 **3. Adding and Updating Entries**  

```python
capitals["Germany"] = "Berlin"  # Adding a new key-value pair
capitals["France"] = "Marseille"  # Updating an existing value
print(capitals)
```  

📌 **4. Removing Entries**  

```python
del capitals["Japan"]  # Removing a key-value pair
print(capitals)
```  

📌 **5. Looping Through a Dictionary**  

```python
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
```  

📌 **6. Checking If a Key Exists**  

```python
if "Pakistan" in capitals:
    print("Pakistan is in the dictionary!")
```  

---

## 🏗 Project: Contact List Manager  

```python
# Simple contact book using dictionaries

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"✅ Contact {name} added successfully!")

def show_contacts():
    print("📌 Contact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Adding contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")

# Displaying contacts
show_contacts()
```  

📷 **Suggested Image for Project Steps:** *A phonebook with names and numbers listed.*  

💡 **Try modifying the program** to allow searching for a contact by name!  

---

## ✅ Summary of Dictionaries  
✔ **Dictionaries** store data as **key-value pairs**.  
✔ They allow **fast lookups** and are **mutable**.  
✔ Used in **data storage, API responses, and structured data representation**.  

### 🎯 **Mini-Challenge:**  
Create a dictionary of **your favorite programming languages and their creators**, then print it!  

⏭ **Next Lesson:** Working with Python Files! 🚀  
