echo "Iniciando pipeline con descarga de omega_bruto.csv"

#Consulta SQL
QUERY="SELECT TOP 50000 Source,RA_ICRS,DE_ICRS,pmRA,pmDE,Gmag,BPmag,RPmag FROM \"I/355/gaiadr3\" WHERE 1=CONTAINS(POINT('ICRS',RA_ICRS,DE_ICRS),CIRCLE('ICRS',201.6967,-47.4795,0.5))"

#Endpoint explícito
ENDPOINT="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

#Se arregla el URL
URL="${ENDPOINT}${QUERY}"
URL_CLEAN=$(echo $URL | sed 's/ /%20/g')

wget -q -O omega_bruto.csv "$URL_CLEAN"

echo "Datos descargados exitosamente"
