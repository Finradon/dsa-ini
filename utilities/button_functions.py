import os
import streamlit as st
from enemies.entity import entity
from enemies.hero import hero
from enemies.demon import demon
from enemies.melee_fighter import melee_fighter
from utilities.entity_labels import map_entities

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
        for element in st.session_state['data']:
            element.regenerate()
        # ToDo: Invoke Regenerate Method

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
    add_entity(hero.from_json(data))

# import a demon by its name
def add_demon_from_name(name: str):
    path = 'json-samples/demons/' + name + '.json'
    with open(path) as f:
        data = f.read()
    add_entity(demon.from_json(data))

def add_humanoid_from_name(name: str):
    path = 'json-samples/humanoids/' + name + '.json'
    with open(path) as f:
        data = f.read()
    add_entity(melee_fighter.from_json(data))

def add_npc_from_name(name: str):
    path = 'json-samples/specials/' + name + '.json'
    with open(path) as f:
        data = f.read()
    add_entity(melee_fighter.from_json(data))

def remove_entity(ent: entity):
    if len(st.session_state['data']) == 1:
        st.session_state['data'].append(entity.dummy())
        
    st.session_state['data'].remove(ent)


# ----- NON-BUTTON-FUNCTIONS ----- #

# get filenames given a directory
def get_names_from_dir(dir: str) -> list:
    file_list = os.listdir(dir)
    for i, elem in enumerate(file_list):
        file_list[i] = os.path.splitext(elem)[0]

    return file_list

def get_name_count(name: str) -> int:
    counter = 0
    for entity in st.session_state['data']:
        if entity.name[:len(name)] == name:
            counter += 1

    return counter

def add_entity(ent: entity):

    if ent.name not in get_names_from_dir('json-samples/helden') + get_names_from_dir('json-samples/specials'):
        nr = get_name_count(ent.name) + 1
        ent.name = ent.name + " " + str(nr)

    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = ent
    else:
        st.session_state['data'].append(ent)


