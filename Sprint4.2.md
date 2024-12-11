# Proceso de Recoleccion de Datos del Proyecto de Segmentacion de Clientes para Campañas Personalizadas    

## 1. Fuentes
**Identificacion de fuentes**
- Base de datos interna del Banco

**Descripcion de las fuentes**
- La base de datos cuenta con algunos registros demograficos de los clientes del banco, igualmente hay registros de los contactos realizados de previas campañas de marketing asi como algunos de los servicios que tiene el cliente suscritos con el banco.

## 2. Metodo de Recoleccion de datos
**Procedimientos y Herramientas**
Se hace mediante exportacion manual, extraida de su lugar de almacenaje en la nube (Servicio de Azure)por el equipo de Data Science del Banco y cuando se requiere.   

**Frecuencia de Recolección**
Mensualmente

**Script de Descarga**


```python
import pandas as pd

csv_url = "https://github.com/StephanieRO/Machine_Learning_project/blob/main/bank_dataset.CSV"
df = pd.read_csv(csv_url)
print(df.info())
```

## 3. Formato y Estructura de los Datos
**Tipos de datos**
Numericos: edad, balance, día, duracion, campaña, pdias, previous

Categoricos: job, marital, education, contact, month, pcontact

Binarios: usuario con deposito, default, housing, loan

**Formato de Almacenamiento**
Datos tabulares almacenados en un fichero csv

## 4. Limitaciones de los datos
Frecuencia de contacto: No todos los usuarios han sido contactados previamente la misma cantidad de veces y se tendria algunos missing values. 

## 5. Consideraciones sobre datos sensibles
**Tipos de datos sensibles**
Información financiera sensible: loan, housing, balance
Sesgo: job 

**Medidas de Protección**
- Accesos restringido: Acceso a datos sensibles restringido sólo a personal autorizado con necesidad de conocer estos datos para fines específicos del proyecto.
- Cumplimiento de Regulación: Cumplimiento con la GDRP

