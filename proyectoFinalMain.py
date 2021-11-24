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


emision = pd.read_excel("./datos/emisionCO2.xlsx")
pais1=emision['Entity'].values
years1=emision['Year'].values
emisiones1=emision['Annual CO2 emissions (per capita)'].values

lluvias=pd.read_excel("./datos/lluvia.xlsx")


def filtrar(lista1,lista2,lista3):
    listaT1=[]
    listaT2=[]
    listaT3=[]
    for i in range(len(lista1)):
        if(lista3[i]>=1990 and lista3[i]<=2014):
            listaT1.append(lista1[i])
            listaT2.append(lista2[i])
            listaT3.append(lista3[i])
    return [listaT1,listaT2,listaT3]

listaTemp=filtrar(pais1,emisiones1,years1)
pais1=listaTemp[0]
emisiones1=listaTemp[1]
years1=listaTemp[2]

total=0;
for i in emisiones1:
    total+=i

paiselect=["Afghanistan","Mundo"]


def sumarValues(paisName):
    global pais1,emisiones1
    total=0
    
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            total+=emisiones1[i]
    return total
def yearsValues(paisName):
    global pais1,emisiones1,years1
    lTemp=[[],[]]
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            lTemp[0].append(years1[i])
            lTemp[1].append(emisiones1[i])
    return lTemp



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(html.Div(html.Div([
    dcc.Input(id="names", type="text", value="Afghanistan",style={'display':'none'}),
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
        return pais1[names["row"]+(page*25)]

@app.callback(
    Output("line-chart", "figure"), 
    [Input("names", "value")])
def update_line_chart(pais1):
    
    fig = px.line(emision, 
        x=yearsValues(pais1)[0], y=yearsValues(pais1)[1])
    fig.update_xaxes(title_text="Año")
    fig.update_yaxes(title_text="Emision de CO2")
    fig.update_layout(legend_title_text = "dd")
    return fig

app.run_server(debug=True)
