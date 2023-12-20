import streamlit as st

sponsors_sect = st.container()
sponsors_sect2 = st.container()

with sponsors_sect:
    st.title('Our Sponsors and Partners')
    st.markdown("---")

    # logos
    st.subheader('Funding was generously provided by')

    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/CBTRUST-CoBranding-Horizontal-Logo-SCREEN.png',
             caption='Funding for the 22-23 and 23-24 MWEE Grants')
    st.markdown("---")

    st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/Chesapeake_Oyster_Alliance_PNG.png',
             caption='Funding for the 22-23 and 23-24 Oyster Innovation Grants')
    st.markdown("---")

    st.subheader('Grant Holders')
    st.markdown("---")

    l_col, r_col = st.columns(2)  # the position of the col variable in the list determines its position?

    with l_col:
        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/logo_SMRWA_color_trans275.gif',
                 caption='Oyster Innovation Grant Holder 2023 - 2024')
        st.markdown("---")

        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/Logo-ForrestTechCenter.jpg')

        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/StMarysCountyPublicSchools-LOGO.png',
                 caption='Youth Education (MWEE) Grant Holder 2022 - 2023 and 2023 - 2024 school years')

        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/Leonardtown-tagline-Icon_4C.png',
                 caption='Our host at the Leonardtown Wharf - see the sign!')
        st.markdown("---")

        st.image('/Users/normoforan/SynologyDrive/StreamlitPICS/FSCB logo.png',
                 caption='Partner and lead organization for the Lovers Point Oyster Restoration site')

    with r_col:
        st.markdown('''
        Let's talk about the St. Mary\'s River Watershed Association!

        Talk more...

        Talk more...

        Visit the [SMRWA website](http://www.smrwa.org)
        ''')
        st.markdown("---")
        st.markdown('''
        Let's talk about the Dr. James A. Forrest Career and Technology Center!

        More talk...

        More talk...

        Visit the [BOBs website](https://sites.google.com/view/bobsmonitors/home)

        Visit the [JAFCTC website](https://tech.smcps.org)
        ''')
