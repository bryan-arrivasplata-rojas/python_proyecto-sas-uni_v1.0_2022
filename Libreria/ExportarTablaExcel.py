import pandas as pd
import subprocess
from Libreria.RutaExactaPath import *

def exportarExcel(lista_reporte,cabezera_reporte,nombre_excel):
    df_rrss = pd.DataFrame(lista_reporte,columns=cabezera_reporte) #columns=['Nombre','Cantidad','ES_FBK','Anio']
    filename = "Recursos/EXCEL_EXPORTADOS/"+nombre_excel+".xlsx"
    df_rrss.to_excel(filename)
    path = resolver_ruta(filename)
    subprocess.Popen([path], shell=True)

'''fbk = ['Facebook',2449,True,2006]
twt = ['Twitter',2449,True,2006]
ig = ['Instagram',2449,True,2006]
yt = ['Youtube',2449,True,2006]
lkn = ['LinkenIn',2449,True,2006]

lista_rrs = [fbk,twt,ig,yt,lkn]
print(lista_rrs)

df_rrss = pd.DataFrame(lista_rrs,columns=['Nombre','Cantidad','ES_FBK','Anio'])
df_rrss.to_excel('data.xlsx')'''