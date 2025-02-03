# ===========================
# Chapter 3: Interactivity
# ===========================
import streamlit as st

# Checkbox Example
if st.checkbox("Show Secret Message"):
    st.write("🎉 You found the secret!")

# Button Example
if st.button("Click Me"):
    st.write("Button clicked!")

# Selectbox Example
option = st.selectbox(
    "Choose a number:",
    [1, 2, 3, 4, 5]
)
st.write(f"You selected {option}")
