# 🔒 Encapsulation in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **encapsulation** is in Python.  
✅ Learn how to **protect data** using private and protected attributes.  
✅ Implement **getter and setter methods**.  
✅ Develop a **real-world mini-project** demonstrating encapsulation.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Bank Account System  
🛠 **What we will build:** A secure bank account system that hides sensitive data.  
📌 **Why?** Learn how encapsulation protects important information.  
🔥 **Skills Gained:** Data security, class design, encapsulation principles.  

📷 **Suggested Image for Project:** *A vault representing data protection.*  

---

## 🔍 Understanding Encapsulation  

Encapsulation is the technique of **hiding the internal details** of an object and restricting direct access to it.

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

📷 **Suggested Image:** *A lock icon protecting data inside a bank system.*  

---

## ✅ Summary of Encapsulation  
✔ **Encapsulation** hides sensitive data.  
✔ **Private attributes** (`__var`) prevent direct access.  
✔ **Getter and Setter methods** control how data is accessed.  

⏭ **Next Lesson:** Inheritance 🚀  
