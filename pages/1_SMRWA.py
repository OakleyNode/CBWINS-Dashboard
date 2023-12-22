import streamlit as st
import streamlit.components.v1 as components
# import pandas as pd

page_header = st.container(border=True)
status_sect = st.container(border=True)
data2023_sect = st.container(border=True)

with page_header:
    st.title("St. Mary\'s River Watershed Association Dashboard")
    st.subheader("Location of the 2023 Study Sites")
    st.image('images/SMRWA_Buoy_Locations.jpg',
             caption='BOB locations for the 2023 study season')
    # st.markdown(":red[Make the picture smaller and add better explanatory text]")

with status_sect:
    st.subheader('Current BOB Status')
    st.text('PLACEHOLDER FOR RED/YELLOW/GREEN DASHBOARD OF BOB STATUS')

with data2023_sect:
    st.subheader("Ongoing exploratory analysis of the 2023 data")
    st.markdown('**Sample sensor buoy data (preliminary)**')
    st.markdown(''':blue[The graph below shows salinity data from Sensor Buoy 01 (SB-01) compared to the flow rate of the
                St. Mary\'s River. The river flow rate data comes from the USGS station ID 01661500 at Great Mills. Salinity
                data is from SB-01 as reported to ThingSpeak from 20 June to 03 October 2023. Flow rate values are divided
                by 10 to bring them into the same range of Salinity for ease of comparison.]''')

    salSB01xFR = open("images/SMRWA_2023_SB01_SalinityHMxFlowRateSM.html",
                      'r', encoding='utf-8')
    source_code = salSB01xFR.read()
    components.html(source_code, height=400)

    st.markdown("---")

st.sidebar.markdown('Some explanatory sidebar text that goes on for awhile... blah blah')
st.sidebar.checkbox('This is an awesome feature -- check me!!')
