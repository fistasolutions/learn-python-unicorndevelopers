# Hello World Program

## Writing Your First Python Program
The first program you typically write in any programming language is the "Hello, World!" program. It is a simple way to get started and ensure that your development environment is correctly set up.

### Steps to Write "Hello, World!"
1. Open your Python IDE (e.g., Visual Studio Code, Jupyter Notebook).
2. Create a new file or notebook.
3. Add the following line of code:

```python
print("Hello, World!")
```

4. Run the program to see the output.

### Output:
```
Hello, World!
```

---

## What is `print` in Python?
The `print()` function is used to output text or data to the console. It is one of the most commonly used functions in Python.

### Syntax:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Explanation:
- **`*objects`**: The values to be printed.
- **`sep`**: Separator between values (default is a space).
- **`end`**: What to print at the end (default is a newline `\n`).

### Examples:
```python
print("Hello, World!")
print("Python", "is", "fun", sep="-")
print("This is the end", end="!")
```

### Output:
```
Hello, World!
Python-is-fun
This is the end!
```

---

## How to Run a Python Program
### Running `.py` Files
1. Open a text editor or IDE.
2. Save your Python code in a file with a `.py` extension (e.g., `hello.py`).
3. Open a terminal or command prompt.
4. Navigate to the file's directory.
5. Run the program using the command:

```bash
python hello.py
```

### Running Code in Jupyter Notebook
1. Open Jupyter Notebook.
2. Create a new notebook or open an existing one.
3. Add your Python code in a cell.
4. Run the cell by pressing `Shift + Enter` or clicking the "Run" button.

---

## Difference Between `.py` and `.ipynb`
### `.py`
- Plain text file containing Python code.
- Can be executed in any Python interpreter or terminal.
- Ideal for scripting and larger projects.

### `.ipynb`
- Interactive file used in Jupyter Notebooks.
- Contains cells for both code and markdown (text).
- Ideal for data analysis, visualizations, and tutorials.

---

## Explanation of Jupyter Notebook
Jupyter Notebook is an open-source web application that allows you to create and share documents with live code, equations, visualizations, and narrative text.

### Key Features:
- Interactive coding environment.
- Supports multiple languages, including Python.
- Inline visualization with libraries like Matplotlib and Seaborn.

### Markdown Section in Jupyter Notebook
Markdown is used to write formatted text in Jupyter Notebook. Examples include headings, bullet points, and links.

#### Markdown Examples:
```markdown
# Heading Level 1
## Heading Level 2
**Bold Text**
*Italic Text*
- Bullet Point 1
- Bullet Point 2
```




### Running a Jupyter Notebook
1. Open Anaconda Navigator or run the command `jupyter notebook` in your terminal.
2. Navigate to the directory where you want to create a notebook.
3. Create a new notebook and start coding!
