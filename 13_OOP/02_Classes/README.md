# 🚀 Lesson: Object-Oriented Programming (OOP) - Classes in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **OOP and Classes** are and why they are important.  
✅ Learn how to **create classes, objects, and constructors** in Python.  
✅ Develop a **real-world mini-project** using OOP concepts.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Library Management System  
🛠 **What we will build:** A program to manage books using classes and objects.  
📌 **Why?** To understand **encapsulation, constructors, and object interactions**.  
🔥 **Skills Gained:** OOP fundamentals, class-based design, and data management.  

📷 **Suggested Image for Project:** *A digital bookshelf with books categorized by author and title.*  

---

## 🔍 Understanding OOP with Simple Examples  

### 🧐 What is Object-Oriented Programming?  
Think of a **car factory** 🚗🏭.  
- A **Car Blueprint (Class)** defines the structure (color, model, speed).  
- Each **Car (Object)** is a real instance of that blueprint.  

Similarly, in Python, a **Class** is a blueprint, and **Objects** are real instances created from it.  

📷 **Suggested Image for Explanation:** *A blueprint of a car vs. an actual car.*  

---

### 🔢 OOP Concepts in Python  

📌 **1. Defining a Class and Creating an Object**  

```python
# Creating a simple class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        return f"This car is a {self.color} {self.brand}."

# Creating an object of Car class
my_car = Car("Toyota", "Red")
print(my_car.describe())  # Output: This car is a Red Toyota.
```  

📌 **2. The `__init__` Constructor (Initializer Method)**  

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating objects
person1 = Person("Alice", 25)
print(person1.greet())
```  

📌 **3. Instance and Class Variables**  

```python
class Dog:
    species = "Canine"  # Class variable (shared among all objects)

    def __init__(self, name, breed):
        self.name = name  # Instance variable (unique to each object)
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.species)  # Output: Canine
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max
```  

📌 **4. Encapsulation (Hiding Data Using Private Variables)**  

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Creating an account
account = BankAccount("John", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```  

📌 **5. Inheritance (Reusing Code from a Parent Class)**  

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Woof! Woof!
```  

📌 **6. Polymorphism (Different Classes, Same Method Name)**  

```python
class Bird:
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

bird = Bird()
penguin = Penguin()

print(bird.fly())  # Output: Birds can fly
print(penguin.fly())  # Output: Penguins cannot fly
```  

---

## 🏗 Project: Library Management System (Using OOP)  

```python
# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"📖 {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book added: {book.get_info()}")

    def show_books(self):
        if not self.books:
            print("📭 No books available!")
        else:
            print("📚 Available Books:")
            for book in self.books:
                print(book.get_info())

# Main Program
library = Library()

while True:
    print("\n📖 Library Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = Book(title, author)
        library.add_book(book)
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
```  

📷 **Suggested Image for Project Steps:** *A list of books being displayed on a console screen.*  

💡 **Try modifying the program** to allow **removing books from the library!**  

---

## ✅ Summary of OOP - Classes  
✔ **Classes** are blueprints for creating objects.  
✔ **Objects** are instances of a class.  
✔ **Encapsulation, Inheritance, and Polymorphism** are key OOP principles.  
✔ **Constructors (`__init__`) initialize object attributes.**  

### 🎯 **Mini-Challenge:**  
Modify the library system to include **categories** and allow searching books by author!  

⏭ **Next Lesson:** Advanced OOP Concepts - Inheritance & Polymorphism! 🚀  
