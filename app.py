import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('preprocessor.pkl', 'rb') as preprocessor_file:
    loaded_preprocessor = pickle.load(preprocessor_file)

with open('kmeans_model.pkl', 'rb') as model_file:
    loaded_kmeans = pickle.load(model_file)


# Título de la aplicación
st.title('Clasificación de Clientes Bancarios')

# Entrada de datos del usuario
job = st.selectbox('Actividad laboral (seleccione una opción)', ['blue-collar','entrepreneur','housemaid','management','retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
marital = st.selectbox('Estado civil (seleccione una opción)',['single','married','divorced'])
education = st.selectbox('Educación (seleccione una opción)', ['primary','secondary','tertiary','unknown'])
default = st.radio('¿Tiene crédito en mora?', [0, 1], captions=["No","Si"], horizontal=True)
balance = st.number_input('Balance (Saldo medio anual en euros)', min_value=0)
housing = st.radio('¿Tiene préstamo hipotecario?', [0, 1], captions=["No","Si"], horizontal=True)
loan = st.radio('¿Tiene préstamo personal?', [0, 1], captions=["No","Si"], horizontal=True)


# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'job': [job],
    'marital': [marital],
    'education': [education],
    'default_encoded': [default],
    'balance': [balance],
    'housing_encoded': [housing],
    'loan_encoded': [loan]
})

# Estandarizar las entradas
user_data_standardized = loaded_preprocessor.transform(user_data)

# Realizar la predicción
prediction_cluster = loaded_kmeans.predict(user_data_standardized)


st.write("Resultado del Clustering: ")

# Mostrar la predicción
if prediction_cluster[0] == 0:
    st.write("***El cliente pertenece al Cluster 0, tiene mayor probabilidad de adquirir un depósito a plazo.***")
else:
    st.write("***El cliente pertenece al Cluster 1, tiene menor probabilidad de adquirir un depósito a plazo.***")
