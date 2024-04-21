"""
This is the code for the CBWINS Dashboard on Steamlit.
Run code locally by entering:  streamlit run BOBS_Home.py
in the terminal window below.
"""

import streamlit as st

# import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from dataloader import ThingSpeakAPICaller  # type: ignore

st.set_page_config(
    page_title="BOBS!",
    page_icon="👋",
)

page_header = st.container(border=True)
bgrnd_sect = st.container(border=True)
loc_sect = st.container(border=True)
status_sect = st.container(border=True)


def assign_project_to_bob(bob_names):
    labels = {"BOB": "JAFCTC", "SB": "SMRWA"}
    res = ["CBWINS"] * len(bob_names)
    for k, name in enumerate(bob_names):
        for key, value in labels.items():
            if name.find(key) != -1:
                res[k] = value
                break
    return [[n, r] for n, r in zip(bob_names, res)]


TS_channel_IDs = {
    "1329419": "Prototype-5b",
    "1650300": "BOB-07",
    "1807956": "BOB-05",
    "1948145": "Prototype-4",
    "2062275": "BOB-01",
    "2062276": "BOB-02",
    "2062277": "BOB-03",
    "2062279": "BOB-04",
    "2062280": "BOB-06",
    "2188765": "SB-01",
    "2188768": "SB-02",
    "2188771": "SB-03",
    "2188776": "SB-04",
    "2256155": "SB-05",
    "2402453": "BOB-08",
    "2475657": "Prototype-7a",
    "2490682": "BOB-09",
    "2506725": "BOB-10",
}
channel_ids = {
    k: v
    for k, v in zip(
        TS_channel_IDs.keys(), assign_project_to_bob(list(TS_channel_IDs.values()))
    )
}


def format_timedelta(td):
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if days:
        parts.append(f"{days} {'day' if days <= 1 else 'days'}")
    if hours:
        parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if not any([days, hours, minutes]):
        parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    return ", ".join(parts)


# define header names
col_names = [
    "Channel",
    "Last Timestamp",
    "BOB ID",
    "Project",
    "Time since last TX",
    "Voltage",
]
result = pd.concat(
    [ThingSpeakAPICaller.get(id, {"results": 1}) for id in channel_ids.keys()]
).set_index(pd.Index(channel_ids.keys()))
keep = result.columns[np.array([col.find("oltage") for col in result.columns]) != -1]
status = result[["Timestamp"]].reset_index(names="channel id")
status[["bob name", "project"]] = list(channel_ids.values())
status["offset"] = [
    (pd.Timestamp.now(tz="UTC") - t).round(freq="min") for t in status["Timestamp"]
]
status = status.rename(columns={"offset": "Time_since_last_TX"})
status["voltage"] = np.max(result[keep], axis=1).values.round(1)
status.sort_values(by=["project", "Time_since_last_TX"], inplace=True)

txt_block_1 = """
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
"""

with page_header:
    st.title("The BOBS Project Dashboard")
    st.markdown(
        """:red[
                **!!! NOTE !!!** While much of this site is accurate, this app is still a work in progress
                to test and familiarize ourselves with the Streamlit library. Future enhancements will include
                the live status of BOBs, an interactive map of BOB locations by year, and visualizations of
                water quality data.]"""
    )
    st.image(
        "images/P5_BretonBay.png",
        caption="Prototype 5 at the Lovers Point Oyster Restoration site in Breton Bay, August 2022",
    )

    st.markdown(
        "### The BOBS project seeks to engage students and the general public "
        + "to increase awareness of water quality issues."
    )
    st.markdown(
        """**:red["Our species needs, and deserves, a citizenry with minds wide awake and a basic understanding of how
                the world works." -- Carl Sagan]**"""
    )
    st.markdown(
        """**:blue[Paraphrasing Thomas Jefferson, "Whenever the people are well-informed, they can be trusted with the
                governance of their own ecosystems."]**"""
    )
    txt_block_1


with bgrnd_sect:
    st.subheader("Locations of BOBs in Southern Maryland")
    st.text("PAST, PRESENT and FUTURE")

    # ***** LOCATIONS MAP *****
    locations = pd.read_csv("data/LocationsLatLong.csv")
    st.dataframe(locations, hide_index=True)
    st.map(locations, use_container_width=True)
    st.caption("Map of BOBS (Bay Observation Boxes) in Southern Maryland")

with status_sect:
    st.subheader("Current BOB Status")
    st.dataframe(status)  # Same as st.write(df)
    st.text("Refresh the page or use full screen if locations are not immediately apparent.")
