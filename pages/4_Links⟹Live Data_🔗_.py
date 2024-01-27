import streamlit as st
import streamlit.components.v1 as components
html = '<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1329419/widgets/300436"></iframe>'

st.set_page_config(
    page_title="LINKS!",
    page_icon="🔗",
)
page_header = st.container()
TS_FT_sect = st.container(border=True)
TS_SM_sect = st.container(border=True)

with page_header:
    st.title("Links to the Live Data and more!")
    st.image('images/ThingSpeakHumdityGraph.png',
             caption='Graph of Humidity from ThingSpeak')
    # The following code works to embed the entire page.........
    # components.iframe("https://thingspeak.com/channels/1329419", width=None, height=600, scrolling=True)
    st.components.v1.html(html, scrolling=True)
    st.markdown('''
                :red[BOB data is routed to public channels hosted by [ThingSpeak](https://thingspeak.com).
                 ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize,
                 and analyze live data streams in the cloud. You can send data to ThingSpeak
                from any IOT device and use MATLAB to create visualizations of live data and
                 send alerts.]
                ''')

with TS_FT_sect:
    st.subheader("ThingSpeak Channels ::: Forrest Tech BOBs")
    st.markdown('[BOB-01](https://thingspeak.com/channels/2062275)')
    st.markdown('[BOB-02](https://thingspeak.com/channels/2062276)')
    st.markdown('[BOB-03](https://thingspeak.com/channels/2062277)')
    st.markdown('[BOB-04](https://thingspeak.com/channels/2062279)')
    st.markdown('[BOB-05](https://thingspeak.com/channels/1807956)')
    st.markdown('[BOB-06](https://thingspeak.com/channels/2062280)')
    st.markdown('[BOB-07](https://thingspeak.com/channels/1650300)')

with TS_SM_sect:
    st.subheader("ThingSpeak Channels ::: St. Mary\'s River BOBs")
    st.markdown('[SB-01](https://thingspeak.com/channels/2188765)')
    st.markdown('[SB-02](https://thingspeak.com/channels/2188768)')
    st.markdown('[SB-03](https://thingspeak.com/channels/2188771)')
    st.markdown('[SB-04](https://thingspeak.com/channels/2188776)')
    st.markdown('[SB-05](https://thingspeak.com/channels/2256155)')
