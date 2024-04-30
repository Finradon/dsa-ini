import streamlit as st
from enemies.entity import entity
from enemies.melee_fighter import melee_fighter

# button1&2: Add generic bandit
def add_enemy(enemy: entity):
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = enemy
    else:
        st.session_state['data'].append(enemy)

# button3: sort the initiative list
def sort_enemies():
    st.session_state['data'].sort(key=lambda x: x.ini, reverse=True)
    for element in st.session_state['data']:
        element.turn = False

# button4: go next in the initiative list
def next():
    if len(st.session_state['data'])-1 != st.session_state['ini_idx']:
        st.session_state['ini_idx'] += 1
    else:
        st.session_state['ini_idx'] = 0
        st.session_state['round'] += 1

# button5: reset the list
def reset():
    st.session_state['data'] = [entity.dummy()]
    st.session_state['ini_idx'] = 0
    st.session_state['round'] = 1   

# json import button
def process_files(file_items):
    for file in file_items:
        file_data = file.getvalue().decode("utf-8")
        # TODO needs to be adapted to different classes
        if st.session_state['data'][0].name == "Dummy":
            st.session_state['data'][0] = melee_fighter.from_json(file=file_data)
        else:
            st.session_state['data'].append(melee_fighter.from_json(file=file_data))