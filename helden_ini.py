import streamlit as st
from enemies.entity import entity
from enemies.melee_fighter import melee_fighter

st.set_page_config(layout="wide", page_title="Helden Initiative")
st.title("Helden Initiative")

# define session state data (persistent across sessions)
if 'data' not in st.session_state:
    st.session_state['data'] = [entity.dummy()] # list of all fight participants

if 'ini_idx' not in st.session_state:
    st.session_state['ini_idx'] = 0 # index of the fight participant whose turn it is

if 'round' not in st.session_state:
    st.session_state['round'] = 1 # round counter


# top buttons, general interaction
with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns(6)
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
    
    with col6:
        st.header(f"Runde: {st.session_state['round']}")


ini_container = st.container(border=True)

if button1:
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = melee_fighter.bandit()
    else:
        st.session_state['data'].append(melee_fighter.bandit())

if button2:
    if st.session_state['data'][0].name == "Dummy":
        st.session_state['data'][0] = melee_fighter.orc()
    else:
        st.session_state['data'].append(melee_fighter.orc())

if button3:
    st.session_state['data'].sort(key=lambda x: x.ini, reverse=True)
    for element in st.session_state['data']:
        element.turn = False

if button4:
    if len(st.session_state['data'])-1 != st.session_state['ini_idx']:
        st.session_state['ini_idx'] += 1
    else:
        st.session_state['ini_idx'] = 0
        st.session_state['round'] += 1

if button5:
    st.session_state['data'] = [entity.dummy()]
    st.session_state['ini_idx'] = 0
    st.session_state['round'] = 1   

# set the appropriate particiapants turn to True
st.session_state['data'][st.session_state['ini_idx']].turn = True
st.session_state['data'][st.session_state['ini_idx'] - 1].turn = False

# declaire and fill the container with the participants
with ini_container:
    # Column Titles
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([2, 1, 1, 4, 4, 2, 1, 1, 1])
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

    # loop over all elements in the participant list
    for i, element in enumerate(st.session_state['data']):
        
        # use a border if it is the participants turn
        with st.container(border=element.turn):
            
            # init columns and display data
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([2, 1, 1, 4, 4, 2, 1, 1, 1])
            with col1:
                st.subheader(element.name)
            with col2:
                st.subheader(element.ini)
            with col3:
                st.subheader(element.lep)        
            with col4:
                # define an attack roll button
                c1, c2 = st.columns([1, 3])
                with c1:
                    atbutton = st.button(f'AT: {element.at}', key=i)
                with c2:
                    if atbutton:
                        st.subheader(element.attack_roll())
            with col5:
                # parry roll button
                c1, c2 = st.columns([1, 3])
                with c1:
                    atbutton = st.button(f'PA: {element.pa}', key=i+100)
                with c2:
                    if atbutton:
                        st.subheader(element.parry_roll())
            with col6:
                if hasattr(element, 'wound_count'):
                    st.subheader(element.wound_count)
            with col7:
                st.subheader(element.rs)
            with col8:
                # damage input
                dmg = st.number_input(label="Schaden", value=None, min_value=0, key=i+200, label_visibility="hidden")
            with col9:
                dmg_button = st.button("DMG", key=i+300, on_click=element.receive_damage, kwargs={"value": dmg})
                
# JSON import
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        files = st.file_uploader("Importiere eigene Charaktere:", type='json', accept_multiple_files=True)

    with col2:
        def process_files(file_items):
            for file in file_items:
                file_data = file.getvalue().decode("utf-8")
                if st.session_state['data'][0].name == "Dummy":
                    st.session_state['data'][0] = melee_fighter.from_json(file=file_data)
                else:
                    st.session_state['data'].append(melee_fighter.from_json(file=file_data))
        
        import_button = st.button('Import', on_click=process_files, kwargs={"file_items": files})

# st.write(st.session_state)
