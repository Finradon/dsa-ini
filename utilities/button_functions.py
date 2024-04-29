import streamlit as st
from enemies.humanoid import humanoid

# button1&2: Add generic bandit
def add_enemy(enemy: humanoid):
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = enemy
    else:
        st.session_state['data'].append(enemy)

# button 3: sort the initiative list
def sort_enemies():
    st.session_state['data'].sort(key=lambda x: x.ini, reverse=True)
    for element in st.session_state['data']:
        element.turn = False

def next():
    if len(st.session_state['data'])-1 != st.session_state['ini_idx']:
        st.session_state['ini_idx'] += 1
    else:
        st.session_state['ini_idx'] = 0
        st.session_state['round'] += 1

def reset():
    st.session_state['data'] = [humanoid.dummy()]
    st.session_state['ini_idx'] = 0
    st.session_state['round'] = 1   