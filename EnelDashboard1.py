from gather_data import df_konecta, df_total, getData, plotDistributions, ejecutivos 
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt

def ejecutivos_chart(ejecutivos_array, agg = True):

  if agg == True:

    plt.figure(figsize = ((21,8)))
    for j in range(len(ejecutivos_array)):
      st.set_option('deprecation.showPyplotGlobalUse', False)
      plt.plot(ejecutivos_array[j]['FECHA'],ejecutivos_array[j]['SCORE'])
    st.pyplot()

  else:

    for k in range(len(ejecutivos_array)):
      st.set_option('deprecation.showPyplotGlobalUse', False)
      plt.figure(figsize = (21,4))
      plt.title(ejecutivos_array[k].iloc[0,2])
      plt.plot(ejecutivos_array[k]['FECHA'],ejecutivos_array[k]['SCORE'])
      plt.rcParams.update({'figure.max_open_warning': 0})
      st.pyplot()

st.title("Progreso por ejecutivo en el tiempo")

habilidad = st.selectbox(
'Elige la habilidad',
('Agilizar', 'Asesorar', 'Acoger', 'Asistir'))

proveedor = st.selectbox(
'Elige el proveedor',
('UPCOM', 'KONECTA'))


todos = list(getData(df_total,proveedor,habilidad)['NOMBRE'])
todos.insert(0,"TODOS")
todos = tuple(todos)
ejs = st.selectbox(
'Selecciona un ejecutivo',
(todos))

if ejs == "TODOS":      
    ejecutivos_chart(ejecutivos(getData(df_total,proveedor,habilidad)),True)
else:
    ejecutivos_chart(ejecutivos(getData(df_total,proveedor,habilidad,ejs)),False)


