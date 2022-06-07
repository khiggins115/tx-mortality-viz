import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



# load in the health data. Accepts a string that says what kind of data is desired, 
# and uses and if/elif statement to load the corresponding dataset
def load_health_data(health_source):
    if health_source == 'Cardiovascular Disease':
        disease_df = pd.read_csv('data/tx_cvd.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Infectious Diseases':
        disease_df = pd.read_csv('data/tx_inf.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Respiratory Diseases':
        disease_df = pd.read_csv('data/tx_resp.csv', parse_dates=['year_id'], dtype={'FIPS': object})
    elif health_source == 'Substance Abuse & Self Injury':
        disease_df = pd.read_csv('data/tx_subInj.csv', parse_dates=['year_id'], dtype={'FIPS': object})

    return disease_df
