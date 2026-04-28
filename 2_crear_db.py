import pandas as pd
import sqlite3

df = pd.read_csv('omega_bruto.csv')

df_limpio = df.dropna(subset=['pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag'])

arqueo = sqlite3.connect('arqueologia.db')
df_limpio.to_sql('estrellas', arqueo, if_exists='replace', index=False)
arqueo.close()

print("Se crea la base de datos llamada arqueologia.db")
