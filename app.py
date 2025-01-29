import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Cargar el modelo y el escalador desde archivos
with open('preprocessor.pkl', 'rb') as preprocessor_file:
    loaded_preprocessor = pickle.load(preprocessor_file)

with open('kmeans_model.pkl', 'rb') as model_file:
    loaded_kmeans = pickle.load(model_file)


# Título de la aplicación
st.title('Predicción de si el cliente pertenese al cluster 1() o 0()')

# Entrada de datos del usuario
job = st.selectbox('Trabajo', ['profesional','t_manuales','out_laboral','unknown'], index=None, placeholder="seleccione una opcion")
marital = st.selectbox('Estado civil',['single','married','divorced'], index=None, placeholder="seleccione una opcion" )
education = st.selectbox('Educacion', ['primary','secondary','tertiary','unknown'], index=None, placeholder="seleccione una opcion")
default = st.selectbox('Default', ['si','no',], index=None, placeholder="seleccione una opcion")
balance = st.number_input('Balance de cuenta del cliente (euros)', min_value=0)
housing = st.selectbox('Housing', ['si','no',], index=None, placeholder="seleccione una opcion")
loan = st.selectbox('Loan', ['si','no',], index=None, placeholder="seleccione una opcion")

# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'job': [job],
    'marital': [marital],
    'education': [education],
    'default': [default],
    'balance': [balance],
    'housing': [housing],
    'loan': [loan]
})

# Estandarizar las entradas
user_data_standardized = preprocessor_file.transform(user_data)

# Realizar la predicción
prediction_cluster = model_file.predict(user_data_standardized)


# Mostrar la predicción
st.write(f'"El cliente pertenece al cluster: {prediction_cluster[0]}')