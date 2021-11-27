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

RegionesDic=['Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern HemisphereNorthern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere']
PaisesDic=['Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'Faeroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North America', 'North Korea', 'North Macedonia', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
DiccionarioRegiones={}
for i in range(len(RegionesDic)):
    DiccionarioRegiones[PaisesDic[i]]=RegionesDic[i]
titulos=['Entity','Year','Annual CO2 emissions (per capita)','Average monthly precipitation','Total GHG emissions excluding LUCF (CAIT)','Region']

emision = pd.read_excel("./datos/emisionCO2.xlsx")
pais1=emision['Entity'].values
years1=emision['Year'].values
emisiones1=emision['Annual CO2 emissions (per capita)'].values


lluvia=pd.read_excel("./datos/lluvia.xlsx")
pais2=lluvia['Entity'].values
years2=lluvia['Year'].values
lluvias=lluvia['Average monthly precipitation'].values


emision2 = pd.read_excel("./datos/emisionGHC.xlsx")
pais3=emision2['Entity'].values
years3=emision2['Year'].values
emisiones2=emision2['Total GHG emissions excluding LUCF (CAIT)'].values
listaPP=[]
#for i in pais1:
 #   if (not(i in listaPP)):
  #     listaPP.append(i)

#print(listaPP)


            


diccionario=emision.to_dict('records')
for i in titulos:
    print(type(i))
def filtrar():
    listaT1=[]
    listaT2=[]
    listaT3=[]
    listaT4=[]
    listaT5=[]
    listaT6=[]
    i=0
    x=0
    y=0
    val=False
    while i<len(pais1):
        if(years1[i]>=1990 and years1[i]<=2014):
            if pais1[i]==pais2[x] and years1[i]==years2[x]:
                
                if pais1[i]==pais3[y] and years1[i]==years3[y]:
                    listaT1.append(pais1[i])
                    listaT2.append(emisiones1[i])
                    listaT3.append(years1[i])
                    listaT4.append(diccionario[i])
                    listaT4[-1]['Average monthly precipitation']=lluvias[x]
                    listaT4[-1]['Total GHG emissions excluding LUCF (CAIT)']=emisiones2[y]
                    listaT4[-1]['Region']=DiccionarioRegiones[pais1[i]]
                    listaT5.append(lluvias[x])
                    listaT6.append(emisiones2[y])
                    x=0
                    y=0
                    i+=1
                else:
                    y+=1
            else:
                x+=1
        else:
            i+=1
        if(x>=len(pais2)):
            val=True
            x=0
        if(y>=len(pais3)):
            val=True
            x=0
            y=0
        if(val):
            i+=1
            val=False
        
        
    return [listaT1,listaT2,listaT3,listaT4,listaT5,listaT6]


listaTemp=filtrar()
pais1=listaTemp[0]
emisiones1=listaTemp[1]
years1=listaTemp[2]
#print(diccionario)
diccionario=listaTemp[3]
lluvias=listaTemp[4]
emisiones2=listaTemp[5]
total=0;
pais11=pais1
emisiones11=emisiones1
years11=years1
lluvias11=lluvias
emisiones22=emisiones2
for i in emisiones1:
    total+=i
    
lltt=[]
for i in pais1:
    if(not(i in lltt)):
        lltt.append(i)
print(len(lltt))        
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
    max1=0
    max2=0
    max3=0
    lTemp=[[],[],[],[]]
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            max1+=emisiones1[i]
            max2+=lluvias[i]
            max3+=emisiones2[i]
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            lTemp[0].append(years1[i])
            lTemp[1].append((emisiones1[i]*100)/max1)
            lTemp[2].append((lluvias[i]*100)/max2)
            lTemp[3].append((emisiones2[i]*100)/max3)
    return lTemp



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#Pais
app.layout = html.Div([html.Div(html.Div(html.Div([
    dcc.Input(id="names", type="text", value="Afghanistan",style={'display':'none'}),
    dcc.Input(id="pruebast", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="values", type="text", value="Annual CO2 emissions (per capita)", style={'display':'none'}),
    html.Div([(html.Div([dcc.Graph(id="line-chart")],className="row rowline")),(html.Div([dcc.Graph(id="pie-chart")],className="row rowPie"))],className="col"),
    html.Div([html.Div([html.Div([dcc.Input(id="search", type="search",className="form-control")],className="col colInputSearch"),html.Div([html.Label('Vista por paises')],className="col"),html.Div([html.Button('Ver por Regiones',className="regionButton")],className="col")],className="row"),dash_table.DataTable(
        #autoWidth= "false",
        id='table',
        columns=[{"name": i, "id": i} for i in titulos],
        style_cell = dict(textAlign="center",fontSize=10),
        data=diccionario,
        page_size=25,
        
       
        style_header=dict(backgroundColor="paleturquoise"),
        
        fill_width=False
    )],className="col"),
    
],className="row"),className="container"),style={'margin-top':'2%'},className="container-fluid porPais"),

#Region
html.Div(html.Div(html.Div([
    dcc.Input(id="namesR", type="text", value="Afghanistan",style={'display':'none'}),
    dcc.Input(id="pruebastR", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="valuesR", type="text", value="Annual CO2 emissions (per capita)", style={'display':'none'}),
    html.Div([(html.Div([dcc.Graph(id="line-chartR")],className="row rowline")),(html.Div([dcc.Graph(id="pie-chartR")],className="row rowPie"))],className="col"),
    html.Div([html.Div([html.Div([dcc.Input(id="searchR", type="search",className="form-control")],className="col colInputSearch"),html.Div([html.Label('Vista por regiones')],className="col"),html.Div([html.Button('Ver por paises', className="paisButton")],className="col")],className="row"),dash_table.DataTable(
        #autoWidth= "false",
        id='tableR',
        columns=[{"name": i, "id": i} for i in titulos],
        style_cell = dict(textAlign="center",fontSize=10),
        data=diccionario,
        page_size=25,
        
       
        style_header=dict(backgroundColor="paleturquoise"),
        
        fill_width=False
    )],className="col"),
    
],className="row"),className="container"),style={'margin-top':'2%','display':'none'},className="container-fluid porRegion")
















                       ])

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
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[1], name='CO2',
                         line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[2], name='Lluvia',
                         line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[3], name='GHC',
                         line=dict(color='brown', width=4)))

    fig.update_xaxes(title_text="Año")
    fig.update_yaxes(title_text="Emision de CO2")
    fig.update_layout(plot_bgcolor='rgb(78,205,196)',paper_bgcolor='rgb(239,241,243)')
    return fig

@app.callback(
    Output("table", "data"), 
    [Input("search", "value")])
def updateTable(valor):
        global pais1,emisiones1,years1,lluvias,emisiones2
        
        if(valor is None):
            pais1=pais11
            emisiones1=emisiones11
            years1=years1
            lluvias=lluvias11
            emisiones2=emisiones22
            return diccionario
        else:
            dTemp=[]
            pais1=[]
            emisiones1=[]
            years1=[]
            lluvias=[]
            emisiones2=[]
            for i in diccionario:
                if(i['Entity'].upper()== str(valor).upper() or i['Entity'].upper().find(str(valor).upper())!=-1 ):
                    dTemp.append(i)

            for i in dTemp:
                pais1.append(i['Entity'])
                emisiones1.append(i['Annual CO2 emissions (per capita)'])
                years1.append(i['Year'])
                lluvias.append(i['Average monthly precipitation'])
                emisiones2.append(i['Total GHG emissions excluding LUCF (CAIT)'])
            return dTemp




app.run_server(debug=False)
