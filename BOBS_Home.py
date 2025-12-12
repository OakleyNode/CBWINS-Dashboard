"""
This is the code for the CBWINS Dashboard on Steamlit.
Run code locally by entering:  streamlit run BOBS_Home.py
in the terminal window below.
"""

import streamlit as st

# import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import requests
import json
from pathlib import Path
from abc import ABC, abstractmethod

st.set_page_config(
    page_title="BOBS!",
    page_icon="👋",
)

page_header = st.container(border=True)
bgrnd_sect = st.container(border=True)
loc_sect = st.container(border=True)
status_sect = st.container(border=True)


class _APICaller(ABC):
    @abstractmethod
    def get():
        pass


class ThingSpeakAPICaller(_APICaller):
    @classmethod
    def get(cls, channel_id, GET_config):
        """
        Fetches data from ThingSpeak.

        Parameters
        ----------
        channel_id : int
            Channel ID to read from.

        GET_config : dict
            Specify any custom query, e.g., {"results" : 10} will get the 10 last
            points from the server.
            See https://www.mathworks.com/help/thingspeak/readdata.html for possible
            selections.

        Returns
        -------
        df : pd.DataFrame
            Table containing the fetched data. Columns are "Timestamp",
            "entry_id", and any other fields available when the data was fetched.
            Returns None if the channel is inaccessible or returns an error.

        Note
        ----
        If the channel is private, specify the API key in the `GET_config` as
        {"api_key" : api_key}.
        """
        custom_query = ""
        for key, val in GET_config.items():
            custom_query += str(key) + "=" + str(val) + "&"
        custom_query = custom_query[:-1]
        get_url = (
            f"https://api.thingspeak.com/"
            f"channels/{channel_id}/feeds.json?{custom_query}"
        )

        try:
            response = requests.get(get_url)
            response.raise_for_status()  # Raise error for bad status codes
            query = response.json()

            # Check if the response has the expected structure
            if "channel" not in query:
                print(f"Warning: Channel {channel_id} returned invalid response (no 'channel' key)")
                return None

            if "feeds" not in query or not query["feeds"]:
                print(f"Warning: Channel {channel_id} has no data feeds")
                return None

            # get descriptive field names
            field_names = cls._get_field_names(query)

            # rename column names
            results_df = pd.DataFrame(query["feeds"]).rename(columns=field_names)

            # convert data type from str to float for all fields
            df = results_df[list(field_names.values())].astype(float)

            # insert at the beginning a column of timestamps
            df.insert(0, "Timestamp", results_df["created_at"].apply(pd.Timestamp))

            return df

        except requests.exceptions.RequestException as e:
            print(f"Warning: Failed to fetch channel {channel_id}: {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Warning: Error parsing data from channel {channel_id}: {e}")
            return None

    @staticmethod
    def _get_field_names(query):
        """
        Gets the descriptive field names.

        Parameters
        ----------
        query : dict
            The raw dict fetched from the server.

        Returns
        -------
        field_names : dict
            Keys are "field{i}" generic. Values are the descriptive text.
        """
        desc = query["channel"]
        field_names = {}

        # iterate through the dict, which has keys and values
        for key, val in desc.items():
            # if the key contains "field", then it's a field so store it
            if "field" in str(key):
                field_names[key] = val

        return field_names


class USGSAPICaller(_APICaller):
    @classmethod
    def get(cls, GET_config, return_api_response=False):
        """
        Get data from usgs.gov.

        Parameters
        ----------
        GET_config : dict
            Specifies the GET request.

        return_api_response : bool, optional
            If True, will return the raw JSON response. By default False.

        Returns
        -------
        pd.DataFrame, JSON (optional)
        """
        if GET_config["format"] != "json":
            raise NotImplementedError("Can only process JSON formats currently.")

        response = requests.get(
            "https://waterservices.usgs.gov/nwis/iv/", params=GET_config
        ).json()

        # list of dicts, length is number of fields
        time_series = response["value"]["timeSeries"]
        n_fields = len(time_series)

        # combine all fields into one dataframe
        table = []
        for k in range(n_fields):
            # get the field name + units
            #   - variableName has units, but in unicode
            #   - take only name from variableName (split)
            #   - take units from unitCode and add to field name
            field_name = time_series[k]["variable"]["variableName"].split(",")[0]
            field_units = time_series[k]["variable"]["unit"]["unitCode"]
            field_name += f" ({field_units})"

            # get to the data
            df = pd.DataFrame.from_dict(time_series[k]["values"][0]["value"])
            df = (
                df.drop(columns=["qualifiers"])
                .astype({"value": np.float16})
                .rename(columns={"value": field_name, "dateTime": "Timestamp"})
            )
            df["Timestamp"] = [pd.Timestamp(t) for t in df["Timestamp"]]
            table.append(df)
        table = pd.concat(table, axis=1)
        table = table.loc[:, ~table.columns.duplicated()].set_index("Timestamp")

        if return_api_response:
            return table, response
        return table


def load_channel_config():
    """Load channel configuration from JSON file."""
    config_path = Path(__file__).parent / "config" / "channels.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config['channels']


def format_channel_display_name(device_name, channel_type):
    """Format the display name based on channel type."""
    if channel_type == "primary":
        return f"{device_name} - Primary"
    elif channel_type == "secondary":
        return f"{device_name} - Secondary"
    else:
        return device_name


# Load channel configuration from JSON file
channel_config = load_channel_config()

# Create channel_ids dictionary with display names and owners
# Format: {channel_id: [display_name, owner]}
channel_ids = {
    channel_id: [
        format_channel_display_name(info['device_name'], info['channel_type']),
        info['owner']
    ]
    for channel_id, info in channel_config.items()
    if info['status'] == 'active'
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

# Fetch data from ThingSpeak, filtering out failed channels
channel_data = {}
for channel_id in channel_ids.keys():
    data = ThingSpeakAPICaller.get(channel_id, {"results": 1})
    if data is not None:
        channel_data[channel_id] = data
    else:
        print(f"Skipping channel {channel_id} - no data available")

# Only proceed if we have at least one successful channel
if not channel_data:
    st.error("Unable to fetch data from any ThingSpeak channels. Please check your configuration.")
    st.stop()

# Combine successful channel data
result = pd.concat(channel_data.values()).set_index(pd.Index(channel_data.keys()))
keep = result.columns[np.array([col.find("oltage") for col in result.columns]) != -1]
status = result[["Timestamp"]].reset_index(names="channel id")

# Only include channel info for successfully fetched channels
status[["bob name", "project"]] = [channel_ids[ch_id] for ch_id in channel_data.keys()]
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
    st.text("Refresh the page or use full screen if locations are not immediately apparent.")

with status_sect:
    st.subheader("Current BOB Status")
    st.dataframe(status)  # Same as st.write(df)
    st.text("During the winter months, most BOBs are offline for refurbishment for the coming monitoring season.")
