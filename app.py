import streamlit as st
import pandas as pd
from enemies.humanoid import humanoid

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('add bandit')

with col2:
    button2 = st.button('add orc')

with col3:
    button3 = st.button('Button 3')

if button1:
    e1 = humanoid.bandit().to_dict()
    e1 = pd.DataFrame([e1])
    st.session_state['data'] = pd.concat([st.session_state['data'], e1], ignore_index=True)

if button2:
    e1 = humanoid.orc().to_dict()
    e1 = pd.DataFrame([e1])
    st.session_state['data'] = pd.concat([st.session_state['data'], e1], ignore_index=True)

st.data_editor(st.session_state['data'])
# st.write(st.session_state)
