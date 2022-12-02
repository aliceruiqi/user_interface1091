import pandas as pd
import streamlit as st
import numpy as np
import random

st.markdown("""
            # This is a title
            ## this is a subtitle
            this is a text
            - this is a list
            """)

df = pd.DataFrame({
    'first column': random.randint(1,10),
    'second column': np.arange(10, 101, 10)
})

line_count = st.slider('Select a line count', 1, 10, 3)

st.write(df.head(line_count))
