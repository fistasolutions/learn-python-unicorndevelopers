# 🎭 Polymorphism in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **polymorphism** is in Python.  
✅ Learn how functions and methods can have **multiple behaviors**.  
✅ Implement **method overriding and operator overloading**.  
✅ Develop a **real-world mini-project** demonstrating polymorphism.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Shape Area Calculator  
🛠 **What we will build:** A system where different shapes implement their own area calculations.  
📌 **Why?** Understand how polymorphism allows multiple implementations.  
🔥 **Skills Gained:** OOP principles, dynamic method behavior.  

📷 **Suggested Image for Project:** *Different shapes (circle, square) using a common method differently.*  

---

## 🔍 Understanding Polymorphism  

Polymorphism allows the **same method to behave differently** based on the object calling it.  

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Bark! Meow!
```

📷 **Suggested Image:** *Different animals making different sounds using the same method.*  

---

## ✅ Summary of Polymorphism  
✔ **Polymorphism** allows multiple implementations of the same method.  
✔ **Method overriding** and **operator overloading** demonstrate polymorphism.  

⏭ **Next Lesson:** Python Packages 🚀  
