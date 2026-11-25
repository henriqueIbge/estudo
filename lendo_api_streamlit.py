import json
import requests
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
from streamlit.components.v1 import html#novo. st.html
import streamlit.components.v1 as components# novo st.iframe
import extra_streamlit_components as stx
from streamlit_javascript import st_javascript
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import geobr
#import pygeos
import geopandas as gpd
import plotly.express as px
import base64
from streamlit_pdf_viewer import pdf_viewer
from streamlit import session_state as ss
from pathlib import Path
tabelas_todo={}
tabelas={}


        
#Horticultura
tabelas[6953]='''Número de estabelecimentos agropecuários com horticultura
, Quantidade produzida na horticultura, Quantidade vendida de produtos da horticultura
, Valor da produção da horticultura e Valor da venda de produtos da horticultura
, por tipologia, produtos da horticultura, condição do produtor em relação às terras
e grupos de atividade econômica'''
tabelas[6954]='''Número de estabelecimentos agropecuários com horticultura
, Quantidade produzida na horticultura, Quantidade vendida de produtos da horticultura
, Valor da produção da horticultura e Valor da venda de produtos da horticultura
, por tipologia, produtos da horticultura e grupos de área total'''
#Lavouras Permanentes
tabelas[6955]='''Produção, Valor da produção, Venda, Valor da venda, Colheita, Área plantada
e Efetivos das plantações da lavoura permanente nos estabelecimentos agropecuários
, por tipologia, produtos da lavoura permanente, condição do produtor em relação às terras
e grupos de atividade econômica'''
tabelas[6956]='''Produção, Valor da produção, Venda, Valor da venda, Colheita, Área plantada
e Efetivos das plantações da lavoura permanente nos estabelecimentos agropecuários
, por tipologia, produtos da lavoura permanente e grupos de área total'''

#Lavouras Temporárias
tabelas[6957]='''Produção, Valor da produção, Venda, Valor da venda e Área colhida da lavoura
temporária nos estabelecimentos agropecuários, por tipologia, produtos da lavoura temporária
, condição do produtor em relação às terras e grupos de atividade econômica'''
tabelas[6958]='''Produção, Valor da produção, Venda, Valor da venda e Área colhida da lavoura
temporária nos estabelecimentos agropecuários, por tipologia, produtos da lavoura temporária
, tipo de semente e grupos de área colhida'''
tabelas[6959]='''Produção, Valor da produção, Venda, Valor da venda e Área colhida da lavoura temporária
nos estabelecimentos agropecuários, por tipologia, produtos da lavoura temporária e grupos
de área total'''
#movimentação financeira
tabelas[6895]='''Número de estabelecimentos agropecuários que obtiveram financiamento, por tipologia
, agente financeiro responsável pelo financiamento, condição do produtor em relação às terras
, grupos de atividade econômica, recursos provenientes de programas governamentais de crédito
e grupos de área total'''	
tabelas[6896]='''Número de estabelecimentos agropecuários que obtiveram financiamento, por tipologia
, finalidade do financiamento, condição do produtor em relação às terras, agente financeiro responsável pelo financiamento
, grupos de atividade econômica e grupos de área total'''
tabelas[6897]='''Número de estabelecimentos agropecuários com produção e Valor da produção dos estabelecimentos
agropecuários, por tipologia, tipo de produção, condição do produtor em relação às terras
e grupos de atividade econômica'''
tabelas[6898]='''Número de estabelecimentos agropecuários com produção e Valor da produção dos estabelecimentos
agropecuários, por tipologia, tipo de produção, classes de valor da produção e grupos de área total'''
tabelas[6899]='''Número de estabelecimentos agropecuários que realizaram despesas e Valor das despesas
realizadas pelos estabelecimentos agropecuários, por tipologia, tipo de despesa, condição do produtor
em relação às terras e grupos de atividade econômica'''
tabelas[6900]='''Número de estabelecimentos agropecuários que realizaram despesas e Valor das despesas
realizadas pelos estabelecimentos agropecuários, por tipologia, tipo de despesa e grupos de área total'''
tabelas[6901]='''Número de estabelecimentos agropecuários que obtiveram receitas ou com outras rendas
do produtor e Valor das receitas ou rendas obtidas pelos estabelecimentos agropecuários, por tipologia
, receitas do estabelecimento e outras rendas do produtor, condição do produtor em relação às terras
e grupos de atividade econômica'''
tabelas[6902]='''Número de estabelecimentos agropecuários que obtiveram receitas ou com outras rendas
do produtor e Valor das receitas ou rendas obtidas pelos estabelecimentos agropecuários, por tipologia
, receitas do estabelecimento e outras rendas do produtor e grupos de área total'''
#pecuaria
tabelas[6906]='''Número de estabelecimentos agropecuários, por tipologia, controle de doenças e/ou parasitas
, suplementação alimentar e beneficiamento, condição do produtor em relação às terras, origem da orientação técnica
recebida e grupos de área total'''
tabelas[6907]='''Número de estabelecimentos agropecuários com efetivo da pecuária e Número de cabeças, por tipologia
, espécie da pecuária e condição do produtor em relação às terras'''
tabelas[6908]='''Número de estabelecimentos agropecuários com efetivo da pecuária e Número de cabeças, por tipologia
, espécie da pecuária, grupos de atividade econômica e grupos de área total'''
tabelas[6910]='''Número de estabelecimentos agropecuários com bovinos, Efetivos e Venda, por tipologia, condição do produtor
em relação às terras, grupos de cabeças de bovinos e grupos de atividade econômica'''
tabelas[6911]='''Número de estabelecimentos agropecuários com bovinos, Efetivos e Venda, por tipologia, grupos de área de pastagem
e grupos de área total'''
tabelas[6912]='''Número de estabelecimentos agropecuários que produziram leite de vaca, Vacas ordenhadas nos estabelecimentos agropecuários
, Quantidade produzida de leite de vaca, Valor da produção de leite de vaca, Número de estabelecimentos agropecuários que venderam leite de vaca cru
, Quantidade vendida de leite de vaca cru e Valor da venda de leite de vaca cru, por tipologia, condição do produtor em relação às terras
e grupos de cabeças de bovinos'''
tabelas[6913]='''Número de estabelecimentos agropecuários que produziram leite de vaca, Vacas ordenhadas nos estabelecimentos agropecuários
, Quantidade produzida de leite de vaca, Valor da produção de leite de vaca, Número de estabelecimentos agropecuários que venderam leite de vaca cru
, Quantidade vendida de leite de vaca cru e Valor da venda de leite de vaca cru, por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6918]='''Número de estabelecimentos agropecuários com bubalinos, Efetivos, Venda e Produção de leite, por tipologia, condição do produtor em relação às terras
, sexo do produtor e grupo de cabeças de bubalinos'''
tabelas[6919]='''Número de estabelecimentos agropecuários com bubalinos, Efetivos, Venda e Produção de leite, por tipologia, grupos de atividade econômica
e grupos de área total'''
tabelas[6920]='''Número de estabelecimentos agropecuários com equinos, Número de cabeças de equinos nos estabelecimentos agropecuários, Número de estabelecimentos agropecuários
que venderam equinos, Número de cabeças de equinos vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de equinos nos estabelecimentos agropecuários, por tipologia
, condição do produtor em relação às terras e grupos de cabeças de equinos'''
tabelas[6921]='''Número de estabelecimentos agropecuários com equinos, Número de cabeças de equinos nos estabelecimentos agropecuários, Número de estabelecimentos agropecuários
que venderam equinos, Número de cabeças de equinos vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de equinos nos estabelecimentos agropecuários, por tipologia
, grupos de atividade econômica e grupos de área total'''
tabelas[6922]='''Número de estabelecimentos agropecuários com asininos, Número de cabeças de asininos nos estabelecimentos agropecuários, Número de estabelecimentos agropecuários
que venderam asininos, Número de cabeças de asininos vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de asininos nos estabelecimentos agropecuários
, por tipologia, condição do produtor em relação às terras e grupos de cabeças de asininos'''
tabelas[6923]='''Número de estabelecimentos agropecuários com asininos, Número de cabeças de asininos nos estabelecimentos agropecuários
, Número de estabelecimentos agropecuários que venderam asininos, Número de cabeças de asininos vendidas nos estabelecimentos agropecuários
e Valor da venda de cabeças de asininos nos estabelecimentos agropecuários, por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6924]='''Número de estabelecimentos agropecuários com muares, Número de cabeças de muares nos estabelecimentos agropecuários, Número de estabelecimentos agropecuários
que venderam muares, Número de cabeças de muares vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de muares nos estabelecimentos agropecuários, por tipologia
, condição do produtor em relação às terras e grupos de cabeças de muares'''
tabelas[6925]='''Número de estabelecimentos agropecuários com muares, Número de cabeças de muares nos estabelecimentos agropecuários, Número de estabelecimentos agropecuários
que venderam muares, Número de cabeças de muares vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de muares nos estabelecimentos agropecuários
, por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6926]='''Número de estabelecimentos agropecuários com suínos, Efetivos e Venda, por tipologia, condição do produtor em relação às terras e grupo de cabeças de suínos'''
tabelas[6927]='''Número de estabelecimentos agropecuários com suínos, Efetivos e Venda, por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6928]='''Número de estabelecimentos agropecuários com caprinos, Efetivos, Venda e Produção de leite, por tipologia, condição do produtor
em relação às terras e grupo de cabeças de caprinos'''
tabelas[6929]='''Número de estabelecimentos agropecuários com caprinos, Efetivos, Venda e Produção de leite, por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6930]='''Número de estabelecimentos agropecuários com ovinos, Efetivos, Venda, Produção de lã e Produção de leite, por tipologia
, condição do produtor em relação às terras e grupo de cabeças de ovinos'''
tabelas[6931]='''Número de estabelecimentos agropecuários com ovinos, Efetivos, Venda, Produção de lã e Produção de leite,
por tipologia, grupos de atividade econômica e grupos de área total'''
tabelas[6933]='''Número de estabelecimentos agropecuários com codornas, Efetivos, Produção de ovos de codorna e Venda de ovos de codorna
, por tipologia, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total'''
tabelas[6934]='''Número de estabelecimentos agropecuários com coelhos, Número de cabeças de coelhos nos estabelecimentos agropecuários
, Número de cabeças de coelhos vendidas nos estabelecimentos agropecuários e Valor da venda de cabeças de coelhos nos estabelecimentos agropecuários
, por tipologia, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total'''
tabelas[6935]='''Número de estabelecimentos agropecuários com apicultura e Venda de produtos, Total de caixas de abelha e Quantidade de mel
e cera de abelha, geleia real, própolis e pólen vendidos, por tipologia, condição do produtor em relação às terras, grupos de atividade econômica
e grupos de área total'''
tabelas[6936]='''Número de estabelecimentos agropecuários com sericicultura, Produção e Venda de casulos de bicho-da-seda, por tipologia
, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total'''
tabelas[6937]='''Número de estabelecimentos agropecuários que venderam produtos da aquicultura, Quantidade vendida de produtos da aquicultura
e Valor da venda de produtos da aquicultura, por tipologia, espécie criada na aquicultura, condição do produtor em relação às terras
, grupos de atividade econômica e grupos de área total'''
tabelas[6938]='''Número de estabelecimentos agropecuários com aquicultura, por tipologia, espécie criada na aquicultura, condição do produtor
em relação às terras, grupos de atividade econômica e grupos de área total'''
tabelas[6939]='''Número de estabelecimentos agropecuários com ranicultura, Quantidade vendida de carne de rãs e Valor da venda de carne de rãs
, por tipologia, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total'''
tabelas[6940]='''Número de estabelecimentos agropecuários com galinhas, galos, frangos, frangas e pintos
, Efetivos, Venda, Produção de ovos e Venda de ovos, por tipologia, grupos de cabeças e condição do produtor em relação às terras'''
tabelas[6941]='''Número de estabelecimentos agropecuários com galinhas, galos, frangos, frangas e pintos, Efetivos
, Venda, Produção de ovos e Venda de ovos, por tipologia, grupos de cabeças e grupos de atividade econômica'''
tabelas[6942]='''Número de estabelecimentos agropecuários com galinhas, galos, frangos, frangas e pintos, Efetivos, Venda
, Produção de ovos e Venda de ovos, por tipologia, grupos de cabeças e grupos de área total'''
tabelas[6943]='''Número de estabelecimentos agropecuários com mais de 200 cabeças de galinhas, galos, frangos, frangas e pintos
, Efetivos e composição do plantel na data de referência, por tipologia, condição do produtor em relação às terras e grupos de cabeças'''
tabelas[6944]='''Número de estabelecimentos agropecuários com mais de 200 cabeças de galinhas, galos, frangos, frangas e pintos
, Efetivos e composição do plantel na data de referência, por tipologia, grupos de atividade econômica e grupos de área total'''
#pessoal ocupado
tabelas[6884]='''Número de estabelecimentos agropecuários com pessoal ocupado, Pessoal ocupado em estabelecimentos agropecuários
, Número de estabelecimentos agropecuários com pessoal ocupado com laço de parentesco com o produtor e Pessoal ocupado em estabelecimentos
agropecuários com laço de parentesco com o produtor, por tipologia, sexo, faixas de idade, condição do produtor
em relação às terras e grupos de atividade econômica'''
tabelas[6885]='''Número de estabelecimentos agropecuários com pessoal ocupado, total, com laço e sem laço de parentesco com o produtor
e Pessoal ocupado em estabelecimentos agropecuários com laço e sem laço de parentesco com o produtor, total, permanentes, temporários
e parceiros, por tipologia, sexo, faixas de idade e grupos de área total'''
tabelas[6886]='''Número de estabelecimentos agropecuários com pessoal ocupado sem laço de parentesco com o produtor
e Pessoal ocupado em estabelecimentos agropecuários sem laço de parentesco com o produtor, total, permanentes, temporários e parceiros
, por tipologia, sexo, faixas de idade, condição do produtor em relação às terras e grupos de pessoal ocupado'''
tabelas[6887]='''Número de estabelecimentos agropecuários com pessoal ocupado e Pessoal ocupado em estabelecimentos agropecuários, por tipologia
, tipo de pessoal ocupado e grupos e classes de atividade'''
tabelas[6888]='''Número de estabelecimentos agropecuários e Pessoal ocupado em estabelecimentos agropecuários, por tipologia, tipo de pessoal ocupado
, classes de dias trabalhados, condição do produtor em relação às terras e grupos de atividade econômica'''
tabelas[6889]='''Número de estabelecimentos agropecuários e Pessoal ocupado em estabelecimentos agropecuários, por tipologia, tipo de pessoal ocupado
, classes de dias trabalhados, sexo do produtor e grupos de área total'''	
tabelas[6890]='''Número de estabelecimentos agropecuários, por tipologia, tipo de intermediador, condição do produtor em relação às terras
, grupos de atividade econômica e grupos de área total'''	
tabelas[6891]='''Número de estabelecimentos agropecuários, por tipologia, classes de dias de utilização da mão-de-obra
com intermediação de empreiteiro, condição do produtor em relação às terras, grupos de atividade econômica e grupos de área total'''
#silvicultura
tabelas[6945]='''Número de estabelecimentos agropecuários com espécies da silvicultura, Área cortada de espécies da silvicultura
e Número de pés existentes nos estabelecimentos agropecuários, por tipologia, espécies da silvicultura
, condição do produtor em relação às terras e grupos de atividade econômica'''
tabelas[6946]='''Número de estabelecimentos agropecuários com espécies da silvicultura, Área cortada de espécies da silvicultura
e Número de pés existentes nos estabelecimentos agropecuários, por tipologia, espécies da silvicultura e grupos de área total'''
tabelas[6947]='''Número de estabelecimentos agropecuários com produtos da silvicultura, Quantidade produzida na silvicultura
, Quantidade vendida de produtos da silvicultura, Valor da produção na silvicultura e Valor da venda de produtos da silvicultura
, por tipologia, produtos da silvicultura, condição do produtor em relação às terras e grupos de atividade econômica'''
tabelas[6948]='''Número de estabelecimentos agropecuários com produtos da silvicultura, Quantidade produzida na silvicultura
, Quantidade vendida de produtos da silvicultura, Valor da produção na silvicultura e Valor da venda de produtos da silvicultura
, por tipologia, produtos da silvicultura e grupos de área total'''
#confederação da agricultura e pecuária CNA
tabelas[6836]='''Número de estabelecimentos agropecuários com espécies da silvicultura, Área total dos estabelecimentos agropecuários
com espécies da silvicultura, Número de pés existentes nos estabelecimentos agropecuários e Área cortada de espécies da silvicultura
, por espécies da silvicultura, associação do produtor à cooperativa e/ou à entidade de classe, condição legal do produtor e grupos de área total'''
tabelas[6962]='''Número de estabelecimentos agropecuários e Área dos estabelecimentos agropecuários, por produtor possui DAP (Declaração de Aptidão ao PRONAF)
, uso de calcário e/ou outros corretivos do pH do solo, telefone, e-mail e internet e grupos de área total'''
tabelas[6963]='''Número de estabelecimentos agropecuários com uso de irrigação e Pessoal ocupado em estabelecimentos agropecuários com uso de irrigação
, por método utilizado para irrigação, escolaridade do produtor, classes de dias trabalhados e grupos de área total'''
tabelas[6964]='''Número de estabelecimentos agropecuários com uso de irrigação, por método utilizado para irrigação, escolaridade do produtor
, existência de energia elétrica, tipo de intermediador e grupos de área total	2017'''
tabelas[6965]='''Número de estabelecimentos agropecuários com lavoura temporária, Área total dos estabelecimentos agropecuários com lavoura temporária
, Quantidade produzida nas lavouras temporárias e Área colhida nas lavouras temporárias, por produtos da lavoura temporária
, origem da orientação técnica recebida e grupos de área total'''
tabelas[6966]='''Produção, Venda, Colheita, Área plantada e Efetivos das plantações da lavoura permanente nos estabelecimentos agropecuários
, por produtos da lavoura permanente, origem da orientação técnica recebida e grupos de área total'''
tabelas[6874]='''Número de estabelecimentos agropecuários e Número de tratores, implementos e máquinas existentes nos estabelecimentos agropecuários
, por tipologia, tratores, implementos e máquinas existentes no estabelecimento agropecuário, grupos de área de lavoura e grupos de área total'''	
tabelas[6877]='''Número de estabelecimentos agropecuários com veículos e Número de veículos existentes nos estabelecimentos agropecuários, por tipologia
, veículos existentes no estabelecimento agropecuário, grupos de área de lavoura e grupos de área total'''
tabelas[6895]='''Número de estabelecimentos agropecuários que obtiveram financiamento, por tipologia, agente financeiro responsável pelo financiamento
, condição do produtor em relação às terras, grupos de atividade econômica, recursos provenientes de programas governamentais de crédito e grupos de área total'''
tabelas[6896]='''Número de estabelecimentos agropecuários que obtiveram financiamento, por tipologia, finalidade do financiamento
, condição do produtor em relação às terras, agente financeiro responsável pelo financiamento, grupos de atividade econômica e grupos de área total'''

#obs: as duas tabelas finais são repetições de quadros anteriores


codtab_a=[['Horticultura',0,2], ['Lavouras Permanentes',2,4], ['Lavouras Temporárias',4,7],['Movimentação financeira',7,15],['Pecuária',15,48], ['Pessoal ocupado',48,56], ['Silvicultura',56,60], ['CNA',60,68]]
codtab_b=[6953, 6954, 6955, 6956, 6957, 6958, 6959, 6895, 6896, 6897, 6898, 6899, 6900, 6901, 6902, 6906, 6907, 6908, 6910, 6911,
           6912, 6913, 6918, 6919, 6920, 6921, 6922, 6923, 6924, 6925, 6926, 6927, 6928, 6929, 6930, 6931, 6933, 6934, 6935, 6936,
           6937, 6938, 6939, 6940, 6941, 6942, 6943, 6944, 6884, 6885, 6886, 6887, 6888, 6889, 6890, 6891, 6945, 6946, 6947, 6948,
           6836, 6962, 6963, 6964, 6965, 6966, 6874, 6877]

textos=list(tabelas.values())
cod_tabelas=list(tabelas.keys())

for ia in range(len(codtab_a)):
  tabtab={}
  for ib in range(codtab_a[ia][1],codtab_a[ia][2]):
    tabtab[codtab_b[ib]]=textos[ib]  
  tabelas_todo[codtab_a[ia][0]]=tabtab
  
grupo_tabelas=list(tabelas_todo.keys())#'Horticultura','Lavoura Permanente', etc....
list(tabelas_todo['Horticultura'].keys())#[6953,6954]
tabela_1=cod_tabelas[0]

def qual_tabela(codigo_tabela):
  global resposta
  global tabela_2
  tabela_2=codigo_tabela
  camdados1=r'https://servicodados.ibge.gov.br/api/v3/agregados/%s/metadados'%tabela_2
  resposta= requests.get(camdados1)
  #resposta.headers

##PESQUISA NAS APIS IBGE
#1º PASSO - VER TODAS AS PESQUISAS               https://servicodados.ibge.gov.br/api/v3/agregados
#2° VER TABELAS POR ASSUNTO                      https://servicodados.ibge.gov.br/api/v3/agregados?assunto=85
###ASSUNTOS:
##### extração vegetal assunto=75, floricultura=77, horticultura=76, lav_perm=24, lav_temp=23, leite=72
##### ovos de galinha=73, pecuária=40, pessoal ocupado = 45, produção vegetal=47, silvicultura=74, valor agropecuário=69, estoques=85
##### característca estab. agro = 43, condição do produtor = 44, abate=70, couro=71, agroindústria=78, receitas=88, PAM = 25 
#3º PASSO - VER OS METADADOS DAS TABELAS         https://servicodados.ibge.gov.br/api/v3/agregados/5802/metadados
#4º PASSO - FAZER OS FILTROS CONFORME METADADOS  https://servicodados.ibge.gov.br/api/v3/agregados/1030/periodos/-10/variaveis?classificacao&localidades=N1
assuntos_agro={'Extração vegetal':75, 'Floricultura':77,'Horticultura':76,'Lavoura permanente':24,'Lavoura temporária':23,
               'Leite':72, 'Ovos de galinha':73,'Pecuária':40,'Pessoal ocupado':45, 'Produção vegetal':47,'Silvicultura':74,
               'Valor agropecuário':69,'Estoques':85, 'característca do estabelecimento agro':43, 'Condição do produtor':44,
               'Abate':70,'Couro':71,'Agroindústria':78,'Receitas':88,'PAM':25}
##EXEMPLOS DE FILTROS:
####https://servicodados.ibge.gov.br/api/v3/agregados# ver pesquisas
####https://servicodados.ibge.gov.br/api/v3/agregados/1005/variaveis?classificacao&localidades=N1 #1005 uma tabela do censo 2006
####https://servicodados.ibge.gov.br/api/v3/agregados/1030/periodos/-10/variaveis?classificacao&localidades=N1#histórico de área dos censos
####https://servicodados.ibge.gov.br/api/v3/agregados/1033/periodos/-10/variaveis?classificacao&localidades=N1#histórico de tratores dos censos
####https://servicodados.ibge.gov.br/api/v3/agregados/1005/variaveis?classificacao&localidades=N1
####https://servicodados.ibge.gov.br/api/v3/agregados/1035/variaveis?classificacao=12778&localidades=N1 #historico efetivos animais
####https://servicodados.ibge.gov.br/api/v3/agregados/1031/variaveis?classificacao=12777&localidades=N1#historico por tipo de utilizacao
####https://servicodados.ibge.gov.br/api/v3/agregados/2059/metadados#mercosul censo demográfico
####https://servicodados.ibge.gov.br/api/v3/agregados/2059/variaveis?classificacao&localidades=N101
####https://servicodados.ibge.gov.br/api/v3/agregados/1032/periodos/-10/variaveis?classificacao&localidades=N1 #hitórico pessoal ocupado
####https://servicodados.ibge.gov.br/api/v3/agregados/5802/periodos/-10/variaveis/6535|1006535?classificacao=716[33617,33621,33626]&localidades=N2|N1

#obs a tabela 5802 vê comercialização de agrotóxicos por UF= pesquisa IDS de 2012 a 2014 tabelas 769 (fertilizantes) a 774 e 5802 776 agrosiilvopastoril de 1970 a 2006
#https://servicodados.ibge.gov.br/api/v3/agregados/5802/periodos/-10/variaveis/6535?classificacao=716&localidades=N2#tipos de agrotóxicos por região



def pesquisas_tema(tema=43):
  global Pesquisa1
 
  
  camin=r'https://servicodados.ibge.gov.br/api/v3/agregados?assunto=%s'%tema
  resposta6= requests.get(camin)
  dados6= resposta6.json()
  npesquisas=len(dados6)
  Pesquisa1={}
  for i1 in range(npesquisas):
    nom_pesquisa=dados6[i1]['nome']
    
    ntabelas=len(dados6[i1]['agregados'])
    Tabela1={}
    for i2 in range(ntabelas):
      id_tabela=dados6[i1]['agregados'][i2]['id']
      nome_tabela=dados6[i1]['agregados'][i2]['nome']
      camin2=r'https://servicodados.ibge.gov.br/api/v3/agregados/%s/metadados'%dados6[i1]['agregados'][i2]['id']
      resposta7= requests.get(camin2)
      resposta7_2=resposta7.json()
      
      pesquisa_nom=resposta7_2['pesquisa']
      pesquisa_assunto=resposta7_2['assunto']
      pesquisa_freq=resposta7_2['periodicidade']['frequencia']
      pesquisa_ini=resposta7_2['periodicidade']['inicio']
      pesquisa_fim=resposta7_2['periodicidade']['fim']
      cabeca_pesquisa='%s_%s_%s_%s_%s'%(pesquisa_nom,pesquisa_assunto,pesquisa_freq,pesquisa_ini,pesquisa_fim)
      
      nvariaveis=len(resposta7_2['variaveis'])
      
      idnom_variavel={}      
      for i2b in range(nvariaveis):
        V1=resposta7_2['variaveis'][i2b]['id']
        V2=resposta7_2['variaveis'][i2b]['nome']
        idnom_variavel['%s_%s'%(V1,V2)]=int(V1)
      nclasses=len(resposta7_2['classificacoes'])
      
      Classe1={}
      for i3 in range(nclasses):
        id_classe=resposta7_2['classificacoes'][i3]['id']
        nome_classe=resposta7_2['classificacoes'][i3]['nome']
        ncategoria=len(resposta7_2['classificacoes'][i3]['categorias'])
        idnom_categoria={}
        for i3b in range(ncategoria):
          A1=resposta7_2['classificacoes'][i3]['categorias'][i3b]['id']
          A2=resposta7_2['classificacoes'][i3]['categorias'][i3b]['nome']
          idnom_categoria['%s_%s'%(A1,A2)]=A1
        Classe1['%s_%s'%(id_classe,nome_classe)]=idnom_categoria
        
      Classe1['variavel']=idnom_variavel
      Tabela1['%s: %s_%s'%(cabeca_pesquisa,id_tabela,nome_tabela)]=Classe1
    Pesquisa1[nom_pesquisa]=Tabela1
    
def ler_pesquisa():
  pass
  #tipo_pesquisa=list(Pesquisa1.keys())#a lista de pesquisas do combo pesquisa  
  #chaves2=list(Pesquisa1[combo pesquisa].keys())#lista de tabelas do combo tabelas
  #chaves3=list(Pesquisa1[combo pesquisa][combo tabelas].keys())#lista combo classes
  #chaves4=list(Pesquisa1[combo pesquisa][combo tabelas][combo classes].keys())#lista combo categorias
  #chaves5=Pesquisa1[combo pesquisa][combo tabelas][combo classes][combo categorias]# identificador da categoria
 
def criar_variavel_inicial():
  global dados1
  global dados2
  global escolhida
  global classes_T
  global variaveis_T
 
  
  dados1=[]
  dados2=[]
  dados1a=[]
  dados2a=[]
  escolhida=[]
  classes_T=[]
  variaveis_T=[]
  if "controle1" not in st.session_state:
    st.session_state['controle1'] =[]
  if "Pesquisa1z" not in st.session_state:
    st.session_state['Pesquisa1z']=[]
  
criar_variavel_inicial()
def info_tabela_escolhida():
  global variaveis
  global classes
  global g1
  global cod_variaveis
  global dados1
  global dados2
  global escolhida
  global indica_pos
  
  if tabela_2 not in dados2:
    dados1.append([])
    dados2.append(tabela_2)
    dados1[-1]= resposta.json()
    dados1[-1].keys()
    variaveis=dados1[-1]['variaveis']
    var1={}
    for u in range(len(variaveis)):
      var1[variaveis[u]['id']]=variaveis[u]['nome']
    variaveis_T.append(var1)
    nvar=len(dados1[-1]['variaveis'])
    classes=dados1[-1]['classificacoes']
    classes_T.append(classes)
    nclass=len(classes)
    #ncategorias=len(classes[i]['categorias'])
    g1={}
                            
    for i in range(len(classes)):
        inter={}
        for j in range(len(classes[i]['categorias'])):
            inter[classes[i]['categorias'][j]['id']]=classes[i]['categorias'][j]['nome']
        g1['%s_%s'%(classes[i]['id'],classes[i]['nome'])]=inter

    cod_variaveis=list(g1.keys())#[829, 226, 218, 12517]['tipo_agricultor','produtos','condicao_legal','tipo_atividade']
    escolhida.append(g1)
    
  indica_pos=dados2.index(tabela_2)

#exit()  
  
#qual_tabela(6953)
#info_tabela_escolhida()

#outra tabela - só acessar escolhida e dados2. Pode acessar, também,  dados1 e dados2, classes_T e variaveis_T
#qual_tabela(6941)
#info_tabela_escolhida()

################# vendo variaveis classes e categorias ####################################
###variaveis_T[?]=dicionario{codigo:nome}
###len(variaveis_T[0]) = número de variáveis
  
###escolhida[?].keys() = classes ###['829_Tipologia', '12653_Grupos de cabeças de galinhas, galos, frangos, frangas e pintos', '12517_Grupos de atividade econômica']
###len(escolhida[?]) = número de classes

###escolhida[?][classes_acima]= {categorias}
### EX:escolhida[?]['829_Tipologia'] ###{46302:'Total', ....,46423:'Pronamp - não'}
### escolhida[0][list(escolhida[0].keys())[0]]###{46302:'Total', ....,46423:'Pronamp - não'}
###len(escolhida[?][list(escolhida[?].keys())[??]]) = número de categorias dentro da classes?

#### tem que ser a opção multiselect para selecionar mais de uma

####modelo='https://servicodados.ibge.gov.br/api/v3/agregados/6941/variaveis/2588|2589?classificacao=829[46302,46303]|12517[113601]&localidades=N3'#N6[N3[33]]=todos os municípios do RJ



#tabela1=6953
#var1 = variaveis[0]
#clas1=cod_variaveis[0]#829
#clas2=cod_variaveis[2]#218
#modelo=r'https://servicodados.ibge.gov.br/api/v3/agregados/\
#6953/variaveis/2312?classificacao=829[46303]|218[46503]&localidades=N3'

#if st.session_state["rdbtV12010000"]=='Não' or st.session_state["rdbtV12010000"]==None:

#import plotly.express as px
#grafico = px.density_mapbox(tabela, lon="geolocation_lng", lat="geolocation_lat", z="quantidade", mapbox_style="open-street-map",zoom=3, radius=10)
#grafico.update_layout(margin={"r": 0, "t": 0, "b": 0, "l": 0})
#grafico.show()
##def mapa1():
##  global gdf_muni
##  global junta
##  data_mun_RS= geobr.read_municipality(code_muni='RS',year=2020)
##  gdf_muni=data_mun_RS[data_mun_RS.name_muni=='Porto Alegre']
##  gdf_muni.plot()
##  gdf_muni.crs='EPSG:4326'
##  uc_gdf=geobr.read_conservation_units(date=201909,simplified=True,verbose=True)
##  uc_gdf.crs='EPSG:4326'
##  gpd.options.use_pygeos = True
##  junta=gpd.sjoin(uc_gdf,gdf_muni)
##  fig, ax = plt.subplots(figsize=(10,10))
##  base=gdf_muni.plot(ax=ax,color='white',edgecolor='black')
##  junta.plot(ax=base,column='group',legend=True,cmap='Pastel2')
##  ax.set_title('UCs - Porto Alegre - RS')
##  plt.show()
##  fig.savefig('teste2.png')
##def mapa1_interativo():
##  #-----folium.Map(location=center, zoom_start=1, tiles=None)
##  m=gdf_muni.explore(
##    color='grey',
##    tooltip='name_muni',
##    tooltip_kwds=dict(labels=False),
##    name='Porto Alegre'
##    )
##
##  junta.explore(
##    m=m,
##    column='group',#grupo da UC
##    scheme='naturalbreaks',
##    cmap='Spectral',    
##    style_kwds=dict(color='black'),
##    legend=True,
##    k=200,
##    legend_kwds=dict(colorbar=False),
##    name='UCs'
##    )
##  #----folium.TileLayer('Stamen Toner',control=True).add_to(m)
##  folium.LayerControl().add_to(m)
##  m.save(outfile='teste.html')
##
##def mapa2():
##  br_uf = geobr.read_state()
##  br_uf_d = br_uf.merge(d)
##  f, ax = plt.subplots()
##  f.set_size_inches(16, 16)
##  br_uf_d.plot(
##    ax=ax, # Axis de destino do gráfico
##    column="Área plantada (Hectares)", # Coluna com os valores usados para colorir o mapa
##    cmap="Greens", # Mapa de cores
##    edgecolor="black", # Cor dos contornos
##    linewidth=0.25, # Espessura dos contornos
##  )
##  cax = f.add_axes(
##    [
##        0.82,    # posicao x (entre 0.0 e 1.0)
##        0.18,    # posicao y (entre 0.0 e 1.0)
##        0.03,    # largura x
##        0.40,    # altura y
##    ]
##  )
##  sm = plt.cm.ScalarMappable(
##    cmap="Greens",                                       # Usa o mesmo cmap do mapa
##    norm=plt.Normalize(
##        vmin=br_uf_d["Área plantada (Hectares)"].min(),  # Valor mínimo
##        vmax=br_uf_d["Área plantada (Hectares)"].max(),  # Valor máximo
##    ),
##  )
##  f.colorbar(
##    sm,
##    cax=cax,
##    # Formata a escala do Colorbar
##    format=ticker.FuncFormatter(lambda x, pos: f"{x/1000: >10,.0f} mil ha"),
##  )
##  ax.set_title(
##    "Área plantada de Milho por Estado em 2018",
##    fontdict={"fontsize": 20},
##  )
##  f.text(
##    0.15,                  # Posição x
##    0.20,                  # Posição y
##    "Fonte: IBGE (2020)."  # Texto
##  )
##  #ax.axis("off")
##  f.savefig("TESTE.png")

def gif():
  import streamlit as st
  import base64

  """### gif from url"""
  st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

  """### gif from local file"""
  file_ = open("/home/rzwitch/Desktop/giphy.gif", "rb")
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")
  file_.close()

  st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
  )
def imagem_fundo(imagem, tipo='jpg'):####função não funciona
  with open(imagem, 'rb') as f:
    data = f.read()
    bin_str =base64.b64encode(data).decode()
  page_bg_img =f'<style>.stApp{{background-image: url("data:image/%s;base64,%s");background-size: cover}}</style>'.format(tipo,bin_str)
  st.markdown(page_bg_img, unsafe_allow_html=True)
  return
def render_svg2(svg_file,tamanho=80):

    with open(svg_file, "r") as f:
        lines = f.readlines()
        svg = "".join(lines)

        #"""Renders the given svg string."""
        b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        #html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
        html_string = f'<a href="{svg_file}" target="_blank"><img src="data:image/svg+xml;base64,%s" width="%s" caption="legend"></a>'%(b64,tamanho)

        st.markdown(html_string, unsafe_allow_html=True)
        #return html

def imagem_tamanho():#usado uma vez só para transformar a imagem selecionada
  from PIL import Image
  import os
  img = Image.open('imagem_agro.jpeg')
  base_width = 300
  wpercent = (base_width / float(img.size[0]))
  hsize = int((float(img.size[1]) * float(wpercent)))
  img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
  #img.save('imagem_agro2.jpeg')  
  rgba = img.convert("RGBA")
  datas = rgba.getdata()
  newData = []
  for item in datas: 
    if item[0] > 250 and item[1] > 250 and item[2] > 250:  
        # storing a transparent value when we find a white colour 
        newData.append((255, 255, 255, 0)) 
    else: 
        newData.append(item)  # other colours remain unchanged        
  rgba.putdata(newData)
  rgba.save("transparent_image.png", "PNG")
  img2 = Image.open('transparent_image.png')
  img2.save('imagem_agro2.jpeg')
  os.remove('transparent_image.png')#removendo o que foi criado
  
def cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE'):
      cb1 = cab1
      cb2 = cab2
      dadoscab=[cb1,cb2]     
      with st.container(height=70,border=False):
        row1=st.columns([1,1,2,4,2],gap='medium')
        with row1[4]:          
          #st.image('fazenda_colorida.jpg',output_format='JPEG', width=70)#use_container_width=True
          render_svg2('./imagem_fazenda/fazenda3.svg',tamanho=120)
        with row1[2]:
          #st.image('imagem_agro2.jpeg',output_format='JPEG')#use_container_width=True
          render_svg2('arvore.svg',tamanho=80)
        with row1[3]:
          st.markdown(
                   '<span id= "cabec1" style="font-size: 18px;color:##008523;width:1076px;text-align: justify">**{0:^}**</span>'.format(cb1), unsafe_allow_html=True)
        with row1[1]:
            st.markdown(
                    '<span id= "cabec2" style="font-size: 18px;color:##008523;width:1076px;text-align: justify">**{0:}**</span>'.format(cb2), unsafe_allow_html=True)

        st.html('<hr size="3" color=#cc99aa  style="border:1px solid #ccaa99; margin:1px auto;">')

##      with st.container(height=37,border=False):
##        row2=st.columns([0.01,0.5, 0.49],gap='medium')
##        with row2[1]:
##            st.markdown(
##                    '<span id= "cabec2" style="font-size: 18px;color:##008523;width:1076px;justify-content:left">**{0:}**</span>'.format(cb2), unsafe_allow_html=True)
      #st.markdown(':blue[--------------------------------------------------------------------------------------------------------------------------------------------------------------]',)
def ufs():
  global coduf
  import requests
  camdados2=r'https://servicodados.ibge.gov.br/api/v3/agregados/6953/variaveis/2312?classificacao=829[46302]|228[113862]|218[46502]|12517[113601]&localidades=N3'
  resposta3= requests.get(camdados2)
  dados9=[]
  dados9.append([])
  dados9[-1]=resposta3.json()
  dados9[-1][0].keys()
  dados9[-1][0]['resultados'][0].keys()
  coduf={}
  for u in range(tam):
    coduf[int(dados9[-1][-1]['resultados'][-1]['series'][u]['localidade']['id'])]=dados9[-1][-1]['resultados'][-1]['series'][u]['localidade']['nome']
#roda ufs para gerar o dicionário de ufs e código
coduf={11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá',
       17: 'Tocantins', 21: 'Maranhão', 22: 'Piauí', 23: 'Ceará', 24: 'Rio Grande do Norte',
       25: 'Paraíba', 26: 'Pernambuco', 27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais',
       32: 'Espírito Santo', 33: 'Rio de Janeiro', 35: 'São Paulo', 41: 'Paraná', 42: 'Santa Catarina',
       43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso', 52: 'Goiás',
       53: 'Distrito Federal'}

def mun_por_uf():
  global uf_mun
  ufs=list(coduf.keys())
  camdados3=r'https://servicodados.ibge.gov.br/api/v3/agregados/6953/variaveis/2312?classificacao=829[46302]|228[113862]|218[46502]|12517[113601]&localidades=N6[N3[%s]]'
  uf_mun={}
  for t2 in ufs:
    caminho=camdados3%(t2)
    resposta4= requests.get(caminho)
    dados10=[]
    dados10.append([])
    dados10[-1]=resposta4.json()
    tam1=len(dados10[-1][0]['resultados'][-1]['series'])    
    muni1={} 
    for t3 in range(tam1):          
      muni1[dados10[-1][0]['resultados'][-1]['series'][t3]['localidade']['id']]=dados10[-1][0]['resultados'][-1]['series'][t3]['localidade']['nome']
    uf_mun[t2]=muni1
def censo():
  global nivel3
  global teto2
  global cb2
  global varvar2
  global varvar1
  global nivel1
  global nivel5
  
  cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
  with st.container(height=80,border=False):
    censolin1=st.columns([1,3,3,1],gap='medium')
    with censolin1[1]:
      cb1=st.selectbox(label='{0:}- {1:}'.format('Grupo de Tabelas','Censo'), options= grupo_tabelas,index=0, key='cbbox{0:}'.format('escolha1'),placeholder="Escolha uma opção de tabela", disabled=False, label_visibility="visible")
    with censolin1[2]:
      cb2= st.selectbox(label='{0:}- {1:}'.format('Tabelas','Censo'), options= list(tabelas_todo[cb1].keys()),index=0, key='cbbox{0:}'.format('escolha2'),placeholder="Escolha uma opção da tabela anterior", disabled=False, label_visibility="visible")
  st.markdown('<p style="font-size: 14px;color: blue;">"{0:}"</p>'.format(tabelas[cb2]),unsafe_allow_html=True)
  #cb2
  #if 'key' not in st.session_state:
    #st.session_state['key'] = 'value'
  cdf=0
  while cdf==0:
    try:
      qual_tabela(cb2)
      #criar_variavel_inicial()
      info_tabela_escolhida()
      cdf=1
    except:
      cdf=0
      pass
  if cdf==1:
    #dados2
    #list(escolhida[indica_pos].keys())
    #for u in range(len(list(escolhida[indica_pos].keys()))):
      #st.markdown('<p style="font-size: 14px;color: blue;">"{0:}"</p>'.format(list(escolhida[indica_pos].keys())[u]),unsafe_allow_html=True)
      ###st.write(list(escolhida[indica_pos].keys())[u])
      #txt1=''
      #for u2 in range(len(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[u]].values()))):
        #t1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[u]].values())[u2]
        #t2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[u]].keys())[u2]
        #txt1+='%s_%s ||  '%(t2,t1)
      #st.write(txt1)
    #st.write(len(g1))
    nivel1=list(escolhida[indica_pos].keys())#lista para o multiselect de classes
    nivel1b={}
    for j in nivel1:
      nivel1b[j.strip()]=j.strip().split('_')[1]#dicionário de classes
    #o [0] só vê as categorias da primeira classe
    nivel2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[0]].values())#lista para o multiselect de categorias
    nivel2b=escolhida[indica_pos][list(escolhida[indica_pos].keys())[0]]#dicionário de categorias

    varvar1={}
    for i in variaveis:
      varvar1[i['nome']]=i['id']
    with st.container(height=80,border=False):
      linvar1=st.columns([1,2,1],gap='medium')
      with linvar1[1]:
        varvar2=st.multiselect('Variaveis',list(varvar1.keys()),key='%s'%'variavel')
    #st.markdown("""<style> div[data-baseweb=select] span{max-width: 400px;font-size: 0.6rem;}</style>""", unsafe_allow_html=True)
    #varvar2#vê as variáveis selecionadas
    varvar3=[]#coloca as variáveis selecionadas dentro de uma tupla de códigos
    if len(varvar2)>0:
      for y in varvar2:
        varvar3.append(varvar1[y])
    #st.write(tuple(varvar3))
    #varvar3
    #try:
    #  varvar1[varvar2[0]]
    #except:
    #  pass
    colcol=[len(nivel1b)//4,len(nivel1b)%4]
    par2=colcol[1]
    if par2!=0:
      ctq=1
    else:
      ctq=0
    par1=colcol[0]+ctq
    teto2=[]
    nivel3=[]
    nivel4={}#{'829_Tipologia': {46302: 'Total', ... '811_Controle de doenças e/ou parasitas, suplementação alimentar e beneficiamento': {47082: 'Total',...
    nivel5={}#{'829_Tipologia': {'Total': 46302 ....'811_Controle de doenças e/ou parasitas, suplementação alimentar e beneficiamento': {'Total': 47082..
    for uj in range(par1):
      teto1=[]
      
      if par2!=0:        
        if uj<par1-1:#se não for o último registro
          intcol=[0.05,0.05]
          for kj in range(4*uj,4*(uj+1)):
            intcol.insert(1,1)
            #guardando as categorias por classes=nivel3
            nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))

            vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]           
            nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
            interm5={}
            lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
            lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
            for u in range(len(lista1)):
              interm5[lista2[u]]=lista1[u]
            nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
          teto1=st.columns(intcol,gap='medium')
          for kj in range(4*uj,4*(uj+1)):            
            if kj<4:
               par3=kj
            elif kj>=4:              
              par3=kj%4#resto da divisão
                
            with teto1[par3+1]:#quardar nessa coluna
              vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
            teto2.append(vv3)
        elif uj==par1-1:
          intcol=[0.05,0.05]
          for kj in range(uj*4,uj*4+par2):
            intcol.insert(1,1)
            nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))
            vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]           
            nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
            interm5={}
            lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
            lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
            for u in range(len(lista1)):
              interm5[lista2[u]]=lista1[u]
            nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
          teto1=st.columns(intcol,gap='medium')
          for kj in range(uj*4,uj*4+par2):
            if kj<4:
               par3=kj
            elif kj>=4:              
              par3=kj%4#resto da divisão
            
            with teto1[par3+1]:
              vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
            teto2.append(vv3)
      else:
        intcol=[0.05,0.05]
        for kj in range(4*uj,4*(uj+1)):
          intcol.insert(1,1)
          nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))
          vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]         
          nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
          interm5={}
          lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
          lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
          for u in range(len(lista1)):
               interm5[lista2[u]]=lista1[u]
          nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
        teto1=st.columns(intcol,gap='medium')
        for kj in range(4*uj,4*(uj+1)):
          if kj<4:
            par3=kj
          elif kj>=4:              
            par3=kj%4#resto da divisão
          with teto1[par3+1]:
            vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
          teto2.append(vv3)
  
  #teto2
  #st.write(len(teto2))
  #teto2[0]
  #st.write(len(teto2[0]))
  
  dados_api2()
  #st.write(vert1)
    
  #st.write(list(nivel5.keys()))
  #st.write(list(nivel5[list(nivel5.keys())[0]]))
  esq, meio, direita = st.columns(3)
  with meio:
    if st.button("acessar api"):
                 st.write("ACESSANDO DADOS")
                 #acesso_dados1()
            
#o nivel3 traz todas as categorias por classe
def dados_api2():
  global vert1
  global fimmod
  #global txtvar
  #'N6' in dados1[-1]['nivelTerritorial']['Administrativo']#se True tem informação de município
  if len(varvar2)==0:#Se não for selecionada nenhuma variável
    p1=[varvar1[list(varvar1.keys())[0]]]#pegar a primeira variável
  else:
    inte2=[]
    for r2 in varvar2:
      inte2.append(varvar1[r2])
    p1=inte2
  #p1
  vert1=[]
  vert2=[]#só guarda os primeiros ids das categorias de cada classe
  for r in range(len(nivel1)):#número de classes
    inte=[]
    if len(teto2[r])==0:#se nada foi selecionado dentro de cada multselect(r)
      para1=list(nivel5[nivel1[r]].keys())[0]#pegando a primeira categoria da classe nivel1[r] = geralmente é o Total
      vert1.append([nivel5[nivel1[r]][para1]])#guardando o id da categoria
      vert2.append([nivel5[nivel1[r]][para1]])#guardando o id da categoria
    else:
      for r2 in teto2[r]:
        inte.append(nivel5[nivel1[r]][r2])
      vert1.append(inte)#guardando o(s) id(s) das categoria(s) selecionada(s)
      para1=list(nivel5[nivel1[r]].keys())[0]
      vert2.append([nivel5[nivel1[r]][para1]])#guardando o primeiro id de categoria dentro da classe
  #vert1
  #st.write(len(vert1))
  #vert1[0]
  modelo1='https://servicodados.ibge.gov.br/api/v3/agregados/%s/'%cb2
  nvar=len(p1)
  nnvar1=''
  for j in range(nvar):
    if j==0:
      nnvar1+='%s'
    else:
      nnvar1+='|%s'   
      
  nclas=len(nivel1)
  nnclas1=''
  for j in range(nclas):
    nncat1=''
    cat1=len(vert1[j])
    for j2 in range(cat1):
      if j2==0:
        if cat1!=1:
          nncat1+='%s[%s'
        else:
          if j!=nclas-1:
            nncat1+='%s[%s]|'
          else:
            nncat1+='%s[%s]'          
      elif j2<cat1-1:
        nncat1+=',%s'
      else:
        if j!=nclas-1:
          nncat1+=',%s]|'
        else:
          nncat1+=',%s]'
    nnclas1+=nncat1  
   
  w1=list(nivel5.keys())
  
  #nivel5[w1[0]][w2[0]]#VENDO O CÓDIGO NUMÉRICO DA PRIMEIRA CATEGORIA DA PRIMEIRA CLASSE
  #nivel5[w1[3]][w2[1]]#VENDO O CÓDIGO NUMÉRICO DA SEGUNDA CATEGORIA DA TERCEIRA CLASSE
  
  intervari1=[]
  for y1 in range(len(teto2)):    
    w2=list(nivel5[w1[y1]].keys())
    #intervari1=[]
    intervari1.append(int(w1[y1].split('_')[0]))#colocando o número da classe
    if len(teto2[y1])!=0:#se tiver categoria selecionada            
      for y1a in teto2[y1]:
        parr2=w2.index(y1a)
        intervari1.append(nivel5[w1[y1]][w2[parr2]])
    else:
      intervari1.append(nivel5[w1[y1]][w2[0]])
  #txtvar='%s'%intervari1      
  mod='variaveis/'+'%s?classificacao='%nnvar1+nnclas1+'&localidades=N3'
  #st.write(mod)
  modelo2='variaveis/2588|2589?classificacao=829[46302,46303]|12517[113601]&localidades=N3'#N6[N3[33]]=todos os municípios do RJ
  fimmod=modelo1+mod
  tudi1=tuple(p1+intervari1)
  fimmod2=fimmod%tudi1
  st.write(fimmod2)
  st.markdown('<p style="font-size: 14px;color: green;">"{0:}"</p>'.format('Exemplo:N6[N3[31,35]] = vê os municípios de MG e SP'),unsafe_allow_html=True)
  st.markdown('<p style="font-size: 14px;color: green;">"{0:}"</p>'.format('Exemplo: N3|BR = vê os Estados e Brasil'),unsafe_allow_html=True)

def tudo():
  #global nivel3
  global cb11
  global cb21
  global cb31
  global chaves2b
  global chaves2c
  global controle1
  global Pesquisa1z
  
  #global cnta
  #global nivel1
  #global nivel5
  #st.session_state['cnta']=0

  cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
  #  
  #
  #chaves3=list(Pesquisa1[combo pesquisa][combo tabelas].keys())#lista combo classes
  #chaves4=list(Pesquisa1[combo pesquisa][combo tabelas][combo classes].keys())#lista combo categorias
  #chaves5=Pesquisa1[combo pesquisa][combo tabelas][combo classes][combo categorias]# identificador da categoria
  temass=list(assuntos_agro.keys())
  inicol = st.columns([1,4,1],gap='medium')
  with inicol[1]:
     cb11=st.selectbox(label='{0:}- {1:}'.format('Temas','Agro'), options= temass,index=0, key='cbbox{0:}'.format('tema1'),placeholder="Escolha uma opção de tema", disabled=False, label_visibility="visible")

  if cb11 not in st.session_state['controle1']:#evita acessar a internet se já viu a tema anteriormente    
    cdf1=0
    while cdf1==0:
      try:
        pesquisas_tema(tema=assuntos_agro[cb11])#RODANDO O PROGRAMA DE SELEÇÃO DE TABELAS NA INTERNET
        cdf1=1
      except:
        cdf1=0
    st.session_state['controle1'].append(cb11)
    st.session_state['Pesquisa1z'].append(Pesquisa1)
    #controle1.append(cb11)
    #Pesquisa1z.append(Pesquisa1)
    nump=-1
  else:
    nump= st.session_state['controle1'].index(cb11)
    
  chaves2=[]
  chaves2b=[]
  chaves2c=[]
  chaves2d=[]
  tipo_pesquisa=list(st.session_state['Pesquisa1z'][nump].keys())#a lista de pesquisas do combo pesquisa
  for ju in range(len(tipo_pesquisa)):
    chaves2.append(list(st.session_state['Pesquisa1z'][nump][tipo_pesquisa[ju]].keys()))#lista de tabelas do combo tabelas por pesquisa
  
  for yu in chaves2:
    intt={}
    intt2={}
    for k in yu:
      intt['%s- %s'%(k.split(':')[0],k.split(':')[1].split('_')[0].strip())]=k.split(':')[1].split('_')[1].strip()
      intt2['%s- %s'%(k.split(':')[0],k.split(':')[1].split('_')[0].strip())]=k
    chaves2b.append(intt)
    chaves2d.append(intt2)#só para ligar a chaves2b no futuro
  for yu in chaves2b:  
    chaves2c.append(list(yu.keys()))
  with st.container(height=80,border=False):
    tudolin1=st.columns([1,6,6,1],gap='medium')
    with tudolin1[1]:
      cb21=st.selectbox(label='{0:}- {1:}'.format('Pesquisas','Agro'), options= tipo_pesquisa,index=0, key='cbbox{0:}'.format('pesquisa1'),placeholder="Escolha uma opção de tabela", disabled=False, label_visibility="visible")
    with tudolin1[2]:     
      cb31= st.selectbox(label='{0:}- {1:}'.format('Tabelas','Agro'), options= chaves2c[tipo_pesquisa.index(cb21)],index=0, key='cbbox{0:}'.format('tabelas1'),placeholder="Escolha uma opção da tabela anterior", disabled=False, label_visibility="visible")
  
  st.markdown('<p style="font-size: 15px;color: blue;">"{0:}"</p>'.format(cb31),unsafe_allow_html=True)
  st.markdown('<p style="font-size: 14px;color: blue;">"{0:}"</p>'.format(chaves2b[tipo_pesquisa.index(cb21)][cb31]),unsafe_allow_html=True)
  #st.write(controle1)  
  #st.session_state
  
  tabelaz=st.session_state['Pesquisa1z'][nump][list(st.session_state['Pesquisa1z'][nump].keys())[tipo_pesquisa.index(cb21)]][chaves2d[tipo_pesquisa.index(cb21)][cb31]]
  nivel1=list(tabelaz.keys())[:-1]#lista para o multiselect de classes não trazendo o campo 'variavel'
  nivel2=list(tabelaz.values())[:-1]#lista para o multiselect de categorias não trazendo o campo de categorias da 'variavel'
  varvar1=list(tabelaz.values())[-1]
  #with st.container(height=80,border=False):
  linvar1=st.columns([0.2,20,20,0.2],gap='medium')  
  
  with linvar1[1]:
    varvar2=st.multiselect('Variaveis',list(varvar1.keys()),key='%s'%'variavel',placeholder="      Selecione uma Tabela            ")
    
    st.markdown("""
    <style>        
        .stTextInput > label {
            font-size:50%; 
            font-weight:bold;                        
        }
        .stMultiSelect > label {
            font-size:120%; 
            font-weight:bold; 
            color:green;
        }
        span[data-baseweb="tag"] {
          background-color: blue !important;          
        }
        span[data-baseweb="select"] {
          width: 1000px;
        }
        
         
    </style>
    """, unsafe_allow_html=True)
  with linvar1[2]:
    textvar=''
    T1={}
    
    for i in range(len(varvar2)):
      textvar+='%s: %s || '%(i+1,varvar2[i])
      T1[i]=varvar2[i]
    T2={'id': list(T1.keys()), 'Nome': list(T1.values())}
    dfT = pd.DataFrame(data=T2)
    #st.markdown("<p style='text-align: justify; color: black;'>Selecionados= %s</p>"%textvar, unsafe_allow_html=True)
    #st.table(dfT)
    def style_dataframe(df):
      return df.style.set_table_styles(
          [{
              'selector': 'th',
              'props': [
                  ('background-color', '#C0C0C0'),
                  ('color', 'white'),
                  ('font-family', 'Arial, sans-serif'),
                  ('font-size', '16px')
              ]
          }, 
          {
              'selector': 'td, th',
              'props': [
                  ('border', '2px solid #DCDCDC')
              ]
          },
          {
              'selector': 'tr',
              'props': [
                  ('background-color', '#B0C4DE')                 
                        
              ]
          }
           ]
      )
    def style_dataframe2(df):
      for i in range(df.shape[0]):
        if i==0 or df.iloc[i,0]%2==0:
          return df.style.set_table_styles(
              [{
                  'selector': 'tr',
                  'props': [
                      ('background-color', '#B0C4DE')                 
                        
                  ]
              }]
            )
        else:
          return df.style.set_table_styles(
              [{
                'selector': 'tr',
                'props': [
                    ('background-color', '#DCDCDC')                 
                    
                  ]
              }]
            )
       
   
    styled_df2 = style_dataframe(dfT)
    
    #styled_df2=style_dataframe2(pd.DataFrame(styled_df2))
    #styled_df2=style_dataframe2(dfT[dfT['id']%2!=0])
    #styled_df2=style_dataframe3(dfT[dfT['id']%2==0])
    try:
      st.write(styled_df2.to_html(), unsafe_allow_html=True)
    except:
      pass



    
    #st.write("Selecionados:", textvar)
    #CSS = """.st-key-variavel.stMultiSelect{width: 1000px;}"""
    #st.html(f"<style>{CSS}</style>")
    #span[data-baseweb="tag"]>span:first-child {background-color:#272272 !important;}
##  '''nivel1=list(escolhida[indica_pos].keys())#lista para o multiselect de classes
##  nivel1b={}
##  for j in nivel1:
##    nivel1b[j.strip()]=j.strip().split('_')[1]#dicionário de classes
##  #o [0] só vê as categorias da primeira classe
##  nivel2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[0]].values())#lista para o multiselect de categorias
##  nivel2b=escolhida[indica_pos][list(escolhida[indica_pos].keys())[0]]#dicionário de categorias
##
##  varvar1={}
##  for i in variaveis:
##    varvar1[i['nome']]=i['id']
##  with st.container(height=80,border=False):
##    linvar1=st.columns([1,2,1],gap='medium')
##    with linvar1[1]:
##      varvar2=st.multiselect('Variaveis',list(varvar1.keys()),key='%s'%'variavel')
##  #st.markdown("""<style> div[data-baseweb=select] span{max-width: 400px;font-size: 0.6rem;}</style>""", unsafe_allow_html=True)
##  #varvar2#vê as variáveis selecionadas
##  varvar3=[]#coloca as variáveis selecionadas dentro de uma tupla de códigos
##  if len(varvar2)>0:
##    for y in varvar2:
##      varvar3.append(varvar1[y])
##  #st.write(tuple(varvar3))
##  #varvar3
##  #try:
##  #  varvar1[varvar2[0]]
##  #except:
##  #  pass
##  colcol=[len(nivel1b)//4,len(nivel1b)%4]
##  par2=colcol[1]
##  if par2!=0:
##    ctq=1
##  else:
##    ctq=0
##  par1=colcol[0]+ctq
##  teto2=[]
##  nivel3=[]
##  nivel4={}#{'829_Tipologia': {46302: 'Total', ... '811_Controle de doenças e/ou parasitas, suplementação alimentar e beneficiamento': {47082: 'Total',...
##  nivel5={}#{'829_Tipologia': {'Total': 46302 ....'811_Controle de doenças e/ou parasitas, suplementação alimentar e beneficiamento': {'Total': 47082..
##  for uj in range(par1):
##    teto1=[]
##    
##    if par2!=0:        
##      if uj<par1-1:#se não for o último registro
##        intcol=[0.05,0.05]
##        for kj in range(4*uj,4*(uj+1)):
##          intcol.insert(1,1)
##          #guardando as categorias por classes=nivel3
##          nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))
##
##          vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]           
##          nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
##          interm5={}
##          lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
##          lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
##          for u in range(len(lista1)):
##            interm5[lista2[u]]=lista1[u]
##          nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
##        teto1=st.columns(intcol,gap='medium')
##        for kj in range(4*uj,4*(uj+1)):            
##          if kj<4:
##             par3=kj
##          elif kj>=4:              
##            par3=kj%4#resto da divisão
##              
##          with teto1[par3+1]:#quardar nessa coluna
##            vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
##          teto2.append(vv3)
##      elif uj==par1-1:
##        intcol=[0.05,0.05]
##        for kj in range(uj*4,uj*4+par2):
##          intcol.insert(1,1)
##          nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))
##          vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]           
##          nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
##          interm5={}
##          lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
##          lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
##          for u in range(len(lista1)):
##            interm5[lista2[u]]=lista1[u]
##          nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
##        teto1=st.columns(intcol,gap='medium')
##        for kj in range(uj*4,uj*4+par2):
##          if kj<4:
##             par3=kj
##          elif kj>=4:              
##            par3=kj%4#resto da divisão
##          
##          with teto1[par3+1]:
##            vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
##          teto2.append(vv3)
##    else:
##      intcol=[0.05,0.05]
##      for kj in range(4*uj,4*(uj+1)):
##        intcol.insert(1,1)
##        nivel3.append(list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values()))
##        vel4=escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]]         
##        nivel4[list(escolhida[indica_pos].keys())[kj]]=vel4
##        interm5={}
##        lista1=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]])
##        lista2=list(escolhida[indica_pos][list(escolhida[indica_pos].keys())[kj]].values())
##        for u in range(len(lista1)):
##             interm5[lista2[u]]=lista1[u]
##        nivel5[list(escolhida[indica_pos].keys())[kj]]=interm5
##      teto1=st.columns(intcol,gap='medium')
##      for kj in range(4*uj,4*(uj+1)):
##        if kj<4:
##          par3=kj
##        elif kj>=4:              
##          par3=kj%4#resto da divisão
##        with teto1[par3+1]:
##          vv3=st.multiselect(nivel1[kj],nivel3[kj],key='%s'%nivel1[kj])
##        teto2.append(vv3)
##  
##  #teto2
##  #st.write(len(teto2))
##  #teto2[0]
##  #st.write(len(teto2[0]))
##  
##  dados_api2()
##  #st.write(vert1)
##    
##  #st.write(list(nivel5.keys()))
##  #st.write(list(nivel5[list(nivel5.keys())[0]]))
##  esq, meio, direita = st.columns(3)
##  with meio:
##    if st.button("acessar api"):
##                 st.write("ACESSANDO DADOS")
##                 #acesso_dados1()
##  '''
def acesso_dados1():
  global resposta1
  global dados1a
  camdados1=r'%s'%fimmod2
  resposta1= requests.get(camdados1)
  resposta1.headers
  dados1a.append([]) 
  dados1a[-1]= resposta1.json()
  dados1a[-1].keys()
  variaveis1a=dados1a[-1]['variaveis']
  variaveis1a
ctkey=0
def ViewPDF(wch_fl,compr=1200,larg=950):
  #global ctkey
  #with open(wch_fl,"rb") as pdf_file:
    #base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
    #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="%s" height="%s" type="application/pdf">'%(compr,larg)
    #pdf_display = f'<src="data:application/pdf;base64,{base64_pdf}" width="%s" height="%s" type="application/pdf">'%(compr,larg)
    
    #st.markdown(pdf_display, unsafe_allow_html=True)
    #pdf_display = f'<iframe src="{wch_fl}" width="%s" height="%s" type="application/pdf"></iframe>'%(compr,larg)

  #pdf_display = f'<embed src="{wch_fl}" width="%s" height="%s" >'%(compr,larg)
  #st.markdown(pdf_display, unsafe_allow_html=True)
  st.pdf(wch_fl,height=compr)
  
  
##  if 'pdf_ref' not in ss:
##    ss.pdf_ref = None
##
##  ctkey+=1
##  # Access the uploaded ref via a key.
##  st.file_uploader(wch_fl, type=('pdf'),key='pdf_%s'%ctkey)
##
##  if eval('ss.pdf_%s'%ctkey):
##      ss.pdf_ref = eval('ss.pdf_%s'%ctkey)  # backup
##      
##
##  # Now you can access "pdf_ref" anywhere in your app.
##  if ss.pdf_ref:
##      binary_data = ss.pdf_ref.getvalue()
##      pdf_viewer(input=binary_data, width=compr, height=larg)
   
    
dicagrolink={'AC':9822,'AL':9823,'BA':9826,'CE':9827,'DF':9828,
             'ES':9829,'GO':9830,'MA':9831,'MG':9832,'MS':9833,'MT':9834, 'PA':9835,
             'PB':9836,'PE':9837,'PI':9838,'PR':9839,'RJ':9840,'RN':9841,'RO':9842,
             'RR':9843,'RS':9844,'SC':9845,'SE':9846,'SP':9847,'TO':9848}

listagro=list(dicagrolink.keys())
def Info():      
      tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08, tab09,tab10,tab11 = st.tabs([s.center(9," ") for s in ["Cotações", "Notícias","Clima","Sites","Folder_herbicida", 'Folder_inseticida', 'Folder_fungicida','Nutrição vegetal','Fisiologia','Hortifruti','CENSO2017']])
      
      with tab01:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
        with st.container(height=250,border=False):
          LINHA1=st.columns([0.05,0.30,0.30,0.30,0.05],gap='medium')
          with LINHA1[1]:           
            codig2='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=54&id_indicador%5B%5D=91&id_indicador%5B%5D=23&id_indicador%5B%5D=24&id_indicador%5B%5D=162"></script>'
            #st.html(codig2, height=250, scrolling=True)
            #st.html(codig2, width=250, unsafe_allow_javascript=True)
            st.iframe(codig2, height=250)
            
          with LINHA1[2]:
            codig3='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=77&id_indicador%5B%5D=72&id_indicador%5B%5D=178&id_indicador%5B%5D=12&id_indicador%5B%5D=381-380&id_indicador%5B%5D=380-413&id_indicador%5B%5D=378-61"></script>'
            #st.html(codig3, height=250, scrolling=True)
            #st.html(codig3, width=250, unsafe_allow_javascript=True)
            st.iframe(codig3, height=250)
          with LINHA1[3]:
            codig4='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=159-Bastos+(SP)+-+FOB-branco&id_indicador%5B%5D=159-Grande+BH+-+(MG)+-+CIF-branco&id_indicador%5B%5D=159-Bastos+(SP)+-+FOB-vermelho&id_indicador%5B%5D=159-Grande+BH+-+(MG)+-+CIF-vermelho&id_indicador%5B%5D=159-Recife+(PE)+-+CIF-branco&id_indicador%5B%5D=159-Recife+(PE)+-+CIF-vermelho"></script>'
            #st.html(codig4, height=250, scrolling=True)
            #st.html(codig4, width=250, unsafe_allow_javascript=True)
            st.iframe(codig4, height=250)
          
        with st.container(height=250,border=False):
          LINHA2A1=st.columns([0.05,0.30,0.30,0.30,0.05],gap='medium')
          with LINHA2A1[1]:
            codig6='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=305-RS&id_indicador%5B%5D=305-PR&id_indicador%5B%5D=305-MT&id_indicador%5B%5D=305-MS&id_indicador%5B%5D=305-CE&id_indicador%5B%5D=305-BA"></script>'

            #st.html(codig6, height=250, scrolling=True)
            #st.html(codig6, width=250, unsafe_allow_javascript=True)
            st.iframe(codig6, height=250)
          with LINHA2A1[2]:
            codig6b='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=129-10&id_indicador%5B%5D=129-6&id_indicador%5B%5D=129-4&id_indicador%5B%5D=129-5&id_indicador%5B%5D=129-1"></script>'
            #st.html(codig6b, height=250, scrolling=True)
            #st.html(codig6b, width=250, unsafe_allow_javascript=True)
            st.iframe(codig6b, height=250)
          with LINHA2A1[3]:
            codig5='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=8&id_indicador%5B%5D=2&id_indicador%5B%5D=181&id_indicador%5B%5D=130&id_indicador%5B%5D=leitep&id_indicador%5B%5D=349-MG&id_indicador%5B%5D=349-NP"></script>'
            #st.html(codig5, height=250, scrolling=True)
            #st.html(codig5, width=250, unsafe_allow_javascript=True)
            st.iframe(codig5, height=250)
            st.markdown('<p style="font-size: 14px;color: blue;">Preço FOB = não inclui frete (comprador assume riscos e custos com o transporte = pago no destino). CIF = inclui frete (vendedor paga custo do transporte na origem = vendedor é responsável pela entrega)</p>',unsafe_allow_html=True)
            
        with st.container(height=250,border=False):
          LINHA3A1=st.columns([0.05,0.30,0.30,0.30,0.05],gap='medium')
          with LINHA3A1[1]:
            codig1a='<!-- Widgets Produtos Cepea - www.cepea.esalq.com.br/br/widget.aspx --><script type="text/javascript" src="https://www.cepea.org.br/br/widgetproduto.js.php?fonte=arial&tamanho=7&largura=300px&corfundo=dbd6b2&cortexto=333333&corlinha=ede7bf&id_indicador%5B%5D=50&id_indicador%5B%5D=53&id_indicador%5B%5D=208&id_indicador%5B%5D=104&id_indicador%5B%5D=209&id_indicador%5B%5D=103"></script>'
            #st.html(codig1a, height=250, scrolling=True)
            #st.html(codig1a, width=250, unsafe_allow_javascript=True)
            st.iframe(codig1a, height=250)
          with LINHA3A1[2]:
            codig1b='<!-- Widgets Notícias Agrícolas - www.noticiasagricolas.com.br/widgets --><script type="text/javascript" src="https://www.noticiasagricolas.com.br/widgets/cotacoes?&id=55&fonte=Arial%2C%19Helvetica%2C%19sans-serif&tamanho=9pt&largura=300px&cortexto=333333&corcabecalho=B2C3C6&corlinha=DCE7E9&imagem=true&output=js"></script>'
            #st.html(codig1b, height=250, scrolling=True)
            #st.html(codig1b, width=250, unsafe_allow_javascript=True)
            st.iframe(codig1b, height=250)
            st.markdown('<p style="font-size: 14px;color: blue;">Obs: Algodão: ¢R$ /Libra-peso(lp) <span style="font-family: symbol;">@ </span> 33,069/100 <span style="font-family: symbol;">@</span>1/3 <span style="font-family: symbol;">Þ</span> R$/@<span style="font-family: symbol;">/</span>1lp=0,453597 kg</p>',unsafe_allow_html=True)
            st.markdown('<p style="font-size: 14px;color: blue;">Ex: 70,98 (¢/lb)*33.069= 2347.238/100= 23.47238 (US$/@)*5.76= 135.20 (R$/@)</p>',unsafe_allow_html=True)
          with LINHA3A1[3]:
            codig1c='<!-- Widgets Notícias Agrícolas - www.noticiasagricolas.com.br/widgets --><script type="text/javascript" src="https://www.noticiasagricolas.com.br/widgets/cotacoes?id=81&fonte=Arial%2C%19Helvetica%2C%19sans-serif&tamanho=9pt&largura=300px&cortexto=333333&corcabecalho=B2C3C6&corlinha=DCE7E9&imagem=true&output=js"></script>'
            #st.html(codig1c, height=250, scrolling=True)
            #st.html(codig1c, width=250, unsafe_allow_javascript=True)
            st.iframe(codig1c, height=250)
            
        with st.container(height=250,border=False):
          LINHA4A1=st.columns([0.05,0.30,0.30,0.30,0.05],gap='medium')
          with LINHA4A1[1]:
            mls17a=st.multiselect(label='UFs', options=listagro, default=None, key='mls17a', help=None, on_change=None, args=None, kwargs=None, max_selections=3, placeholder="Escolha 3 opções", disabled=False)#label_visibility="visible"
            st.markdown("""<style>.stMultiSelect [data-baseweb=select] span{max-width: 200px;font-size: 0.8rem;}</style>""", unsafe_allow_html=True)
            mls17a2=[9826,9847,9832]
            if len(mls17a)==1:
              del mls17a2[-1]
              mls17a2.insert(0,dicagrolink[mls17a[0]])
            elif len(mls17a)==2:
              del mls17a2[-1]
              del mls17a2[-1]
              mls17a2.insert(0,dicagrolink[mls17a[0]])
              mls17a2.insert(1,dicagrolink[mls17a[1]])
            elif len(mls17a)==3:
              del mls17a2[-1]
              del mls17a2[-1]
              del mls17a2[-1]
              mls17a2.insert(0,dicagrolink[mls17a[0]])
              mls17a2.insert(1,dicagrolink[mls17a[1]])
              mls17a2.insert(2,dicagrolink[mls17a[2]])
            
            codig17a='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=%s,%s,%s&p=3446,3448,2017,3451&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'%(mls17a2[0],mls17a2[1],mls17a2[2])
            #st.html(codig17a, height=250, scrolling=True)
            #st.html(codig17a, width=250, unsafe_allow_javascript=True)
            st.iframe(codig17a, height=250)
          with LINHA4A1[2]:
            codig17b='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=9826,9830,9832&p=3441,3442,3443,2142&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'
            #st.html(codig17b, height=250, scrolling=True)
            #st.html(codig17b, width=250, unsafe_allow_javascript=True)
            st.iframe(codig17b, height=250)
          with LINHA4A1[3]:
            codig17c='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=9826,9832,9846&p=2149,1762,2075,1761&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'
            #st.html(codig17c, height=250, scrolling=True)
            #st.html(codig17c, width=250, unsafe_allow_javascript=True)
            st.iframe(codig17c, height=250)
            
        with st.container(height=250,border=False):#FAZENDO AINDA
          LINHA5A1=st.columns([0.05,0.30,0.30,0.30,0.05],gap='medium')
          with LINHA5A1[1]:
            codig18a='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=9826,9832,9839&p=11,1771,4160,1772&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'
            #st.html(codig18a, height=250, scrolling=True)
            #st.html(codig18a, width=250, unsafe_allow_javascript=True)
            st.iframe(codig18a, height=250)
            st.markdown('<p style="font-size: 14px;color: blue;">Boi gordo >= 18@)</p>',unsafe_allow_html=True)
          with LINHA5A1[2]:
            codig18b='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=9826,9839,9833&p=4076,4044,3899,3636&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'
            #st.html(codig18b, height=250, scrolling=True)
            st.html(codig18b, width=250, unsafe_allow_javascript=True)
          with LINHA5A1[3]:
            codig18c='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=cotacoes&uf=9826,9839,9847&p=3888,2143,1766,2145&l=&esp=&cor=rgb(232,193,58)&w=300&h=200"></iframe>'
            #st.html(codig18c, height=250, scrolling=True)
            #st.html(codig18c, width=250, unsafe_allow_javascript=True)
            st.iframe(codig18c, height=250)
        #https://www.agrolink.com.br/comercial/conteudo-gratuito
        with st.container(height=250,border=False):
          LINHA2A=st.columns([0.05,0.9,0.05],gap='medium')          
          with LINHA2A[1]:
            codig7='<iframe src="https://www.agron.com.br/widgets/cotacao_interna_horizontal.php" width="850px;" height="100px;" scrolling="no" frameborder="0" style="border-color:#F7F7F7; border:dotted 1px; border-color:#CCC"></iframe>'
            #st.html(codig7, height=150, scrolling=True)
            #st.html(codig7, width=250, unsafe_allow_javascript=True)
            st.iframe(codig7, height=250)
        
       
        #https://portaldeinformacoes.conab.gov.br/custos-de-producao.html
        
        #lerquadros(quadro=json.load(open(os.path.join(os.path.expanduser('~'), 'Desktop')+r"\Visualizador_Quest_Final_100924\quadros\quadro37_v1.json", 'r', encoding='utf-8-sig')))
      with tab02:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')   
        with st.container(height=250,border=False):
          LINHA2=st.columns([0.06,0.22,0.22,0.22,0.22,0.06],gap='small')                   
          with LINHA2[1]:
            codig14='<!-- Widgets Notícias Agrícolas - www.noticiasagricolas.com.br/widgets --><script type="text/javascript" src="https://www.noticiasagricolas.com.br/widgets/cotacoes?id=115&fonte=Arial%2C%20Helvetica%2C%20sans-serif&tamanho=10pt&largura=400px&cortexto=333333&corcabecalho=B2C3C6&corlinha=DCE7E9&imagem=true&output=js"></script>'
            #st.html(codig14, height=250, scrolling=True)
            #st.html(codig14, width=250, unsafe_allow_javascript=True)
            st.iframe(codig14, height=250)
          with LINHA2[2]:
            codig9='<iframe src="https://www.agron.com.br/widgets/dollar.php" width="290px;" height="220px;" scrolling="no" frameborder="0"></iframe>'
            #st.html(codig9, height=250, scrolling=True)
            #st.html(codig9, width=250, unsafe_allow_javascript=True)
            st.iframe(codig9, height=250)
          with LINHA2[3]:
             codig15='<!-- Widgets Notícias Agrícolas - www.noticiasagricolas.com.br/widgets --><script type="text/javascript" src="https://www.noticiasagricolas.com.br/widgets/cotacoes?id=232&fonte=Arial%2C%20Helvetica%2C%20sans-serif&tamanho=10pt&largura=400px&cortexto=333333&corcabecalho=B2C3C6&corlinha=DCE7E9&imagem=true&output=js"></script>'
             #st.html(codig15, height=250, scrolling=True)
             #st.html(codig15, width=250, unsafe_allow_javascript=True)
             st.iframe(codig15, height=250)
          with LINHA2[4]:
             #codig16='<iframe src="https://api.wo-cloud.com/content/widget/?geoObjectKey=16229787&language=pt&region=BR&timeFormat=HH:mm&windUnit=kmh&systemOfMeasurement=metric&temperatureUnit=celsius" name="CW2" scrolling="no" width="290" height="318" frameborder="0" style="border: 1px solid #10658E;border-radius: 8px"></iframe>'
             #st.html(codig16, height=250, scrolling=True)
             codig8='<iframe src="https://www.agron.com.br/widgets/banners-revistas.html" width="290px;" height="390px;" scrolling="no" frameborder="0"  align="middle"></iframe>'
             #st.html(codig8, height=250, scrolling=True)
             #st.html(codig8, width=250, unsafe_allow_javascript=True)
             st.iframe(codig8, height=250)
        with st.container(height=250,border=False):
          LINHA2b=st.columns([0.05,0.18,0.18,0.18,0.18,0.05],gap='small')                   
          with LINHA2b[1]:
            codig10='<iframe src="https://www.agron.com.br/widgets/ultimas-noticias.php?qtd=9&begin=0&largura=300&tamanho=12" width="300px;" height="900px;" scrolling="no" frameborder="0"  align="middle"></iframe>'
            #st.html(codig10, height=250, scrolling=True)
            #st.html(codig10, width=250, unsafe_allow_javascript=True)
            st.iframe(codig10, height=250)
          with LINHA2b[2]:
             codig11='<!-- Widgets Notícias Agrícolas - www.noticiasagricolas.com.br/widgets --><script type="text/javascript" src="https://www.noticiasagricolas.com.br/widgets/noticias?subsecao=2,3,162,6,8,10,64,80,85,146,5,4,11,12,156,40,158,60,13,163,97,14,95,205,15,1,155,84,28,149,26,69,90,62,27,92,148,154,32,101,102,103,105,207,106,107,108,109,147,206,110,111,112,113,159,114,157,115,116,210,68,164,117,118,119,204,211,120,121,203,166&largura=300px&altura=250px&fonte=Arial%2C%12Helvetica%2C%20sans-serif&tamanho=10pt&cortexto=333333&corlink=006666&qtd=40&output=js"></script>'
             #st.html(codig11, height=250, scrolling=True)
             #st.html(codig11, width=250, unsafe_allow_javascript=True)
             st.iframe(codig11, height=250)
          with LINHA2b[3]:
             codig18='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=noticias&uf=&p=&l=&esp=3218,5,1492,8723,6932,4397,15884,3525,3302,3180,93303,4112,1906,3139&cor=rgb(30,106,30)&w=300&h=200"></iframe>'
             #st.html(codig18, height=250, scrolling=True)
             st.html(codig18, width=250, unsafe_allow_javascript=True)
          with LINHA2b[4]:
             codig19='<iframe id="frmPreview" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="https://selos.agrolink.com.br/selos/carregaselo?servico=noticias&uf=&p=&l=&esp=3595,3775,4653,1231,3508&cor=rgb(30,106,30)&w=300&h=200"></iframe>'
             #st.html(codig19, height=250, scrolling=True)
             #st.html(codig19, width=250, unsafe_allow_javascript=True)
             st.iframe(codig19, height=250)


      with tab03:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
        codig16='<iframe src="https://api.wo-cloud.com/content/widget/?geoObjectKey=16229787&language=pt&region=BR&timeFormat=HH:mm&windUnit=kmh&systemOfMeasurement=metric&temperatureUnit=celsius" name="CW2" scrolling="no" width="290" height="318" frameborder="0" style="border: 1px solid #10658E;border-radius: 8px"></iframe>'
        #st.html(codig16, height=200, scrolling=True)
        st.html(codig16, width=250, unsafe_allow_javascript=True)
        #lerquadros(quadro=json.load(open(os.path.join(os.path.expanduser('~'), 'Desktop')+r"\Visualizador_Quest_Final_100924\quadros\quadro37b_v1.json", 'r', encoding='utf-8-sig')))
        #st.markdown('<div id="mrwid38568f23c749e3fb430fd6ba74dc3588"><script type="text/javascript" async src="https://api.meteored.com/widget/loader/38568f23c749e3fb430fd6ba74dc3588"></script></div>',unsafe_allow_html=True)
      with tab04:
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
        st.markdown('[      CONAB-custos       ](https://portaldeinformacoes.conab.gov.br/custos-de-producao.html).')
        st.markdown('[     ABRAFE       ](https://www.ibrafe.org).')
        st.markdown('[     HRAC - Herbicidas       ](https://www.hrac-br.org).')
        st.markdown('[     IRAC - Inseticidas       ](https://www.irac-br.org).')
        st.markdown('[     FRAC - Fungicidas       ](https://www.frac-br.org).')
        st.markdown('[Agrofit ](https://agrofit.agricultura.gov.br/agrofit_cons/principal_agrofit_cons).')
        st.markdown('[Embrapa-Macrologística](https://www.embrapa.br/macrologistica).')
        st.markdown('[Embrapa_exportação](https://www.embrapa.br/macrologistica/sistema/exportacao-agropecuaria).')
        st.markdown('[Nutrição de plantas](https://www.npct.com.br).')
        st.markdown('[ANDA - adubos](https://anda.org.br/).')
        st.markdown('[MAPA - biblioteca digital](https://repositorio-dspace.agricultura.gov.br/handle/1/1905).')
        st.markdown('[Canal Rural](https://www.canalrural.com.br/mercado-agroeconomico).')
        st.markdown('[Estatísticas IBGE](https://www.ibge.gov.br/estatisticas/economicas/agricultura-e-pecuaria.html).')
        st.markdown('[IBGE Produçao Agro](https://www.ibge.gov.br/explica/producao-agropecuaria/)')
        st.markdown('[IBGE CensoAgro_2017](https://censoagro2017.ibge.gov.br/resultados-censo-agro-2017.html)')
        
               
        st.markdown('[BC Crédito rural geral](https://www.bcb.gov.br/estabilidadefinanceira/creditorural)')
        
        st.markdown('[BC Crédito rural TUDO](https://www.bcb.gov.br/estabilidadefinanceira/micrrural)') 
        st.markdown('[BC Crédito rural API](https://dadosabertos.bcb.gov.br/)') 
        st.markdown('[BC Crédito rural API uf tipo](https://olinda.bcb.gov.br/olinda/servico/SICOR/versao/v2/odata/RegiaoUF?$top=100&$format=json&$select=cdRegiao,nomeRegiao,cdEstado,nomeUF,MesEmissao,AnoEmissao,cdPrograma,cdSubPrograma,cdFonteRecurso,Atividade,QtdCusteio,VlCusteio,QtdInvestimento,VlInvestimento,QtdComercializacao,VlComercializacao,QtdIndustrializacao,VlIndustrializacao)') 
        
        st.markdown('[BC Crédito rural custeio agrícola](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcCusteioAgricolaProdutoSegmentoIf.rdl)')
        st.markdown('[BC Crédito rural investimento agrícola](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcInvestimentoAgricolaProdutoSegmentoIf.rdl)')
        st.markdown('[BC Crédito rural comercialização agrícola](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcComercializacaoAgricolaSegmentoIfProduto.rdl)')
        
        st.markdown('[BC Crédito rural custeio pecuária](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcCusteioPecuarioProdutoSegmentoIf.rdl)')
        st.markdown('[BC Crédito rural investimento pecuária](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcInvestimentoPecuarioSegmentoIfProduto.rdl)')
        st.markdown('[BC Crédito rural comercialização pecuária](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcComercializacaoPecuariaProdutoSegmentoIf.rdl)')



        
        st.markdown('[BC Crédito rural UF Tipo](https://www.bcb.gov.br/estabilidadefinanceira/reportmicrrural/?path=conteudo%2FMDCR%2FReports%2FqvcRegiaoUFSegmentoIF.rdl)')        
        st.markdown('[BC operações de crédito](https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarGraficoPorId&hdOidSeriesSelecionadas=22027)')
        st.markdown('[BC operações de crédito json]https://api.bcb.gov.br/dados/serie/bcdata.sgs.22027/dados/ultimos/10?formato=json)')
        st.markdown('[BNDES desembolsos agro](https://api.bcb.gov.br/dados/serie/bcdata.sgs.7418/dados/ultimos/10?formato=json)')


        
        veda={'nome':['produtoa','produtob'],'imagem':['./Fisiologia/Fisiologia_1.png','./Fisiologia/ciclo_de_calvin.jpg']}
        df = pd.DataFrame(veda)
        from PIL import Image
        import base64
        def get_base64_image(image_path):          
          try:
             with open(image_path, "rb") as img_file:
                  return base64.b64encode(img_file.read()).decode('utf-8')
          except FileNotFoundError:
              return None
        def imagem2(x):
          saida=x['imagem']
          if saida.split('//')[-1][-3:]=='jpg':
            texto='img src="data:image/jpg;base64'
          else:
            texto='img src="data:image/png;base64'
          if get_base64_image(x['imagem']):          
            #saida2=st.markdown(f'<{texto},{get_base64_image(saida)}" width="100" height="100" />',unsafe_allow_html=True)
            saida2=f'<{texto},{get_base64_image(saida)}" width="100" height="100" />'
          else:
            saida2="Imagem não encontrada"
          return saida2
        df.loc[:,'Renderização de Imagem']=df.apply(imagem2,axis=1)
        df
        for i in range(df.shape[0]):
          st.markdown(df.iloc[i,-1],unsafe_allow_html=True)
        #st.dataframe(df[['nome', 'Renderização de Imagem']], use_container_width=True)
      with tab05:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE') 
        
        # if 'pdf_ref' not in ss:
        #   ss.pdf_ref = None
        # st.file_uploader("Folder classificação dos herbicidas.pdf", type=('pdf'), key='pdf_herb1')
        # if ss.pdf_herb1:
        #   ss.pdf_ref = ss.pdf_herb1 
        # if ss.pdf_ref:
        #   binary_data = ss.pdf_ref.getvalue()
        #   pdf_viewer(input=binary_data, width=700)  
        ViewPDF("Folder classificação dos herbicidas.pdf",compr=1200,larg=1000)
        #st.metric('Daninhas',8,2)
        herbi_a=st.columns([0.05,0.70,0.25],gap='small')
        import glob
        caminho='./Forrageiras_ou_daninhas/Plantas_daninhas_Embrapa'
        ler=glob.glob(caminho+'//*')
        dicherb={"Plantas daninhas 1":Path('poster1.pdf'),"Plantas daninhas 2":'./poster2.pdf',"Plantas daninhas 3":'./poster3_compressed.pdf', "Forrageiras":'./Forrageiras_ou_daninhas/Cartilha_Forrageiras_Zootécnico_compressed.pdf'}         
        cab1=["Plantas daninhas 1", "Plantas daninhas 2", "Plantas daninhas 3", "Forrageiras"]
        
        for i in range(len(ler)):
          cab1.append("Plantas daninhas %s"%(i+4))
          dicherb["Plantas daninhas %s"%(i+4)]=ler[i]
        cab2=tuple(cab1)
        with herbi_a[1]:
          Herb1 = st.selectbox("PLANTAS RESISTENTES",cab2)
          #st.markdown('<style>.stSelectbox > div { width: 100% !important; }</style>', unsafe_allow_html=True)
          st.markdown('<p style="font-size: 14px;color: blue;"><span style="font-family: Arial;">Principais Gêneros:</span> Panicum (Megathyrsus), brachiaria (Urochloa), Setaria, Paspalum, Cynodon, Andropogon, Pennisetum, Digitaria, etc... </p>',unsafe_allow_html=True)
          st.image('./Forrageiras_ou_daninhas/inflorescências.jpg',output_format='JPG', width=700)
        ViewPDF(dicherb[Herb1],compr=1200,larg=1000)
        
      with tab06:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')
        ViewPDF("Folder Classificação do Modo de Ação de Inseticidas.pdf",compr=1200,larg=1000)
      with tab07:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE')        
        ViewPDF("frac-moa-poster-2020v2.pdf",compr=1200,larg=1000)
      with tab08:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE') 
        with st.container(height=1000,border=False):
          Lnutri=st.columns([0.04,0.45,0.02,0.45,0.04],gap='small')                   
          with Lnutri[1]:
            venutri=st.image('./solo_nutrição/chave_diagnose_visual.jpg',output_format='JPG', width=700) 
          with Lnutri[3]:           
            solo1 = st.selectbox("Solos1",("Pedologia", "Fertilidade 1", "Fertilidade 2"))
          #st.markdown('<style>.stSelectbox > div { width: 100% !important; }</style>', unsafe_allow_html=True)
            dicsolo={"Pedologia":'./solo_nutrição/Pedologia.pdf',"Fertilidade 1":'./solo_nutrição/análise_fertilidade_solos.pdf',"Fertilidade 2":'./solo_nutrição/Nutrifatos.pdf'}         
            ViewPDF(dicsolo[solo1],compr=800,larg=800) 
      with tab09:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE') 
        with st.container(height=1000,border=False):
          import glob
          Lfisio=st.columns([0.04,0.45,0.02,0.45,0.04],gap='small')  
          lerfisio=glob.glob('./Fisiologia/Fotossintese_resumo'+'//*')
          lerfisio2=glob.glob('./Fisiologia/Fotossintese_resumo2'+'//*')
          dicfisio={"Nitrogênio":'./Fisiologia/METABOLISMO_DO_NITROGÊNIO.pdf',
                     "Reguladores":'./Fisiologia/Fitormônios.pdf'}          
          cabfisio1=["Nitrogênio", "Reguladores"]
        
          for i in range(len(lerfisio2)):
            cabfisio1.append("Fotossintese1_%s"%(i+1))
            dicfisio["Fotossintese1_%s"%(i+1)]=lerfisio2[i]
          
          for i in range(len(lerfisio)):
            cabfisio1.append("Fotossintese2_%s"%(i+1))
            dicfisio["Fotossintese2_%s"%(i+1)]=lerfisio[i]            
          
          cabfisio2=tuple(cabfisio1)                      
           
          with Lfisio[1]:           
            fisio1 = st.selectbox("Fisiologia",("Calvin 1", "Calvin 2", "Krebs", "Aminoácidos 1","Aminoácidos 2","Aminoácidos 3","Aminoácidos 4","Geral 1","Geral 2","Geral 3", "Nitrogênio2", "Nitrogênio3","CHIQUIMATO"))
          #st.markdown('<style>.stSelectbox > div { width: 100% !important; }</style>', unsafe_allow_html=True)
            dicfisiologia={"Calvin 1":'./Fisiologia/ciclo_de_calvin_2.jpg',"Calvin 2":'./Fisiologia/ciclo_de_calvin.jpg',"Krebs":'./Fisiologia/Fisiologia_krebs.jfif',
                           "Aminoácidos 1":'./Fisiologia/aminoácidos2.jfif', "Aminoácidos 2":'./Fisiologia/Aminoacids.png',"Aminoácidos 3":'./Fisiologia/códon_aminoácidos2.jfif',
                           "Aminoácidos 4":'./Fisiologia/códon_aminoácidos.jpg', "Geral 1":'./Fisiologia/Fisiologia_1.png', "Geral 2":'./Fisiologia/Fisiologia_2.jfif',
                           "Geral 3":'./Fisiologia/plantas_c3-c4-cam.jfif',"Nitrogênio2":'./Fisiologia/Nitrogênio2.jpg', "Nitrogênio3":'./Fisiologia/Nitrogênio3.jpg','CHIQUIMATO':'./Fisiologia/VIA_CHIQUIMATO1.jpg'}   
            dicfisiologia2={"Calvin 1":'JPG',"Calvin 2":'JPG',"Krebs":'JFIF',
                           "Aminoácidos 1":'JFIF', "Aminoácidos 2":'PNG',"Aminoácidos 3":'JFIF',
                           "Aminoácidos 4":'JPG', "Geral 1":'PNG', "Geral 2":'JFIF',
                           "Geral 3":'JFIF',"Nitrogênio2":'JPG',"Nitrogênio3":'JPG','CHIQUIMATO':'JPG'}       
            venfisio1=st.image(dicfisiologia[fisio1],output_format='%s'%(dicfisiologia2[fisio1]), width=700) 
            if fisio1=='CHIQUIMATO':
              st.markdown('<p style="font-size: 14px;color: blue;"><span style="font-family: Arial;">Glifosato:</span>Afeta a produção de aminoácidos aromáticos por inibir a EPSPs (Enolpiruvilshiquimatofosfato sintase)  </p>',unsafe_allow_html=True)

          with Lfisio[3]:           
            fisio2 = st.selectbox("Fisiologia 2",cabfisio2)
          #st.markdown('<style>.stSelectbox > div { width: 100% !important; }</style>', unsafe_allow_html=True)
            #dicfisio               
            
            if  fisio2=="Reguladores":
              st.markdown('<p style="font-size: 14px;color: blue;"><span style="font-family: Arial;">Paclobutrazol </span> é um fitormônio que inibe a síntese de giberelina e reduz o crescimento vegetativo, auxiliando o desenvolvimento de frutos. Ex: usado em Mangueiras </p>',unsafe_allow_html=True)
   
            ViewPDF(dicfisio[fisio2],compr=800,larg=800)
            #ViewPDF(dicfisiologia[fisio1],compr=800,larg=800) 
        #nutri1='<iframe id="frmNutri1" frameborder="0" scrolling="no" width="300" height="200" style="border:none;" src="%s"></iframe>'%(venutri)
        #st.html(nutri1, height=250, scrolling=True)
              
        #ViewPDF("frac-moa-poster-2020v2.pdf",compr=1200,larg=1000)           
#with open('styles.css') as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
      with tab10:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE') 
        with st.container(height=1000,border=False):
          Lhorti=st.columns([0.04,0.45,0.02,0.45,0.04],gap='small')
          cabhorti=['Plantio']
          cabhorti1=tuple(cabhorti)
          dichorti1={"Plantio":'./Hortifruti/Horti/tabela_Embrapa_Hortaliças.pdf'}
          with Lhorti[1]:           
            Horti1 = st.selectbox("Horticultutra",cabhorti1)           
            ViewPDF(dichorti1[Horti1],compr=650,larg=800)
          cabfruti=['Banana1','Banana2','Abacaxi1','Abacaxi2','Abacaxi3','Goiaba','Mamão1','Mamão2','Maracujá', 'Melancia','Melão1','Melão2','Melão3','Morango',
                    'Uva1','Uva2','Uva3','Uva4','Limão','Atemóia','Manga1','Manga2','Figo','Citrus_1','Citrus_2','Citrus_3','Citrus_4','Citrus_5','Citrus_6']
          cabfruti1=tuple(cabfruti)
          dicfruti1={"Banana1":'./Hortifruti/banana.pdf',"Banana2":'./Hortifruti/gabarito_banana-2.pdf',"Abacaxi1":'./Hortifruti/abacaxi.pdf',
                     "Abacaxi2":'./Hortifruti/gab_abacaxi.pdf',"Abacaxi3":'./Hortifruti/gab_abacaxi_perola_v4.pdf',"Goiaba":'./Hortifruti/goiaba.pdf',
                     "Mamão1":'./Hortifruti/mamao.pdf',"Mamão2":'./Hortifruti/Gabarito_mamao-2.pdf',"Maracujá":'./Hortifruti/maracuja.pdf',"Melancia":'./Hortifruti/melancia.pdf',
                     "Melão1":'./Hortifruti/melao.pdf',"Melão2":'./Hortifruti/gabarito_melao__peledsapo.pdf',"Melão3":'./Hortifruti/gabarito_melao_amarelo.pdf',
                     "Morango":'./Hortifruti/morango.pdf',"Uva1":'./Hortifruti/uva_fina.pdf',"Uva2":'./Hortifruti/uva_rustica.pdf',"Uva3":'./Hortifruti/uva_sem_semente.pdf',
                     "Uva4":'./Hortifruti/uvafina.pdf',"Uva5":'./Hortifruti/gabarito_uva_americana.pdf',"Limão":'./Hortifruti/gabarito_limao-2.pdf',
                     "Atemóia":'./Hortifruti/gabarito_atemoia-2.pdf',"Manga1":'./Hortifruti/manga_a.pdf',"Manga2":'./Hortifruti/Gabarito_manga-2.pdf',"Figo":'./Hortifruti/figo_novo.pdf',
                     "Citrus_1":'./Hortifruti/citrus-2.pdf',"Citrus_2":'./Hortifruti/citrus-3.pdf',"Citrus_3":'./Hortifruti/citrus-4-5.pdf',"Citrus_4":'./Hortifruti/citrus-6-7.pdf',
                     "Citrus_5":'./Hortifruti/citrus-8-9.pdf',"Citrus_6":'./Hortifruti/citrus-10.pdf'}
          with Lhorti[3]:           
            Fruti1 = st.selectbox("Fruticultura",cabfruti1)           
            ViewPDF(dicfruti1[Fruti1],compr=650,larg=800)
      with tab11:   
        cabecalho(cab1='INFORMAÇÕES AGRÍCOLAS',cab2='IBGE') 
        with st.container(height=1000,border=False):
          import glob
          Lcenso=st.columns([0.05,0.90,0.05],gap='small')  
          lercenso=glob.glob('./Censo_2017'+'//*')    
          cabcenso1=[]
          diccenso={}
          lercenso[0].split('/')[-1].split(' ')[-1].split('.')[0].upper()
          for i in range(len(lercenso)):
            cabcenso1.append(lercenso[i].split('/')[-1].split(' ')[-1].split('.')[0].upper())
            diccenso[lercenso[i].split('/')[-1].split(' ')[-1].split('.')[0].upper()]=lercenso[i]          
                   
          
          cabcenso2=tuple(cabcenso1)                     
          
          with Lcenso[1]:           
            censo2 = st.selectbox("Censo 2017",cabcenso2)
          
            ViewPDF(diccenso[censo2],compr=1500,larg=1500)
def main():    
    st.set_page_config(
        page_title="Dashboard Agro",
        #page_icon=st.markdown(':sunflower:,:seedling:'),
        page_icon="🌱",
        layout="wide",  
        initial_sidebar_state="expanded"
        )
    
    with open('styles.css') as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    tabelaestilo = '''<style>      
      
      div [data-testid='stAppViewBlockContainer'] {
        background-color:#cc9999;
        width:99%;
      }
      div [data-testid='stVerticalBlockBorderWrapper'] {
        background-color:#cc99aa;
        width:99%;
      }
      div [data-testid='stSidebarContent'] {
        background-color:#cc9968;
      }
      div [data-testid='stRadio'] {
        background-color:#cc9968;
      }
      div [data-testid='stHeader'] {
        background-color:#cc9999;
        width:100%;
      }
      div [data-testid="element-container"][class="element-container st-emotion-cache-w3csf9 e1f1d6gn4"] {        
        heigth:20%;
        }
      </style>'''
    st.markdown("""
    <style>
        @media (max-width: 768px) {
            /* Reduz o tamanho do título principal no celular */
            h1 {
                font-size: 1.8rem !important;
            }
            /* Diminui o espaçamento das bordas da tela */
            .block-container {
                padding-top: 2rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }
    </style>""", unsafe_allow_html=True)
      #caso queira cada linha da tabela formatada coloque o código abaixo
      #div[data-testid="element-container"]{
      #  margin:0.1%;
      #  top:%;
      #  padding:0%;
      #  background-color:#cca9a9; 
      #  width:99%;}            
      
      
      
      
      #div [data-testid='stTabs'] {
      #background-color:#cca999;
      #width:99%; 
      #}
    st.markdown(tabelaestilo,unsafe_allow_html=True)
    #esse div[data-testid="element-container"] = REALMENTE MUDA AS CONFIGURAÇÕES NA TABELA
    
        
    #html('<hr size="4" color="blue"  style="border:2px solid #4585cc; margin:1px auto;">')
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)
    #---PARA GUARDAR TODAS AS VARIÁVEIS E PODER ACESSAR EM VÁRIAS PÁGINAS
    #try:
    #  for k, v in st.session_state.to_dict().items():
    #    st.session_state[k] = v
    #except:
    #  pass
    
    with st.sidebar:
      st.image('./imagem_fazenda/logotipo_trator_cubista_colorido.jpg',output_format='JPG', width=300)
    choices = st.sidebar.radio('Quadros', ('Pesquisas','Censo','PAM',"PPM","PEVS","Informação"), index=5)
    
    #st.markdown(':sunflower:,:seedling:') 
    
    #link2={}  
    if choices=='Pesquisas':         
      tudo()
      #pass
    if choices=='Censo':         
      censo()      
    if choices=='PAM':
      #pam()
      pass
    if choices=='PPM':
      #ppm()
      pass
    if choices=='PEVS':
      #pevs()
      pass
    if choices=='Informação':
      Info()
    st.sidebar.image('./imagem_fazenda/logotipo_peixe_cubista.jpg',output_format='JPG', width=300)
    #with st.sidebar:
      #st.image('./imagem_fazenda/logotipo_trator_cubista_colorido.jpg',output_format='JPG', width=300)


    #qual_tabela(6953)
    #info_tabela_escolhida()
    #st.session_state   
    #with open('styles.css') as f:
    #    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    #imagem_fundo(imagem='fazenda_colorida.jpg',tipo='jpg')
if __name__ == "__main__":
    main()
