import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('preprocessor.pkl', 'rb') as preprocessor_file:
    loaded_preprocessor = pickle.load(preprocessor_file)

with open('kmeans_model.pkl', 'rb') as model_file:
    loaded_kmeans = pickle.load(model_file)


# Título de la aplicación
st.title('Predicción de si el cliente pertenese al cluster 1() o 0()')

# Entrada de datos del usuario
job = st.selectbox('Trabajo (seleccione una opcion)', ['profesional','t_manuales','out_laboral','unknown'])
marital = st.selectbox('Estado civil (seleccione una opcion)',['single','married','divorced'])
education = st.selectbox('Educacion (seleccione una opcion)', ['primary','secondary','tertiary','unknown'])
default = st.number_input('Default (1 = si, 0 = no)', min_value=0, max_value=1)
balance = st.number_input('Balance de cuenta del cliente (euros)', min_value=0)
housing = st.number_input('Housing (1 = si, 0 = no)', min_value=0)
loan = st.number_input('loan (1 = si, 0 = no)', min_value=0)

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

# Mostrar la predicción
st.write(f'"El cliente pertenece al cluster: {prediction_cluster[0]}')