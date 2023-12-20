import streamlit as st
import streamlit.components.v1 as components
# import pandas as pd

page_header = st.container()
SMRWA_sect = st.container()

with page_header:
    st.title("St. Mary\'s River Watershed Association Dashboard")
    st.subheader("Location of the 2023 Study Sites")
    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/SMRWA_Buoy_Locations.jpg',
             caption='BOB locations for the 2023 study season')
    st.markdown("---")

with SMRWA_sect:
    st.subheader("Ongoing exploratory analysis of the 2023 data")
    st.markdown('**Sample sensor buoy data (preliminary)**')
    st.markdown(''':blue[The graph below shows salinity data from Sensor Buoy 01 (SB-01) compared to the flow rate of the
                St. Mary\'s River. The river flow rate data comes from the USGS station ID 01661500 at Great Mills. Salinity
                data is from SB-01 as reported to ThingSpeak from 20 June to 03 October 2023. Flow rate values are divided
                by 10 to bring them into the same range of Salinity for ease of comparison.]''')

    salSB01xFR = open("/Users/normoforan/SynologyDrive/StreamlitPICS/SMRWA_2023_SB01_SalinityHMxFlowRateSM.html",
                      'r', encoding='utf-8')
    source_code = salSB01xFR.read()
    components.html(source_code, height=400)

    st.markdown("---")

st.sidebar.markdown('Some explanatory sidebar text that goes on for awhile... blah blah')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Select a BOB to see its data(future feature)',
    ('BOB-01', 'BOB-02', 'BOB-03', 'BOB-04', 'BOB-05', 'BOB-06', 'BOB-07', 'BOB-08',
        'BOB-09', 'BOB-10', 'BOB-11')
)

st.sidebar.checkbox('This is an awesome feature -- check me!!')
