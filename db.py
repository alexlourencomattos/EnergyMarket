import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from datetime import date, timedelta
import os
import tempfile
import matplotlib.pyplot as plt
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
def conexao():
    conn = psycopg2.connect(host='postgres.focusenergia.com.br' , port=5432 , database='SeriesTemporaisInmet' , user='focus.energia' ,
                password='Ppn2Vks4bZeTgCXAqyYRqTDFi')
    cnx=psycopg2.connect(host='postgres.focusenergia.com.br' , port=5432 , database='SeriesTemporaisCptec', user='focus.energia' ,
                password='Ppn2Vks4bZeTgCXAqyYRqTDFi')
    query = """ select data, 
                          macro_bacia, 
                          sub_bacia, 
                          valor
                          from 
                          series_diarias.precipitacao_bacia"""
    query_dessem = """ select previsto_em, 
                          previsto_para, 
                          submercado, 
                          carga
                          from 
                          series_diarias.previsao_carga_dessem"""
    return cnx, query
""" query=conexao()[1]
cnx=conexao()[0]
chuva = pd.read_sql(query, cnx)
today = date.today()
day = today - timedelta(days = 14)
day, today

print(chuva.head())
chuva_hoje_grande = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Grande')]
chuva_hoje_iguacu = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Iguacu')]
chuva_hoje_paranaiba = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Paranaiba')]
chuva_hoje_tiete = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Tiete')]
chuva_hoje_itaipu = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Itaipu')]
chuva_hoje_paranapanema = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Paranapanema')]
chuva_hoje_sf = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Sao Francisco')]
chuva_hoje_tc = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Tocantins')]
chuva_hoje_uruguai = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Uruguai')]
chuva_hoje_parana = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Parana')]
chuva_hoje_madeira = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Madeira')]
chuva_hoje_paraguai = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Paraguai')]
chuva_hoje_xingu = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Xingu')]
chuva_hoje_tp = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Teles Pires')]
chuva_hoje_paraguacu = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Paraguaçu')]
chuva_hoje_itabapoana = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Itabapoana')]
chuva_hoje_doce = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Doce')]
chuva_hoje_mucuri = chuva[(chuva['data']>day) & (chuva['macro_bacia']=='Mucuri')]

chuva_hoje_grande.head() """