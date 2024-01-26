import streamlit as st
# import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
    page_title="BOBS!",
    page_icon="👋",
)

page_header = st.container(border=True)
bgrnd_sect = st.container(border=True)
loc_sect = st.container(border=True)

txt_block_1 = '''
What are BOBs? They are Bay Observation Boxes! BOBs are
experimental DIY maker built water quality monitoring devices conceived and built
in St. Mary's County\'s (Maryland) Seventh District. BOBs are built using inexpensive
off-the-shelf components for a fraction of the cost of commercially available products.
The first BOB prototype was deployed in Breton Bay in August 2022. Thanks to CBTRUST
MWEE and Oyster Innovation grants, BOB hardware and software is being tested and
refined through the efforts of the student citizen scientists at the Dr. J.A. Forrest
Career and Technology Center and the St. Mary's River Watershed Association. Our other
critical partners are the Town of Leonardtown, the Chesapeake Biological Laboratory,
the Calvert Marine Museum, and the Friends of St. Clements Bay.
'''

with page_header:
    st.title("The BOBS Project Dashboard")
    st.markdown(''':red[
                **!!! NOTE !!!** While much of this site is accurate, currently this app is only a work in progress
                 / draft / trial site to test and familiarize ourselves with the Streamlit library and Cloud! Future
                enhancements will focus on live status of BOBs and data visualizations of water quality.]'''
                )
    st.image('images/P5_BretonBay.png',
             caption='Prototype 5 at the Lovers Point Oyster Restoration site in Breton Bay, August 2022')

    st.markdown('### The BOBS project seeks to engage students and the general public ' +
                'to increase awareness of water quality issues.')
    st.markdown('''**:red["Our species needs, and deserves, a citizenry with minds wide awake and a basic understanding of how
                the world works." -- Carl Sagan]**''')
    st.markdown('''**:blue[Paraphrasing Thomas Jefferson, "Whenever the people are well-informed, they can be trusted with the
                governance of their own ecosystems."]**''')
    txt_block_1


with bgrnd_sect:
    st.subheader('Locations of BOBs in Southern Maryland')
    st.text('PAST, PRESENT and FUTURE')

    # ***** LOCATIONS MAP *****
    locations = pd.read_csv('data/LocationsLatLong.csv')
    st.dataframe(locations, hide_index=True)
    st.map(locations, use_container_width=True)
    st.caption('Map of BOBS (Bay Observation Boxes) in Southern Maryland - Past, Present, and Future')
