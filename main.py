# This is a sample Python script.
import psycopg2
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
from db import conexao

# Criação do layout do dashboard

query=conexao()[1]
cnx=conexao()[0]
chuva = pd.read_sql(query, cnx)
import os
import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State


# Função que salva o arquivo PDF na pasta de downloads
def save_file(name, content):
    """Salva o arquivo em uma pasta de downloads."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(os.path.expanduser("~"), "Downloads", name), "wb") as f:
        f.write(base64.decodebytes(data))


# Criação do layout do dashboard
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Histórico de Chuva'),

    html.Div(children='''
        Visualização dos dados de precipitação por bacia e sub-bacia.
    '''),

    # Adicionando uma mensagem de feedback para o usuário
    html.Div(id='output-data-upload'),

    dcc.Graph(
        id='precipitacao-bacia: Grande',
        figure={
            'data': [ 
                go.Scatter(
                    x=chuva[chuva['macro_bacia']=='Grande']['data'],  # Dados do eixo x
                    y=chuva[chuva['macro_bacia']=='Grande']['valor'],  # Dados do eixo y
                    mode='markers',
                    marker=dict(size=10))
                # Seus dados e gráficos aqui
            ],
            'layout': {
                # Seu layout aqui
            }
        }
    ),
    dcc.Graph(
        id='precipitacao-bacia',
        figure={
            'data': [ 
                go.Scatter(
                    x=chuva[chuva['macro_bacia']=='Uruguai']['data'],  # Dados do eixo x
                    y=chuva[chuva['macro_bacia']=='Uruguai']['valor'],  # Dados do eixo y
                    mode='markers',
                    marker=dict(size=10))
                # Seus dados e gráficos aqui
            ],
            'layout': {
                # Seu layout aqui
            }
        }
    )
])


# Função que lida com o upload do arquivo
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(content, name):
    if content is not None:
        # Salva o arquivo PDF na pasta de downloads
        save_file(name, content)
        return html.Div([
            'O arquivo ', html.B(name), ' foi salvo na pasta de downloads.'
        ])


# Execução do dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
