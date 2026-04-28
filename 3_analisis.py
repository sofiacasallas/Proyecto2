import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

arqueo=sqlite3.connect('arqueologia.db')
df=pd.read_sql('SELECT * FROM estrellas', arqueo)

#Diagrama racimo completo
plt.figure(figsize=(8, 6))
plt.scatter(df['pmRA'], df['pmDE'], color='purple')
plt.xlabel('pmRA')
plt.ylabel('pmDE')
plt.title('Movimiento propio de Omega Centauri')
plt.grid(True)
plt.savefig('mov_propio.png')
print("Análisis completado. Se guarda la imagen en mov_propio.png")

#Filtro SQL avanzado
df_filtro=pd.read_sql('SELECT * FROM estrellas WHERE pmRA BETWEEN -8 AND 2 AND pmDE BETWEEN -12 AND -2', arqueo)

#Diagrama racimo filtrado de color-magnitud
df_filtro['color_BP_RP']=df_filtro['BPmag']-df_filtro['RPmag']
plt.figure(figsize=(8, 6))
plt.scatter(df_filtro['color_BP_RP'], df_filtro['Gmag'], color='crimson')
plt.gca().invert_yaxis()
plt.xlabel('BP - RP')
plt.ylabel('G')
plt.title('Diagrama Color-Magnitud de Omega Centauri')
plt.grid(True)
plt.savefig('diagrama_HR.png')
print("Análisis completado. Se guarda la imagen en diagrama_HR.png")
