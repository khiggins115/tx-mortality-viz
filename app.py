import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


from load_data import (
    load_health_data,
)
from make_plots import (
    plot_mortality_lines,
    plot_mortality_heatmaps,
    plot_mortality_bars
)

st.set_page_config(layout="wide")


#read in climate data
#tx_climate_df = pd.read_csv('../data/cleaned/tx_for_streamlit/tx_climate_wave.csv', parse_dates=['month_year_long'], dtype={'county_FIPS': object})



st.title("Texas Case Study: County Level Health Trends Investigator")
st.header("A Visual Comparison of Disease Mortality")
st.write("We created this interactive visualization to help users dig into and identify interesting trends, hotspots & associations across mortality causes")

dfs_to_plot = ['Cardiovascular Disease', 'Infectious Diseases', 'Respiratory Diseases', 'Substance Abuse & Self Injury']
sexes = ['Male', 'Female', 'Both']
years = list(range(1980, 2015))

#creates a sidebar
st.sidebar.header('Choose Your Mortality Metrics')
st.sidebar.write("For a better experience, collapse this sidebar once you've made your selections.")
select_mortality_df = st.sidebar.selectbox("Select Disease", dfs_to_plot)
disease_df = load_health_data(select_mortality_df)

mortality_causes = disease_df['cause_name'].unique()

sex = st.sidebar.selectbox("Select Sex Aggregation", sexes)
cause = st.sidebar.selectbox('Select Cause of Death', mortality_causes)  
year = st.sidebar.selectbox("Select Year", years)

show_mortality_lines = st.checkbox("Would you like to see the Mortality Rate over time on a lineplot?")
if show_mortality_lines:
    mortality_lineplot = plot_mortality_lines(disease_df, select_mortality_df, sex)
    st.pyplot(mortality_lineplot)


col1, col2 = st.columns([5, 4])

with col1:
    mortality_heatmap = plot_mortality_heatmaps(disease_df, cause, year, sex)

    st.plotly_chart(mortality_heatmap)

with col2:
    #st.header(cause + ": Granular Mortality Rates, 1980 to 2014 - " + sex)
    mortality_barplot = plot_mortality_bars(disease_df, select_mortality_df, year, sex)
    st.pyplot(mortality_barplot)


