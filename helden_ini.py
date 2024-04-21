import streamlit as st
# import pandas as pd
from enemies.humanoid import humanoid
# import utilities.df_utils as dfutils

st.set_page_config(layout="wide", page_title="Helden Initiative")
st.title("Helden Initiative")

if 'data' not in st.session_state:
    # st.session_state['data'] = pd.DataFrame([humanoid.bandit().to_dict(), humanoid.bandit().to_dict()])
    st.session_state['data'] = [humanoid.dummy()]


if 'ini_idx' not in st.session_state:
    st.session_state['ini_idx'] = 0

if 'round' not in st.session_state:
    st.session_state['round'] = 1


with st.container(border=True):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        button1 = st.button('add bandit')

    with col2:
        button2 = st.button('add orc')

    with col3:
        button3 = st.button('Sort')

    with col4:
        button4 = st.button('Next')
    
    with col5:
        button5 = st.button('Reset')

ini_container = st.container(border=True)

if button1:
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = humanoid.bandit()
    else:
        st.session_state['data'].append(humanoid.bandit())

if button2:
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = humanoid.orc()
    else:
        st.session_state['data'].append(humanoid.orc())

if button3:
    st.session_state['data'].sort(key=lambda x: x.ini, reverse=True)

if button5:
    st.session_state['data'] = [humanoid.dummy()]

with ini_container:
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with st.container(border=True):
        with col1:
            st.header('Name')
        with col2:
            st.header('Ini')
        with col3:
            st.header('LeP')
        with col4:
            st.header('AT')
        with col5:
            st.header('PA')
        with col6:
            st.header('Wunden')
        with col7:
            st.header('RS')
                
    for i, element in enumerate(st.session_state['data']):
        # print(row)
        with st.container(border=True):
            col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
            with col1:
                st.subheader(element.name)
            with col2:
                st.subheader(element.ini)
            with col3:
                st.subheader(element.lep)        
            with col4:
                c1, c2 = st.columns(2)
                with c1:
                    atbutton = st.button(f'AT: {element.at}', key=i)
                with c2:
                    if atbutton:
                        st.subheader(element.attack_roll())
            with col5:
                c1, c2 = st.columns(2)
                with c1:
                    atbutton = st.button(f'AT: {element.pa}', key=i+30)
                with c2:
                    if atbutton:
                        st.subheader(element.parry_roll())
            with col6:
                st.subheader(element.wound_count)
            with col7:
                st.subheader(element.rs)

st.write(st.session_state)