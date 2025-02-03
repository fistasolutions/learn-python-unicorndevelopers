"""
Streamlit Overview and Detailed Guide

Streamlit is an open-source Python library that enables developers to create interactive, web-based applications for data visualization and machine learning models with minimal effort. It's simple, intuitive, and doesn't require extensive front-end coding knowledge.

This guide covers:
1. Introduction
2. Installation
3. Basics of Streamlit
4. Widgets and Interactions
5. Data Visualization
6. Advanced Streamlit Features
7. Deployment
"""

# 1. Introduction
# Streamlit allows users to turn data scripts into shareable web apps. It's particularly useful for creating dashboards and interactive tools.

# 2. Installation
# Install Streamlit using pip.
# ```bash
# pip install streamlit
# ```

# To run a Streamlit app, use the command:
# ```bash
# streamlit run your_script.py
# ```

# 3. Basics of Streamlit
import streamlit as st

# Title and text
def app_basics():
    st.title("Streamlit Basics")
    st.header("Introduction to Streamlit")
    st.text("Streamlit helps you build interactive web apps in Python easily.")

# Displaying Data
def display_data():
    st.header("Displaying Data")
    st.write("Streamlit automatically formats Python data structures:")
    sample_dict = {"Name": "Alice", "Age": 25, "Country": "USA"}
    st.write(sample_dict)

# Markdown Example
def markdown_example():
    st.header("Markdown Support")
    st.markdown("""
    **Markdown** allows *styling* of text with:
    - Bold
    - Italics
    - Lists
    """)

# 4. Widgets and Interactions
# Text Input and Buttons
def widgets_demo():
    st.header("Widgets")
    user_input = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.success(f"Hello, {user_input}!")

# Slider and Selectbox
def slider_and_select():
    st.header("Sliders and Dropdowns")
    age = st.slider("Select your age", 0, 100, 25)
    st.write(f"Selected age: {age}")

    options = ["Red", "Green", "Blue"]
    color = st.selectbox("Choose a color", options)
    st.write(f"You selected: {color}")

# 5. Data Visualization
import pandas as pd
import numpy as np

def data_visualization():
    st.header("Data Visualization")

    # Sample Data
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    # Line Chart
    st.line_chart(df)

    # Bar Chart
    st.bar_chart(df)

    # Map Visualization
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )
    st.map(map_data)

# 6. Advanced Streamlit Features
# File Uploader
def file_upload_demo():
    st.header("File Upload")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())

# Sidebar Widgets
def sidebar_demo():
    st.sidebar.title("Sidebar")
    st.sidebar.radio("Navigation", ["Home", "About"])

# 7. Deployment
# Streamlit apps can be deployed to cloud platforms like Streamlit Community Cloud, Heroku, AWS, or GCP.

# Bringing it all together
def main():
    st.sidebar.title("Streamlit Guide")
    pages = {
        "Basics": app_basics,
        "Displaying Data": display_data,
        "Markdown": markdown_example,
        "Widgets": widgets_demo,
        "Visualization": data_visualization,
        "File Upload": file_upload_demo,
        "Sidebar": sidebar_demo
    }

    choice = st.sidebar.selectbox("Choose a section", list(pages.keys()))
    pages[choice]()

if __name__ == "__main__":
    main()
