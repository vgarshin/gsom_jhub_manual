import streamlit as st
import pandas as pd
import numpy as np

# Source https://docs.streamlit.io/library/get-started/main-concepts

# Title of our demo app
st.title('Test application')

# Along with magic commands, st.write() is Streamlit's "Swiss Army knife". 
# You can pass almost anything to st.write(): text, data, Matplotlib figures, 
# Altair charts, and more.
# Let's start with Pandas dataframe and write it to Streamlit:
st.write("Here's demo table from the dataframe:")
fruits_data = pd.DataFrame(
    {
        'fruits': ['apple', 'peach', 'pineapple', 'watermelon'],
        'color': ['green', 'orange', 'yellow', 'stripes'],
        'weight': [1, 2, 5, 10]
    }
)
st.write(fruits_data)

# You can easily add a line chart to your app with st.line_chart(). 
# We'll generate a random sample using Numpy and then chart it:
st.write("Here's demo chart for fruits:")
chart_data = pd.DataFrame(
     np.random.randn(20, 4),
     columns=['apple', 'peach', 'pineapple', 'watermelon']
)
st.line_chart(chart_data)

# With st.map() you can display data points on a map. 
# Let's use Numpy to generate some sample data 
# and plot it on a map of Saint Petersburg:
st.write("Demo map:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [59.9386, 30.3141],
    columns=['lat', 'lon']
)
st.map(map_data)