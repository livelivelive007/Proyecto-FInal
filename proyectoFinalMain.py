from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import re
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.tips()
emision = pd.read_excel("./datos/emision.xlsx")
pais=emision['Entity'].values
years=emision['Year'].values
emisiones=emision['Annual CO2 emissions (per capita)'].values
total=0;
for i in emisiones:
    total+=i

paiselect=["Afghanistan","Mundo"]


def sumarValues(paisName):
    global pais,emisiones
    total=0
    
    for i in range(len(pais)):
        if(pais[i]==paisName):
            total+=emisiones[i]
    return total
def yearsValues(paisName):
    global pais,emisiones,years
    lTemp=[[],[]]
    for i in range(len(pais)):
        if(pais[i]==paisName):
            lTemp[0].append(years[i])
            lTemp[1].append(emisiones[i])
    return lTemp



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(html.Div(html.Div([
    dcc.Input(id="names", type="text", value="Afghanistan"),
    dcc.Input(id="values", type="text", value="Annual CO2 emissions (per capita)", style={'display':'none'}),
    html.Div([(html.Div([dcc.Graph(id="line-chart")],className="row")),(html.Div([dcc.Graph(id="pie-chart")],className="row"))],className="col"),
    html.Div([dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in emision.columns],
        
        data=emision.to_dict('records'),
        page_size=25,
        style_cell=dict(textAlign='center'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
    )],className="col"),
    
],className="row"),className="container"),className="container-fluid")

@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    global paiselect
    paiselect[0]=names
    valuesselectTemp=[sumarValues(names),total-sumarValues(names)]
    fig = px.pie(emision, values=valuesselectTemp, names=paiselect)
    return fig

@app.callback(
    Output("names", "value"), 
    [Input("table", "active_cell"),Input("names", "value"),Input("table", "page_current")])
def change(names,actual,page):
    if(page==None):
        page=0
    
    if(names==None or names["column"]!=0):
        return actual
    else:
        return pais[names["row"]+(page*25)]

@app.callback(
    Output("line-chart", "figure"), 
    [Input("names", "value")])
def update_line_chart(pais):
    #mask = df.continent.isin(continents)
    fig = px.line(emision, 
        x=yearsValues(pais)[0], y=yearsValues(pais)[1])
    return fig

app.run_server(debug=True)
