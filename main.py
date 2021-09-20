import streamlit as st

import numpy as np
import pandas as pd

st.title('Data visualization for Health and Welfare Statistics')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [34.63319466971191, 133.81113231175243],
    columns=['lat', 'lon'])

st.map(map_data)


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Now, for something completely different...")

expander = st.expander("Comment")
expander.write("Here you could put in some really, really long explanations...")


#copyright
st.write('Copyright © 2021 Brave Bioinformatics')