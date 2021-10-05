
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow.keras
import sklearn.linear_model
import plotly.graph_objects as go


def getData(df_,proveedor = "ALL",tipo = 'Asistir',ejecutivo = "" ):
  proveedor.upper()

  if (proveedor ==  "ALL"):
    return df_[(df_['TIPO'] == tipo)]
  else: 
    if ejecutivo != "":
      return df_[(df_['PROVEEDOR'] == proveedor ) & (df_['TIPO'] == tipo) & (df_['NOMBRE'] == ejecutivo)]
    else:
      return df_[(df_['PROVEEDOR'] == proveedor ) & (df_['TIPO'] == tipo)]

def ejecutivos(df):
  ejecutivos = []
  for i in df['NOMBRE'].unique():
    ejecutivos.append(df[df['NOMBRE']==i])
  return ejecutivos

def plotDistributions(data):
  #import seaborn as sns
  sns.displot(
    data=data,
    x="SCORE", hue="SEMANA",
    kind="kde", height=10,
    multiple="fill", clip=(0, None),
    palette="ch:rot=-.25,hue=1,light=.75",
  ).set(title='Distribución Scores respecto a semana')

  import matplotlib as mpl
  f, ax = plt.subplots(figsize=(20, 8))
  sns.despine(f)
  sns.histplot(
    data,
    x="SCORE", hue="SEMANA",
    multiple="stack",
    palette="rocket",
    edgecolor=".3",
    linewidth=.5,
    ).set(title = "Distribución y evolución según semana")
  ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())

def ejecutivos_chart(ejecutivos_array, agg = False):

  if agg == True:

    plt.figure(figsize = ((21,8)))
    for j in range(len(ejecutivos_array)):
      plt.plot(ejecutivos_array[j]['FECHA'],ejecutivos_array[j]['SCORE'])

  else:

    for k in range(len(ejecutivos_array)):
      plt.figure(figsize = (21,4))
      plt.title(ejecutivos_array[k].iloc[0,2])
      plt.plot(ejecutivos_array[k]['FECHA'],ejecutivos_array[k]['SCORE'])
      plt.rcParams.update({'figure.max_open_warning': 0})

def progressChart(df):
  import plotly.express as px
  fig = px.bar(df, x="SCORE", y="SEMANA", orientation='h')
  fig.show()
##################################################################################################################

permanencia_upcom = pd.read_excel("https://raw.githubusercontent.com/vichudo/enelData/main/BASE%20UPCOM.xlsx",date_parser=True)
permanencia_konecta = pd.read_excel("https://github.com/vichudo/enelData/raw/main/Listado%20de%20usuarios%20Chile-Colombia.xlsx", date_parser=True)
all = pd.read_excel('https://raw.githubusercontent.com/vichudo/enelData/main/AcumuladoStandarized.xlsx')

permanencia_upcom['PROVEEDOR'] = "UPCOM"
permanencia_konecta['PROVEEDOR'] = "KONECTA"


for i in range(len(permanencia_konecta)):
  permanencia_konecta['PAIS'][i] = permanencia_konecta['PAIS'][i].upper()
  permanencia_konecta['NOMBRE'][i] = permanencia_konecta['NOMBRE'][i].upper()
  
for i in range(len(all)):
  all['NOMBRE'][i] = all['NOMBRE'][i].upper()
#permanencia_konecta = permanencia_konecta.dropna()
#permanencia_upcom = permanencia_upcom.dropna()

##################################################################################################################


df_konecta = pd.merge(permanencia_konecta, all, on = "NOMBRE")
df_konecta = df_konecta.drop(columns='PROVEEDOR_x')
df_upcom = pd.merge(permanencia_upcom, all, on = "NOMBRE")
df_upcom = df_upcom.drop(columns='PROVEEDOR_x')

df_total = df_konecta.append(df_upcom)
df_total = df_total.rename(columns={'PROVEEDOR_y':'PROVEEDOR'})
df_total = df_total.sort_values('FECHA')




#####################################################################################################################



