import streamlit as st
import streamlit.components.v1 as components
import json
from pathlib import Path

html = '''<iframe width="450" height="260" style="border: 1px solid #cccccc;"
src="https://thingspeak.com/channels/2402453/widgets/790333"></iframe>'''

st.set_page_config(
    page_title="LINKS!",
    page_icon="🔗",
)

# Load channel configuration
def load_channel_config():
    """Load channel configuration from JSON file."""
    config_path = Path(__file__).parent.parent / "config" / "channels.json"
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

channel_config = load_channel_config()

# Separate channels by owner
cbwins_channels = {
    ch_id: info for ch_id, info in channel_config.items()
    if info['status'] == 'active' and info['owner'] == 'CBWINS'
}
smrwa_channels = {
    ch_id: info for ch_id, info in channel_config.items()
    if info['status'] == 'active' and info['owner'] == 'SMRWA'
}

page_header = st.container()
TS_FT_sect = st.container(border=True)
TS_SM_sect = st.container(border=True)

with page_header:
    st.title("Links to the Live Data and more!")
    st.image('images/ThingSpeakHumdityGraph.png',
             caption='Graph of Humidity from ThingSpeak')
    # The following code embeds the entire page.........
    # components.iframe("https://thingspeak.com/channels/1329419", width=None, height=600, scrolling=True)
    # The following code embed a single chart field.........
    # st.markdown('**Live voltage reading from the Floating Marsh -- BOB-08**')
    # st.components.v1.html(html, height=300, scrolling=False)
    st.markdown('''
                :red[BOB data is routed to public channels hosted by [ThingSpeak](https://thingspeak.com).
                 ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize,
                 and analyze live data streams in the cloud. You can send data to ThingSpeak
                from any IOT device and use MATLAB to create visualizations of live data and
                 send alerts.]
                ''')

with TS_FT_sect:
    st.subheader("ThingSpeak Channels ::: CBWINS BOBs")
    # Sort channels by device name for consistent display
    sorted_cbwins = sorted(cbwins_channels.items(),
                          key=lambda x: (x[1]['device_name'], x[1]['channel_type']))
    for channel_id, info in sorted_cbwins:
        display_name = format_channel_display_name(info['device_name'], info['channel_type'])
        st.markdown(f'[{display_name}](https://thingspeak.com/channels/{channel_id})')

with TS_SM_sect:
    st.subheader("ThingSpeak Channels ::: SMRWA BOBs")
    # Sort channels by device name for consistent display
    sorted_smrwa = sorted(smrwa_channels.items(),
                         key=lambda x: (x[1]['device_name'], x[1]['channel_type']))
    for channel_id, info in sorted_smrwa:
        display_name = format_channel_display_name(info['device_name'], info['channel_type'])
        st.markdown(f'[{display_name}](https://thingspeak.com/channels/{channel_id})')
