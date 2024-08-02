import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Memuat dataset
hour_dt = pd.read_csv("hour.csv")
hour_dt['dteday'] = pd.to_datetime(hour_dt['dteday'])

# Menghitung jumlah penyewaan per musim
season_counts = hour_dt.groupby('season')['cnt'].sum().reset_index()
season_counts['season'] = season_counts['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})

# Menghitung jumlah penyewaan per jam
hour_counts = hour_dt.groupby('hr')['cnt'].sum().reset_index()

# Menghitung jumlah penyewaan berdasarkan pengguna kasual dan terdaftar
user_counts = hour_dt.groupby(['hr'])[['casual', 'registered']].sum().reset_index()

# Membuat aplikasi Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard Penyewaan Sepeda'),

    html.Div(children='''
        Analisis penyewaan sepeda berdasarkan musim, jam, dan tipe pengguna.
    '''),

    dcc.Graph(
        id='season-graph',
        figure=px.bar(season_counts, x='season', y='cnt', title='Jumlah Penyewaan Sepeda per Musim', 
                       labels={'season': 'Musim', 'cnt': 'Jumlah Penyewaan'}, 
                       color='cnt', color_continuous_scale=px.colors.sequential.Viridis)
    ),

    dcc.Graph(
        id='hour-graph',
        figure=px.line(hour_counts, x='hr', y='cnt', title='Jumlah Penyewaan Sepeda per Jam', 
                       labels={'hr': 'Jam', 'cnt': 'Jumlah Penyewaan'}, markers=True)
    ),

    dcc.Graph(
        id='user-graph',
        figure=px.line(user_counts, x='hr', y='casual', title='Jumlah Penyewaan Sepeda per Jam berdasarkan Tipe Pengguna',
                       labels={'hr': 'Jam', 'casual': 'Pengguna Kasual', 'registered': 'Pengguna Terdaftar'},
                       markers=True).add_scatter(x=user_counts['hr'], y=user_counts['registered'], mode='lines+markers', name='Pengguna Terdaftar')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



st.header('Dicoding Collection Dashboard :sparkles:')

