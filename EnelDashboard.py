from gather_data import df_konecta, df_total, getData, plotDistributions
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns

#plt.figure(figsize=(21,10))
st.title("Análisis 4A y Distribución en el tiempo")
#habilidad = "Agilizar"
habilidad = st.selectbox(
'Elige la habilidad',
('Agilizar', 'Asesorar', 'Acoger', 'Asistir'))

proveedor = st.selectbox(
'Elige el proveedor',
('UPCOM', 'KONECTA', 'AMBOS JUNTOS','AMBOS SEPARADOS'))

if proveedor == "UPCOM":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.kdeplot(
        data=getData(df_total.reset_index(),"UPCOM",habilidad), x="SEMANA", y="SCORE",
        fill=True, thresh=0, levels=100, cmap="mako")
    st.pyplot()

if proveedor == "KONECTA":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #plt.figure(figsize=(21,10))
    fig2 = sns.kdeplot(
        data=getData(df_total.reset_index(),"KONECTA",habilidad), x="SEMANA", y="SCORE",
        fill=True, thresh=0, levels=100, cmap="rocket")
    st.pyplot()

if proveedor == "AMBOS SEPARADOS":
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.kdeplot(
        data=getData(df_total.reset_index(),"UPCOM",habilidad), x="SEMANA", y="SCORE",
        fill=True, thresh=0, levels=100, cmap="mako")
    st.pyplot()

    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.kdeplot(
        data=getData(df_total.reset_index(),"KONECTA",habilidad), x="SEMANA", y="SCORE",
        fill=True, thresh=0, levels=100, cmap="rocket")
    st.pyplot()


if proveedor == "AMBOS JUNTOS":
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.kdeplot(
        data=getData(df_total.reset_index(),"ALL",habilidad), x="SEMANA", y="SCORE",
        fill=True, thresh=0, levels=100, cmap="mako")
    st.pyplot()

