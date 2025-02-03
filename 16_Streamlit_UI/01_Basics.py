# Streamlit Comprehensive Guide

# ===========================
# Chapter 1: Basics
# ===========================
# Importing Streamlit
# `import streamlit as st` is importing the Streamlit library and aliasing it as `st`. This allows you
# to use the functions and features of the Streamlit library by prefixing them with `st`, making the
# code more readable and concise.
import streamlit as st

# Title and Text
st.title("Welcome to Class")
st.write("Streamlit makes building web apps super easy and fast.")

# Sidebar Example
st.sidebar.title("Sidebar Example")
st.sidebar.write("This is a sidebar")

# Input Widgets
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Slider Example
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")

