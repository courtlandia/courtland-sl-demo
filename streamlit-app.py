# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Set app title
st.title('Interactive Scatter Plot with Streamlit and Altair')

# Add slider
num_points = st.slider('Number of points in scatter plot', 50, 1000, 500)

# Generate a DataFrame of random data
data = pd.DataFrame({
  'x': np.random.randn(num_points),
  'y': np.random.randn(num_points),
  'size': np.random.randint(10, 50, num_points),
  'color': np.random.randint(0, 20, num_points),
})

# Create scatter plot
scatter_plot = alt.Chart(data).mark_circle().encode(
  x='x',
  y='y',
  size='size',
  color='color',
  tooltip=['x', 'y', 'size', 'color']
).interactive()

# Display scatter plot in Streamlit app
st.altair_chart(scatter_plot, use_container_width=True)
