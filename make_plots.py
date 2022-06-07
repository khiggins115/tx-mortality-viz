import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    geo_counties = json.load(response)


def plot_mortality_lines(df, select_mortality_df, sex):
    fig, ax = plt.subplots(1, 1, figsize=(25, 12))

    #subset df based on sex
    df_plot = df[df['sex'] == sex]
    
    
    title_string = select_mortality_df + ": Granular Mortality Rates (" + sex + ") 1980 - 2014"
    ax.set_title(title_string, fontdict={'fontsize': 25, 'fontweight': 18}, pad=12)
    df_plot.groupby(['year_id','cause_name']).mean()['mx'].unstack().plot(ax=ax)
    ax.set_xlabel('Year', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    ax.set_ylabel('Deaths per 100K', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    plt.tight_layout()

    return fig

def plot_mortality_heatmaps(disease, cause_of_death, chosen_year, sex):
    
    disease['year'] = disease['year_id'].dt.year

    df_plot = disease[(disease['sex'] == sex) & (disease['year'] == chosen_year) & (disease['cause_name'] == cause_of_death)]
    #df_plot = disease[(disease['sex'] == sex) & (disease['cause_name'] == cause_of_death)]

    fig = px.choropleth(
        data_frame=df_plot,
        locations='FIPS', geojson=geo_counties,
        #width=900, height=600,
        hover_name='location_name',
        color='mx',
        center={'lat': 31.9686, 'lon': -99.9018},
        scope='usa',
        #zoom=5,
        title=cause_of_death + "  Heatmap"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        legend_yanchor="top",
        legend_x=-2
    )

    return fig



def plot_mortality_bars(df, select_mortality_df, year, sex):
    df_plot = df[df['sex'] == sex]
    plot_title = 'US ' + select_mortality_df + ' Mortality: ' + str(year) + ' (' + sex + ')'

    # grouping rates of infectious disease mortality
    fig, ax = plt.subplots(figsize=(60, 40))
    #fig.suptitle("Infectious Disease Mortality by Sex")
    ax.set_title(plot_title, fontdict={'fontsize': 50, 'fontweight': 30}, pad=15)
    df_plot.groupby(['cause_name']).mean()['mx'].plot(ax=ax, kind='barh')
    ax.set_xlabel('Deaths per 100K', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    ax.tick_params(axis='x', labelsize=40)
    ax.set_ylabel('Cause Name', fontdict={'fontsize': 25, 'fontweight': 25}, labelpad=15)
    ax.tick_params(axis='y', labelsize=50)
    plt.tight_layout()

    return fig
