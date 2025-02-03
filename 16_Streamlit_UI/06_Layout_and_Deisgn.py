# ===========================
# Chapter 6: Layout and Design
# ===========================
import streamlit as st

# Using Columns
st.write("### Using Columns")
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Using Tabs
st.write("### Using Tabs")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content of Tab 1")

with tab2:
    st.write("Content of Tab 2")

# Using Containers
with st.container():
    st.write("This is inside a container")
    st.line_chart(np.random.randn(10, 2))
