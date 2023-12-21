import streamlit as st
import pandas as pd
import plotly.express as px

page_header = st.container()
bgrnd_sect = st.container()

macrun_precip = pd.read_csv(
    "/data/MacRunPrecipMonthly2023.csv"
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
    st.title("Other Southern Maryland Watershed Data Sources")
    st.text('BRETON BAY WATERSHED -- USGS Stream data')

    st.plotly_chart(fig)
    st.markdown('Source:  USGS Waterdata:  Mcintosh Run Near Leonardtown, MD -- ' +
                'see:  https://waterdata.usgs.gov/monitoring-location/01661350/#parameterCode=00065&period=P7D&showMedian=false')
    st.markdown("---")
