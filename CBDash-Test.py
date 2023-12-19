import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
# import numpy as np

page_header = st.container()
bgrnd_sect = st.container()
JAFCTC_sect = st.container()
SMRWA_sect = st.container()
sponsors_sect = st.container()
loc_sect = st.container()

txt_block_1 = '''What are BOBs? They are Bay Observation Boxes! BOBs are
experimental DIY maker built water quality monitoring devices conceived and built
in St. Mary's County\'s (Maryland) Seventh District. BOBs are built using inexpensive
off-the-shelf components for a fraction of the cost of commercially available products.
The first BOB prototype was deployed in Breton Bay in August 2022. Thanks to CBTRUST
MWEE and Oyster Innovation grants, BOB hardware and software is being tested and
refined through the efforts of student and citizen scientists at the J.A. Forrest
Career and Technology center and the St. Mary's River Watershed Association. Our other
critical partners are the Town of Leonardtown, the Chesapeake Biological Laboratory,
the Calvert Marine Museum, and the Friends of St. Clements Bay.'''

with page_header:
    st.title("The BOBS Project")
    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/P5_BretonBay.png',
             caption='Prototype 5 at the Lovers Point Oyster Restoration site in Breton Bay, August 2022')

    st.markdown('### The BOBS project seeks to engage students and the general public ' +
                'to increase awareness of water quality issues.')
    st.markdown('''**:red["Our species needs, and deserves, a citizenry with minds wide awake and a basic understanding of how
                the world works." -- Carl Sagan]**''')
    st.markdown('''**:blue[Paraphrasing Thomas Jefferson, "Whenever the people are well-informed, they can be trusted with the
                governance of their own ecosystems."]**''')
    txt_block_1
    st.markdown("---")
    st.markdown('**Past, Present and Future locations of BOBs in Southern Maryland...**')
    # ***** LOCATIONS MAP *****
    locations = pd.read_csv('/Users/normoforan/SynologyDrive/DATA/LocationsLatLong.csv')
    st.dataframe(locations, hide_index=True)
    st.map(locations, use_container_width=True)
    st.caption('Map of BOBS (Bay Observation Boxes) in Southern Maryland')
    st.markdown("---")

macrun_precip = pd.read_csv(
    "/Users/normoforan/SynologyDrive/DATA/USGS/MacRunPrecipMonthly2023.csv"
)
fig = px.histogram(
    macrun_precip,
    x=macrun_precip.datetime,
    y=macrun_precip.Precip,
    height=450,
    width=600,
    title="USGS - McIntosh Run - Precipitation<br>April - October 2023",
    nbins=7,
    text_auto=True,
)
fig.update_layout(
    title_font_size=18,
    title_font_family="Verdana",
    xaxis_title="<b>MONTH<b>",
    yaxis_title="<b>TOTAL RAINFALL (inches)<b>",
    title_x=0.07,
)
fig.layout.bargap = 0.1
fig.update_xaxes(ticklabelmode="period", mirror=True, linewidth=6,
                 linecolor="forestgreen", ticks="outside", showline=True)

with bgrnd_sect:
    st.text('SOUTHERN MARYLAND -- BRETON BAY WATERSHED -- GENERAL INFORMATION')

    st.plotly_chart(fig)
    st.markdown('Source:  USGS Waterdata:  Mcintosh Run Near Leonardtown, MD -- ' +
                'see:  https://waterdata.usgs.gov/monitoring-location/01661350/#parameterCode=00065&period=P7D&showMedian=false')
    st.markdown("---")

st.sidebar.markdown('Some explanatory sidebar text that goes on for awhile... blah blah')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Select a BOB to see its data(future feature)',
    ('BOB-01', 'BOB-02', 'BOB-03', 'BOB-04', 'BOB-05', 'BOB-06', 'BOB-07', 'BOB-08',
        'BOB-09', 'BOB-10', 'BOB-11')
)

st.sidebar.checkbox('This is an awesome feature -- check me!!')

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

with SMRWA_sect:
    st.subheader("St. Mary's River Watershed Association")
    st.markdown('**Sample sensor buoy data (preliminary)**')
    st.markdown(''':blue[The graph below shows salinity data from Sensor Buoy 01 (SB-01) compared to the flow rate of the
                St. Mary\'s River. The river flow rate data comes from the USGS station ID 01661500 at Great Mills. Salinity
                data is from SB-01 as reported to ThingSpeak from 20 June to 03 October 2023. Flow rate values are divided
                by 10 to bring them into the same range of Salinity for ease of comparison.]''')

    salSB01xFR = open("/Users/normoforan/SynologyDrive/StreamlitPICS/SMRWA_2023_SB01_SalinityHMxFlowRateSM.html",
                      'r', encoding='utf-8')
    source_code = salSB01xFR.read()
    components.html(source_code, height=400)

    st.markdown("---")  # End of section

with sponsors_sect:
    st.subheader('Project Sponsors and Partners')
    # logos
    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/CBTRUST-CoBranding-Horizontal-Logo-SCREEN.png',
             caption='Funding for the 22-23 and 23-24 MWEE Grants')
    st.markdown("---")

    l_col, m_col, r_col = st.columns([2, 2, 1])  # the position of the col variable in the list determines its position?
    with l_col:
        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/logo_SMRWA_color_trans275.gif',
                 caption='Oyster Innovation Grant Holder 2023 - 2024')
        st.markdown("---")

    with r_col:
        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/FSCB logo.png',
                 caption='Partner and lead organization for the Lovers Point Oyster Restoration site')
        st.markdown("---")

    with m_col:
        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/StMarysCountyPublicSchools-LOGO.png',
                 caption='Youth Education (MWEE) Grant Holder 2022 - 2023 and 2023 - 2024 school years')
        st.markdown("---")

    st.markdown("---")  # End of section
