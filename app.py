import streamlit as st
import pandas as pd
from enemies.humanoid import humanoid
import utilities.df_utils as dfutils

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame([humanoid.bandit().to_dict()])

if 'ini_idx' not in st.session_state:
    st.session_state['ini_idx'] = 0

if 'round' not in st.session_state:
    st.session_state['round'] = 1


col1, col2, col3, col4 = st.columns(4)

with col1:
    button1 = st.button('add bandit')

with col2:
    button2 = st.button('add orc')

with col3:
    button3 = st.button('Sort')

with col4:
    button4 = st.button('Next')

if button1:
    e1 = humanoid.bandit().to_dict()
    e1 = pd.DataFrame([e1])
    st.session_state['data'] = pd.concat([st.session_state['data'], e1], ignore_index=True)

if button2:
    e1 = humanoid.orc().to_dict()
    e1 = pd.DataFrame([e1])
    st.session_state['data'] = pd.concat([st.session_state['data'], e1], ignore_index=True)

if button3:
    st.session_state['data'].sort_values(by=['INI'], ascending=False, inplace=True, ignore_index=True)

if button4:
    if len(st.session_state['data'].index)-1 != st.session_state['ini_idx']:
        st.session_state['ini_idx'] += 1
    else:
        st.session_state['ini_idx'] = 0
        st.session_state['round'] += 1

# if len(st.session_state['data'].index) > 0:
    # dfutils.highlight_by_index(st.session_state['data'], st.session_state['ini_idx'])
# st.dataframe(st.session_state['data'])
st.dataframe(
        st.session_state['data'].style.applymap(
            lambda _: "background-color: darkseagreen;", subset=([st.session_state['ini_idx']], slice(None))
        )
    )
st.write(st.session_state)
