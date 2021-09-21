import dash
from dash.development.base_component import Component
from dash.html import Div
from dash.html.Col import Col
from dash.html.H3 import H3
from dash.html.Span import Span
from dash_bootstrap_components._components.Card import Card
import dash_core_components as dcc
import dash_html_components as html
from flask.scaffold import F
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import pyodbc 
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

############################# BANCO DE DADOS
# ----------------- SELECT I 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=4A422DR3Z;DATABASE=imp-cgdf;Trusted_Connection=yes;')
def connectSQLServer(conn):
    connSQLServer = conn
    return connSQLServer
sql_query = (''' SELECT nome, tonner, dt, total_cilindro FROM impressoras_graficos ORDER BY tonner ''')
sql_query3 = (''' SELECT nome, dt, total_cilindro FROM impressoras_graficos ORDER BY total_cilindro ''')

# ----------------- SELECT II
sql_query2 = (''' select dt, 'off' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras_graficos] 
where [total_impressao] like '0' group by dt
union all
select dt, 'on' as conexao, sum(1) as qtd from [imp-cgdf].[dbo].[impressoras_graficos] 
where [total_impressao] not like '0' group by dt ''')

df = pd.read_sql(sql_query,conn)
df2 = pd.read_sql(sql_query2,conn)
df3 = pd.read_sql(sql_query3,conn)

############################# TRATAMENTO DE DADOS

qtd_offline = df2['qtd'][0] 
qtd_online = df2['qtd'][1]

############################# GRAFICOS
fig = px.bar(df, x=(df["nome"]), y=(df["tonner"]), barmode="group")
fig2 = px.bar(df3, x=(df3["nome"]), y=(df["total_cilindro"]), barmode="group") 


############################# LAYOUT
app.layout = dbc.Container(children=[
    
    ############################# HEADER
    html.Div([
        #------------------- TITULO
        html.H2(children='Controladoria Geral do Distrito Federal - CGDF'),
        # ------------------- DESCRIÇÃO I
        html.Div(children='''Sistema de monitoramento de impressoras'''),
    ]),
   
    ################### CARDS
    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('ONLINE: '),
                html.H3(style={"color": "#adfc92"}, children= qtd_online),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão1" )
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('OFFLINE :'),
                html.H3(style={"color": "#ff0000"}, children= qtd_offline),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão2" )
            ]) 
        ]),
    ]),   

    # ------------------- BOTÃO ATUALIZAR
    
    dbc.Button("Atualizar", color="success", block=True),

    
    # ------------------- DESCRIÇÃO II

    html.H3(id= 'text', children='Buscar por:'),

    # ------------------- MENU DROPDOWN
    dbc.Row([
        dbc.Col([
            #----- TIPO DE DADO
            dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Tonner', 'value': 'TONNER'},
                {'label': 'Cilindro', 'value': 'CILINDRO'},
                {'label': 'Consumo', 'value': 'CONSUMO'}
            ],
            value='TONNER'
            ),
        ]),
        #----- DATA
        dbc.Col([
            dcc.DatePickerSingle(
                id='date-picker',
            )
        ]),
    ]),   


    # ------------------- GRAFICO I
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

])



@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)



def changeText(value):
    if value == 'TONNER':
        return px.bar(df, x=(df["nome"]), y=(df["tonner"]), barmode="group")
    elif value == 'CILINDRO':
        return px.bar(df3, x=(df3["nome"]), y=(df3["total_cilindro"]), barmode="group") 
    return
    

if __name__ == '__main__':
    app.run_server(debug=True)