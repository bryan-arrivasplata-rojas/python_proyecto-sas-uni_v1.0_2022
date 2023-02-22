from datetime import datetime, timedelta
def deteccion_dia_semana(fecha_detectar,formato_fecha): #'%Y-%m-%d' ; '%Y/%m/%d'
    fecha_dti = datetime.strptime(fecha_detectar, formato_fecha)
    #fecha_dtf = datetime.strptime(fecha_detectar, '%Y-%m-%d')
    dia_semana = fecha_dti.strftime('%A')
    return dia_semana
