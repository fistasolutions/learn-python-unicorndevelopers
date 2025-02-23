# 🏛 Inheritance in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **inheritance** is in Python.  
✅ Learn about **single, multiple, multilevel, and hierarchical inheritance**.  
✅ Implement **real-world examples** of inheritance.  
✅ Develop a **real-world mini-project** using inheritance.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Employee Management System  
🛠 **What we will build:** A system where different employee types inherit common properties.  
📌 **Why?** Understand how inheritance reduces code duplication.  
🔥 **Skills Gained:** OOP principles, class hierarchy, code reusability.  

📷 **Suggested Image for Project:** *An organization chart showing inheritance hierarchy.*  

---

## 🔍 Understanding Inheritance  

Inheritance allows a class to **reuse the attributes and methods** of another class.  

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Single Inheritance
    def speak(self):
        return "Bark!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Bark!
```

📷 **Suggested Image:** *A family tree showing class inheritance.*  

---

## ✅ Summary of Inheritance  
✔ **Inheritance** promotes code reusability.  
✔ **Different types**: Single, Multiple, Multilevel, Hierarchical.  

⏭ **Next Lesson:** Abstraction 🚀  
