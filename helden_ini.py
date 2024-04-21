import streamlit as st
from enemies.humanoid import humanoid

st.set_page_config(layout="wide", page_title="Helden Initiative")
st.title("Helden Initiative")

if 'data' not in st.session_state:
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
    for element in st.session_state['data']:
        element.turn = False

if button4:
    if len(st.session_state['data'])-1 != st.session_state['ini_idx']:
        st.session_state['ini_idx'] += 1
    else:
        st.session_state['ini_idx'] = 0
        st.session_state['round'] += 1

if button5:
    st.session_state['data'] = [humanoid.dummy()]
    st.session_state['ini_idx'] = 0
    st.session_state['round'] = 1

st.session_state['data'][st.session_state['ini_idx']].turn = True
st.session_state['data'][st.session_state['ini_idx'] - 1].turn = False
with ini_container:
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([2, 1, 1, 4, 4, 2, 1, 2])
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
        with st.container(border=element.turn):
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([2, 1, 1, 4, 4, 2, 1, 2])
            with col1:
                st.subheader(element.name)
            with col2:
                st.subheader(element.ini)
            with col3:
                st.subheader(element.lep)        
            with col4:
                c1, c2 = st.columns([1, 3])
                with c1:
                    atbutton = st.button(f'AT: {element.at}', key=i)
                with c2:
                    if atbutton:
                        st.subheader(element.attack_roll())
            with col5:
                c1, c2 = st.columns([1, 3])
                with c1:
                    atbutton = st.button(f'PA: {element.pa}', key=i+30)
                with c2:
                    if atbutton:
                        st.subheader(element.parry_roll())
            with col6:
                st.subheader(element.wound_count)
            with col7:
                st.subheader(element.rs)
            with col8:
                with st.form(key= f"{i}"):
                    dmg = st.number_input(label="a", min_value=1, key=i+60)
                    if st.form_submit_button("Submit"):
                        element.receive_damage(dmg)

# st.write(st.session_state)