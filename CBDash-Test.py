import streamlit as st
# import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

page_header = st.container()
bgrnd_sect = st.container()

loc_sect = st.container()

txt_block_1 = '''
What are BOBs? They are Bay Observation Boxes! BOBs are
experimental DIY maker built water quality monitoring devices conceived and built
in St. Mary's County\'s (Maryland) Seventh District. BOBs are built using inexpensive
off-the-shelf components for a fraction of the cost of commercially available products.
The first BOB prototype was deployed in Breton Bay in August 2022. Thanks to CBTRUST
MWEE and Oyster Innovation grants, BOB hardware and software is being tested and
refined through the efforts of student and citizen scientists at the J.A. Forrest
Career and Technology center and the St. Mary's River Watershed Association. Our other
critical partners are the Town of Leonardtown, the Chesapeake Biological Laboratory,
the Calvert Marine Museum, and the Friends of St. Clements Bay.
'''

with page_header:
    st.title("The BOBS Project Dashboard")
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
