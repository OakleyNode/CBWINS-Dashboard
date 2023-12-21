import streamlit as st

page5_header = st.container()
funding_sect = st.container(border=True)
smrwa_sect = st.container(border=True)
JAFCTC_sect = st.container(border=True)
sponsors_sect2 = st.container(border=True)

with page5_header:
    st.title('Stakeholders')

with funding_sect:
    # logos
    st.subheader(':red[Funding was generously provided by]')

    st.image('/images/CBTRUST-CoBranding-Horizontal-Logo-SCREEN.png',
             caption='Funding for the 22-23 and 23-24 MWEE Grants')
    st.markdown("---")

    st.image('/images/Chesapeake_Oyster_Alliance_PNG.png',
             caption='Funding for the 22-23 and 23-24 Oyster Innovation Grants')

with smrwa_sect:
    l_col, r_col = st.columns(2)
    with l_col:
        st.subheader(':blue[Grant Holder]')
        st.image('/images/logo_SMRWA_color_trans275.gif',
                 caption='Oyster Innovation Grants in 2023 and in 2024')
    with r_col:
        st.markdown('''
        Let's talk about the St. Mary\'s River Watershed Association!

        Talk more...

        Talk more...

        Visit the [SMRWA website](http://www.smrwa.org)
        ''')

with JAFCTC_sect:
    l_col, r_col = st.columns(2)
    with l_col:
        st.subheader(':blue[Grant Holder]')
        st.image('/images/Logo-ForrestTechCenter.jpg')
        st.image('/images/StMarysCountyPublicSchools-LOGO.png',
                 caption='Youth Education (MWEE) Grants in the 2022 - 2023 and the 2023 - 2024 school years')
    with r_col:
        st.markdown('''
        Let's talk about the Dr. James A. Forrest Career and Technology Center!

        More talk...

        More talk...

        Visit the [BOBs website](https://sites.google.com/view/bobsmonitors/home)

        Visit the [JAFCTC website](https://tech.smcps.org)
        ''')

with sponsors_sect2:
    st.image('/images/Leonardtown-tagline-Icon_4C.png',
             caption='Our host at the Leonardtown Wharf - see the sign!')

    st.image('/images/FSCB logo.png',
             caption='Partner and lead organization for the Lovers Point Oyster Restoration site')
