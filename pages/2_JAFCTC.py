import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd

page_header = st.container(border=True)
JAFCTC_sect = st.container(border=True)

with page_header:
    st.title("Forrest Tech Center Dashboard")
    st.image('images/BOB05prepLtwnWharf(crop).jpg',
             caption='Getting BOB-05 ready for launch at Leondardtown Wharf, May 19, 2023')

with JAFCTC_sect:
    st.subheader("Dr. J.A. Forrest Career and Technology Center")
    st.markdown('Our JAFCTC BOBS are soon to be in year 3 of operation and pretty soon we\'ll be ' +
                'building BOB 3.0 -- our newest and improved BOB.')
    l_col, r_col = st.columns(2)
    with l_col:
        st.subheader('LEFT COLUMN SUBHEADER')
        st.text('LEFT COLUMN TEXT')
        st.markdown("---")
    with r_col:
        st.subheader('RIGHT COLUMN SUBHEADER')
        st.text('RIGHT COLUMN TEXT')
        st.markdown("---")
    st.markdown("---")

# Adds a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Select a BOB to see its data(future feature)',
    ('BOB-01', 'BOB-02', 'BOB-03', 'BOB-04', 'BOB-05', 'BOB-06', 'BOB-07', 'BOB-08',
        'BOB-09', 'BOB-10', 'BOB-11')
)
