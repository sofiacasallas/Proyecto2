# **Proyecto 2 - Sofía Lorena Casallas Beltrán**

## **Arqueología Galáctica y el Misterio de Omega Centauri**

### **Coordenadas**
- **Ascensión recta:** 201.6967
- **Declinación:** -47.4795

Este repositorio contiene el archivo `1_descarga_omega.sh` que descarga 
los datos de la misión Gaia DR3, con el archivo extraido, en `2_crear_db.py` se limpian
los datos para que tenga valores NaN, esto para finalmente utilizarlos en
`3_analisis.py` donde se  genera el diagrama de movimiento propio y el diagrama 
Color-Magnitud de Omega Centauri.

### *Resultados**

#### **Gráfica 1: Movimiento Propio**
![Movimiento Propio](mov_propio.png)

En esta gráfica se distingue los dos grupos esperados desde la teoría: una nube con estrellas que corresponden a
estrellas que pertenecen a la Vía Láctea y un raximo denso que corresponde a Omega Centauri, el cual se busca definir
su tamaño para analizar exclusivamente las estrellas de este cúmulo. El hecho de que todas compartan el mismo 
vector de movimiento confirma que están gravitacionalmente ligadas.

#### **Gráfica 2: Diagrama Color-Magnitud**
![Diagrama HR](diagrama_HR.png)

Al aplicar el filtro SQL sobre el racimo cinemático, el diagrama 
Color-Magnitud se ve notablemente más limpio que si se graficaran todas 
las estrellas del campo. Sin el filtro, las estrellas "intrusas" de la 
Vía Láctea — que están a distintas distancias y tienen edades y 
composiciones químicas variadas — contaminarían el diagrama produciendo 
una nube de puntos sin estructura reconocible. Al removerlas con SQL, 
emergen claramente:

- **Secuencia Principal:** franja diagonal densa, estrellas que aún 
queman hidrógeno.
- **Punto de Apagado:** donde la secuencia se dobla hacia arriba, 
permite estimar la edad del cúmulo en ~12 mil millones de años.
- **Rama de Gigantes Rojas:** línea que asciende hacia colores más rojos.
- **Rama Horizontal:** gancho visible alrededor de magnitud G=14-15.

Esto demuestra que SQL no es solo una herramienta técnica sino científica: 
al filtrar por movimiento propio se logró aislar una población estelar 
coherente y reconstruir la historia de una galaxia devorada por la Vía Láctea.
