import streamlit as st
# import pandas as pd
from enemies.humanoid import humanoid
# import utilities.df_utils as dfutils

st.title("Helden Initiative")

if 'data' not in st.session_state:
    # st.session_state['data'] = pd.DataFrame([humanoid.bandit().to_dict(), humanoid.bandit().to_dict()])
    st.session_state['data'] = [humanoid.bandit(), humanoid.bandit()]


if 'ini_idx' not in st.session_state:
    st.session_state['ini_idx'] = 0

if 'round' not in st.session_state:
    st.session_state['round'] = 1


with st.container(border=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        button1 = st.button('add bandit')

    with col2:
        button2 = st.button('add orc')

    with col3:
        button3 = st.button('Sort')

    with col4:
        button4 = st.button('Next')

ini_container = st.container(border=True)

if button1:
    st.session_state['data'].append(humanoid.bandit())

if button2:
    st.session_state['data'].append(humanoid.orc())

if button3:
    st.session_state['data'].sort(key=lambda x: x.ini, reverse=True)

with ini_container:
    for element in st.session_state['data']:
        # print(row)
        with st.container(border=True):
            col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
            with col1:
                st.text(element.name)
            with col2:
                st.text(element.ini)
            with col3:
                st.text(element.lep)        
            with col4:
                st.text(element.at)
            with col5:
                st.text(element.pa)
            with col6:
                st.text(element.wound_count)
            with col7:
                st.text(element.rs)


st.write(st.session_state)