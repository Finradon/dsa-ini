import os
import streamlit as st
from enemies.entity import entity
from utilities.entity_labels import map_entities

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
def process_files(file_items, class_name: str):
    class_type = map_entities(class_name)
    if class_type is not None:
        for file in file_items:
            file_data = file.getvalue().decode("utf-8")
            # TODO handle files with wrong json format
            if st.session_state['data'][0].name == "Dummy":
                st.session_state['data'][0] = class_type.from_json(file=file_data)
            else:
                st.session_state['data'].append(class_type.from_json(file=file_data))
    else: 
        st.warning('File does not match class type.')

# import a hero by its name
def add_hero_from_name(name: str):
    path = 'json-samples/helden/' + name + '.json'
    with open(path) as f:
        data = f.read()
    st.session_state['data'].append(humanoid.from_json(data))

# ----- NON-BUTTON-FUNCTIONS ----- #

# get filenames given a directory
def get_names_from_dir(dir: str) -> list:
    file_list = os.listdir(dir)
    for i, elem in enumerate(file_list):
        file_list[i] = os.path.splitext(elem)[0]

    return file_list