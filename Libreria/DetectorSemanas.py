from datetime import datetime, timedelta
def deteccion_semanas(fecha_inicial,fecha_final,formato_fecha): #'%Y-%m-%d' ; '%Y/%m/%d'
    fecha_dti = datetime.strptime(fecha_inicial, formato_fecha)
    fecha_dtf = datetime.strptime(fecha_final, '%Y-%m-%d')
    semanas = int(((fecha_dtf-fecha_dti).days)/7)
    return semanas
