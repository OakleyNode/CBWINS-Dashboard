import streamlit as st
# import pandas as pd
from stace.dataloader import ThingSpeakAPICaller  # Import your ThingSpeakAPICaller class

# Create a function to fetch data from ThingSpeak
def fetch_thingspeak_data(channel_id, get_config):
    data = ThingSpeakAPICaller.get(channel_id, get_config)
    return data

# Streamlit app layout
def main():

    st.title("Streamlit ThingSpeak Data Fetcher")

    # Widget for user input (channel ID and custom query)
    # channel_id = st.number_input("Enter ThingSpeak Channel ID", value=123, step=1)
    channel_ID_list = ('2062275', '2062276', '2062277', '2062279', '1807956', '2062280', '1650300')
    channel_id = st.selectbox("Enter ThingSpeak Channel ID", channel_ID_list)

    custom_query = st.text_input("Enter custom query for API call", value="results=10")

    # Button to trigger API call
    if st.button("Fetch Data"):
        st.text("Fetching data...")
        try:
            # Parse custom query as a dictionary
            get_config = dict(x.split("=") for x in custom_query.split("&"))
            # Fetch data from ThingSpeak
            data = fetch_thingspeak_data(channel_id, get_config)
            # Display the fetched data
            st.dataframe(data)
            st.success("Data fetched successfully!")
        except Exception as e:
            st.error(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
