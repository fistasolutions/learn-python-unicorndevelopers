# 🎭 Abstraction in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **abstraction** is in Python.  
✅ Learn how to create **abstract classes and methods**.  
✅ Implement abstraction using the **ABC module**.  
✅ Develop a **real-world mini-project** demonstrating abstraction.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Payment Processing System  
🛠 **What we will build:** A system that defines a generic payment method using abstraction.  
📌 **Why?** Learn how abstraction enforces method implementation.  
🔥 **Skills Gained:** OOP principles, abstract class design.  

📷 **Suggested Image for Project:** *A generic payment method being implemented by different classes.*  

---

## 🔍 Understanding Abstraction  

Abstraction hides implementation details and **only shows essential features**.  

```python
from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract class
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):  
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

payment = CreditCardPayment()
payment.pay(100)  # Output: Paid 100 using Credit Card
```

📷 **Suggested Image:** *A template showing a structure that must be followed.*  

---

## ✅ Summary of Abstraction  
✔ **Abstraction** hides implementation details.  
✔ **Abstract classes** enforce method implementation.  

⏭ **Next Lesson:** Polymorphism 🚀  
