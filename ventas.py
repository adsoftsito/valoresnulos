import pandas as pd
import numpy as np

df=pd.read_csv("ventas_totales.csv")
#print(df.head()) # top 5 rows
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

# quitar nulo en columna salon_ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#quitar nulos de columna tarjetas_debito
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#quitar nulos a tarjetas_credito
df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

#print(df['otros_medios'].describe())
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
#valores_nulos=df.isnull().sum()
#print(valores_nulos)

# rellena valores nulos con metodo ffill
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# rellena valores nulos con metodo bfill
df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

# rellena con ceros la columna panaderia
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
print(valores_nulos)


#Convertir DataFrame a CSV
df.to_csv('ventas_totales_limpio.csv')