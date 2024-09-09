from dash import Dash, html, dcc, Input, Output, callback
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
app.title = "MCM7183 Exercise 3"
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/wenjiun/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")

image_path = 'assets/logo-mmu.png'

app.layout = [html.H1('MCM7183 Exercise 3'), 
              html.Img(src=image_path), 
              dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='country_selected'), 
              dcc.Graph(id="graph_scatter"), 
              dcc.Slider(1960, 2020, 5, value=2020, id='year_selected'),
              dcc.Graph(id="graph_pie")]

@callback(
    Output('graph_scatter', 'figure'),
    Output('graph_pie', 'figure'),
    Input('country_selected', 'value'),
    Input('year_selected', 'value')
)
def update_figure(country, year):
    subset_Country = df[df['country'].isin([country])]
    fig = px.scatter(subset_Country, x="year", y="gdp")

    subset_year = df[df['year'].isin([year])]
    subset_year_Asia = subset_year[subset_year['state'].isin(["Asia"])]
    subset_year_Africa = subset_year[subset_year['state'].isin(["Africa"])]
    subset_year_America = subset_year[subset_year['state'].isin(["America"])]
    subset_year_Europe = subset_year[subset_year['state'].isin(["Europe"])]
    subset_year_Oceania = subset_year[subset_year['state'].isin(["Oceania"])]
    pie_data = [sum(subset_year_Asia['gdp']),sum(subset_year_Africa['gdp']),sum(subset_year_America['gdp']),sum(subset_year_Europe['gdp']),sum(subset_year_Oceania['gdp'])];
    mylabels = ["Asia", "Africa", "America", "Europe","Oceania"]
    pie_df = {'Continent': mylabels,'GDP': pie_data}
    fig2 = px.pie(pie_df,values="GDP",names="Continent")

    return fig, fig2

if __name__ == '__main__':
    app.run(debug=True)
