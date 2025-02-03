
# ===========================
# Chapter 2: Data Visualization
# ===========================

# Importing Necessary Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# DataFrame Display
st.write("### DataFrame Example")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['Column A', 'Column B', 'Column C']
)
st.dataframe(data)

# Matplotlib Chart
st.write("### Matplotlib Example")
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label="Sine Wave")
ax.legend()
st.pyplot(fig)

# Plotly Chart
st.write("### Plotly Example")
plotly_fig = px.scatter(data, x="Column A", y="Column B")
st.plotly_chart(plotly_fig)

