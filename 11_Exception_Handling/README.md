# 🚀 Lesson: Exception Handling in Python  

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **exceptions** are and why they occur.  
✅ Learn how to **handle errors gracefully** using try-except blocks.  
✅ Develop a **real-world mini-project** demonstrating exception handling.  
✅ Strengthen your understanding with **clear explanations and analogies**.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Smart Calculator with Error Handling  
🛠 **What we will build:** A simple calculator that prevents crashes by handling user input errors.  
📌 **Why?** To understand the importance of handling errors in real-world applications.  
🔥 **Skills Gained:** Debugging, error prevention, input validation.  

📷 **Suggested Image for Project:** *A calculator with a warning/error message displayed.*  

---

## 🔍 Understanding Exception Handling with Simple Examples  

### 🧐 What are Exceptions?  
Imagine you're riding a bicycle 🚴, and suddenly a rock appears on the road.  
If you **ignore it**, you'll crash! But if you **slow down or steer around it**, you continue safely.  
In Python, exceptions are like rocks in your code. Exception handling helps your program **avoid crashing**.  

📷 **Suggested Image for Explanation:** *A cyclist avoiding an obstacle on the road.*  

---

### 🔢 Handling Exceptions in Python  

📌 **1. Basic Try-Except Block**  

```python
try:
    number = int(input("Enter a number: "))  # User might enter text instead of a number
    print(f"You entered: {number}")
except ValueError:
    print("❌ Error: Please enter a valid number!")
```  

📌 **2. Handling Multiple Exceptions**  

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2  # May raise ZeroDivisionError
    print(f"Result: {result}")
except ValueError:
    print("❌ Error: Please enter valid numbers!")
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")
```  

📌 **3. Using Finally for Cleanup**  

```python
try:
    file = open("sample.txt", "r")  # File might not exist
    content = file.read()
    print(content)
except FileNotFoundError:
    print("❌ Error: File not found!")
finally:
    print("✅ Closing file (if it was opened).")
```  

📌 **4. Raising Custom Exceptions**  

```python
def check_age(age):
    if age < 18:
        raise ValueError("❌ Error: Age must be 18 or above!")
    return "✅ Access granted!"

try:
    print(check_age(15))
except ValueError as e:
    print(e)
```  

---

## 🏗 Project: Smart Calculator with Error Handling  

```python
# Smart calculator with exception handling

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"Result: {num1 + num2}")
        elif operator == "-":
            print(f"Result: {num1 - num2}")
        elif operator == "*":
            print(f"Result: {num1 * num2}")
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            print(f"Result: {num1 / num2}")
        else:
            print("❌ Error: Invalid operator!")

    except ValueError:
        print("❌ Error: Please enter valid numbers!")
    except ZeroDivisionError as e:
        print(f"❌ {e}")
    finally:
        print("✅ Calculation complete!")

# Run the calculator
calculator()
```  

📷 **Suggested Image for Project Steps:** *A calculator app with user-friendly error messages.*  

💡 **Try modifying the program** to handle more operations and invalid inputs!  

---

## ✅ Summary of Exception Handling  
✔ **Exceptions** help prevent program crashes.  
✔ Use **try-except** blocks to catch errors.  
✔ The **finally** block is used for cleanup tasks.  
✔ Raising **custom exceptions** improves error handling.  

### 🎯 **Mini-Challenge:**  
Modify the calculator to support **power (**) and modulus (%) operations**, with proper exception handling!  

⏭ **Next Lesson:** Working with File Handling! 🚀  
