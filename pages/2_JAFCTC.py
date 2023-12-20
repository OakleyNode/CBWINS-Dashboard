import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd

page_header = st.container()
JAFCTC_sect = st.container()

with page_header:
    st.title("The BOBS Project Dashboard")
    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/P5_BretonBay.png',
             caption='Prototype 5 at the Lovers Point Oyster Restoration site in Breton Bay, August 2022')

with JAFCTC_sect:
    st.subheader("Dr. J.A. Forrest Career and Technology Center")
    st.markdown('Our JAFCTC BOBS are soon to be in year 2 of operation and pretty soon we\'ll be ' +
                'building BOB 2.0 -- our new and improved BOB.')
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
