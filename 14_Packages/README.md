# 📦 Python Packages: Built-in, Custom, and External

## 🎯 Learning Objectives (OBE)  
By the end of this lesson, you will:  
✅ Understand what **packages** are in Python and why they are useful.  
✅ Learn how to use **built-in packages** effectively.  
✅ Create **custom packages** for modular programming.  
✅ Work with **external packages** using pip.  
✅ Develop a **real-world mini-project** using Python packages.  

---

## 🏗 Project for This Topic (PBL)  
📌 **Project:** Build a Weather Data Analyzer  
🛠 **What we will build:** A Python program that fetches and processes weather data using external packages.  
📌 **Why?** Learn how to integrate and manage multiple packages in a real-world application.  
🔥 **Skills Gained:** Package management, API integration, data analysis.  

📷 **Suggested Image for Project:** *A visual representation of a weather app fetching and displaying weather data.*  

---

## 🔍 Understanding Python Packages

### 🧐 What is a Package?  
A package is a collection of Python modules organized in directories containing a special `__init__.py` file. It helps in organizing and reusing code efficiently.

📷 **Suggested Image for Explanation:** *A folder icon with multiple Python files inside, representing a package structure.*  

### 📌 Built-in Python Packages  
Python comes with several built-in packages to make coding easier. Some common ones include:

```python
import math
print(math.sqrt(25))  # Output: 5.0

import datetime
print(datetime.datetime.now())  # Current date and time
```

### 📌 Creating Custom Packages  
To create a custom package:  

1️⃣ Make a directory and add a `__init__.py` file.  
2️⃣ Add modules (Python files) inside the directory.  
3️⃣ Import the package into other scripts.  

Example:  
**Directory Structure:**  
```
my_package/
    __init__.py
    module1.py
    module2.py
```

`module1.py`:  
```python
def greet(name):
    return f"Hello, {name}!"
```

Usage:  
```python
from my_package import module1
print(module1.greet("Alice"))  # Output: Hello, Alice!
```

### 📌 Working with External Packages  
Python has a vast ecosystem of third-party packages that can be installed using pip.

**Installing an external package:**  
```bash
pip install requests
```

**Using an external package (requests example):**  
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
```

📷 **Suggested Image for External Packages:** *A Python logo with a package icon and a pip command being executed.*  

---

## 🚀 Project Implementation (Hands-on Practice)  
Step-by-step guide to building a **Weather Data Analyzer** using external packages.  
```python
import requests

API_URL = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London"
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    print(f"Temperature in London: {data['current']['temp_c']}°C")
else:
    print("Failed to retrieve data.")
```

📷 **Suggested Image for Project Steps:** *A screenshot of weather data being printed in a terminal.*  

💡 Try modifying the code to accept different cities as user input!  

---

## ✅ Summary of Python Packages  
✔ **Packages** help organize and reuse code.  
✔ **Built-in packages** provide essential functionalities.  
✔ **Custom packages** allow modular programming.  
✔ **External packages** extend Python's capabilities.  

🎯 **Challenge:** Try creating a package with multiple modules for a personal project.  

⏭ **Next Lesson:** Exploring Python Virtual Environments 🚀  
