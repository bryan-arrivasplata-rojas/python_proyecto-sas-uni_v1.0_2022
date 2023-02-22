from wx.core import QueryNewPaletteEvent
from DataBase.Conexion import consulta_sin_variable,consulta_con_variable

def insert(string, tupla):
    query = consulta_con_variable(string, tupla)
    return query

'''def consult(string):
    query = consulta_sin_variable()
    return query

def consulta(string, tupla):
    query = consulta_con_variable()
    return query'''
def login():
    query = consulta_sin_variable("SELECT * FROM DOCENTE")
    return query

def allCursos():
    query = consulta_sin_variable("SELECT nom_curso FROM CURSO")
    lis = [i[0] for i in query]
    return lis

def allDocentes():
    query = consulta_sin_variable("SELECT nombre FROM DOCENTE")
    lis = [i[0] for i in query]
    return lis

def num_clases_por_semana(clase):
    query = consulta_con_variable("SELECT fecha FROM horario_clase where cod_clase = (?)", (clase,))
    return len(query)

def num_alum_matriculados(clase):
    am = alumnos_matriculados(clase)
    return len(am)

def getCodClase(cod_horario_clase):
    query = consulta_con_variable("SELECT cs.cod_clase FROM CURSO_SECCION cs, HORARIO_CLASE hc WHERE cs.cod_clase = hc.cod_clase and hc.cod_horario_clase = (?)", (cod_horario_clase,))
    lis = [i[0] for i in query]
    return lis[0]

def alumnos_matriculados(clase):
    query = consulta_con_variable("SELECT cod_alumno FROM matriculado where cod_curso_seccion = (?)", (clase,))
    am = [i[0] for i in query]
    return am

def unirListas(l1,l2):
    l3 = []
    for i in l1:
        l3.add(i)
    for i in l2:
        l3.add(i)
    return l3

def intersectarListas(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            if i == j:
                l3.append(i)
    return l3

def diferenciaListas(l1,l2):
    for i in l2:
        if i in l1:
            l1.remove(i)
    return l1

def setL(lista):
    set = []
    for x in lista:
        if x not in set:
            set.append(x)
    return set

def ordenar_por(mat, para):
    for i in range(0, len(mat) - 1):
        for j in range(i + 1, len(mat)):
            if (mat[i][para] > mat[j][para]):
                aux = mat[i]
                mat[i] = mat[j]
                mat[j] = aux
    return mat

def ordenar_por_inv(mat, para):
    for i in range(0, len(mat) - 1):
        for j in range(i + 1, len(mat)):
            if (mat[i][para] < mat[j][para]):
                aux = mat[i]
                mat[i] = mat[j]
                mat[j] = aux
    return mat

def busquedaPorNombre(clase, bus):
    query = consulta_con_variable("SELECT al.cod_alumno FROM matriculado m, ALUMNO al where m.cod_alumno = al.cod_alumno and cod_curso_seccion = (?) and al.nombre LIKE (?)", (clase, "%"+bus+"%"))
    ae = [i[0] for i in query]
    return ae

def consultaCiclo(clase, dia):
    query = consulta_con_variable("SELECT cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h WHERE a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and h.fecha LIKE (?)", (clase,"%"+dia+"%", ))
    return query

def consultaMensual(clase, mes, dia):
    query = consulta_con_variable("SELECT cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h WHERE a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and DATEPART(month, a.fecha_m)=(?) AND h.fecha LIKE (?)", (clase, mes,"%"+dia+"%",))
    return query

def consultaSemanal(clase, semana, bus):
    query = consulta_con_variable("SELECT a.cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h, ALUMNO al WHERE a.cod_alumno = al.cod_alumno and al.nombre LIKE (?) and a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and DATEPART(week, a.fecha_m)<=(?)",("%"+bus+"%",clase, semana,))
    return query

def consultaClase(clase, semana, dia, bus):
    query = consulta_con_variable("SELECT a.cod_alumno FROM ASISTENCIA a, HORARIO_CLASE h, ALUMNO al WHERE a.cod_alumno = al.cod_alumno and al.nombre LIKE (?) and a.cod_horario_clase = h.cod_horario_clase and h.cod_clase=(?) and DATEPART(week, a.fecha_m)=(?) and h.fecha = (?)",("%" + bus + "%", clase, semana,dia,))
    return query

def getSecciones(cod_curso):
    query = consulta_con_variable("SELECT cs.cod_clase FROM curso_seccion cs, horario_clase hc WHERE cs.cod_clase = hc.cod_clase and cs.cod_curso = (?)", (cod_curso,))
    secciones = [i[0] for i in query]
    return secciones

def getNombres(cod_alumnos):
    names = []
    for i in cod_alumnos:
        query = consulta_con_variable("SELECT nombre FROM ALUMNO WHERE cod_alumno=(?)", (str(i),))
        names.append(query[0][0])
    return names
def obtener_nombre_alumno(cod_alumno):
    name = ""
    query = consulta_con_variable("SELECT nombre FROM ALUMNO WHERE cod_alumno=(?)", (cod_alumno,))
    name = query[0][0]
    return name
def num_asist_por_alumno(cod_alumno,cod_h_c):
    query = consulta_con_variable("SELECT cod_asistencia FROM asistencia where cod_alumno = (?) and cod_horario_clase= (?)", (cod_alumno,cod_h_c,))
    return len(query)
    
def datos_alumno(cod_alumno):
    datos=[]
    query = consulta_con_variable("SELECT * FROM ALUMNO where cod_alumno = (?)", (cod_alumno,))
    nombre = [i[1] for i in query]
    edad = [i[2] for i in query]
    ciclo = [i[3] for i in query]
    espec = [i[4] for i in query]
    datos=[nombre[0],edad[0],ciclo[0],espec[0]]
    return datos

def codigo_horario_clase(cod_docente,cod_clase):
    #cod_hor_clas = []
    query = consulta_con_variable("SELECT * FROM HORARIO_CLASE hc WHERE hc.cod_docente = (?) AND hc.cod_clase=(?)", (cod_docente,cod_clase,))
    '''for i in query:
        dato = str(i[1])+" "+str(i[4])+" "+str(i[2])+"-"+str(i[3])
        cod_hor_clas.append(dato)'''
    return query

def cursos_profesor(cod_docente):
    query = consulta_con_variable("SELECT cod_clase FROM HORARIO_CLASE h, CURSO c WHERE h.cod_docente=(?)", (str(cod_docente),))
    lista = []
    for i in query:
        if i not in lista:
            lista.append(i)
    choices = [i[0] for i in lista]
    return choices

def identificar_alumno(cod_alumno):
    query = consulta_con_variable("SELECT cod_alumno FROM ALUMNO WHERE cod_alumno=(?)", (cod_alumno,))
    return query

def identificar_alumno_apto(curso_seleccionado,codigo_alumno):
    query = consulta_con_variable("SELECT * FROM MATRICULADO WHERE cod_curso_seccion LIKE (?) AND cod_alumno=(?);", (curso_seleccionado+'%',codigo_alumno,))
    return query

def codigo_horario_claseNum(cod_docente,cod_clase):
    query = consulta_con_variable("SELECT * FROM HORARIO_CLASE hc WHERE hc.cod_docente = (?) AND hc.cod_clase=(?)", (cod_docente,cod_clase,))
    return query
def identificar_alumno_marco(codigo_horario_clase,fecha,codigo_alumno):
    query = consulta_con_variable("SELECT cod_alumno FROM ASISTENCIA WHERE cod_horario_clase = (?) AND fecha_m = (?) AND cod_alumno LIKE (?);",(codigo_horario_clase,fecha, codigo_alumno+'%',))
    return query

def insertar_asistencia(codigo_alumno,codigo_horario_clase,hora_actual,fecha_actual):
    query = consulta_con_variable("INSERT INTO ASISTENCIA (cod_alumno, cod_horario_clase, hora_m, fecha_m) VALUES ((?),(?),(?),(?))",(codigo_alumno, codigo_horario_clase, hora_actual, fecha_actual,))
    return 0

def alumno_pertenece_seccion(codigo_alumno,seccion):
    query = consulta_con_variable("SELECT * FROM MATRICULADO WHERE cod_alumno=(?) AND cod_curso_seccion=(?)",(codigo_alumno,seccion,))
    return query

def informacion_periodo():
    query = consulta_sin_variable("SELECT * FROM PERIODO")
    return query

def informacion_periodo_seleccionado(periodo_seleccionado):
    query = consulta_con_variable("SELECT * FROM PERIODO WHERE descripcion=(?)",(periodo_seleccionado,))
    return query

def alumnos_curso_periodo(cod_curso,periodo):
    query = consulta_con_variable("SELECT * FROM ALUMNO al,PERIODO per,Matriculado mat ,  Curso_Seccion cs WHERE al.cod_alumno = mat.cod_alumno AND mat.cod_periodo = per.cod_periodo AND cs.cod_clase = mat.cod_curso_seccion AND cs.cod_curso = (?) AND per.descripcion=(?) ORDER BY al.nombre;",(cod_curso,periodo,))
    return query

def alumnos_clase_periodo(cod_clase,periodo):
    query = consulta_con_variable("SELECT * FROM ALUMNO al, PERIODO per,Matriculado mat  WHERE al.cod_alumno = mat.cod_alumno AND mat.cod_periodo = per.cod_periodo AND mat.cod_curso_seccion = (?) AND per.descripcion=(?) ORDER BY al.nombre;",(cod_clase,periodo,))
    return query

def alumnos_asistencia_clase_periodo(cod_clase,periodo):
    query = consulta_con_variable("SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre;",(cod_clase,periodo,))
    return query

def alumnos_asistencia_clase_periodo_sin_invitado(cod_clase,periodo):
    query = consulta_con_variable("SELECT * FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre) WHERE cod_alumno != (SELECT al.cod_alumno FROM MATRICULADO mat,ASISTENCIA asi,ALUMNO al,PERIODO per WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre);",(cod_clase,periodo,cod_clase,periodo,))
    return query

def alumnos_invitados_clase_periodo(cod_clase,periodo):
    query = consulta_con_variable("SELECT * FROM ALUMNO al,PERIODO per,MATRICULADO mat,ASISTENCIA asi WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre;",(cod_clase,periodo,))
    return query

def cantidad_acumulada_asistencia_semana_alumno (cod_clase,periodo,cod_alumno,semana_seleccionada):
    query = consulta_con_variable("SELECT COUNT(*) FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?)) WHERE cod_alumno=(?) AND (semana <= (?));",(cod_clase,periodo,cod_alumno,semana_seleccionada,))
    valor = query[0][0]
    return valor

def cantidad_veces_clase_maximo_semana(cod_clase):
    query = consulta_con_variable("SELECT COUNT(*) as maximo FROM HORARIO_CLASE WHERE cod_clase=(?);",(cod_clase,))
    valor = query[0][0]
    return valor

def dias_clase(cod_clase):
    query = consulta_con_variable("SELECT * FROM HORARIO_CLASE WHERE cod_clase = (?);",(cod_clase,))
    return query

def alumnos_periodo_semana_dia_clase(cod_clase,periodo,semana_seleccionada,dia_seleccionado):
    query = consulta_con_variable("SELECT * FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre) WHERE cod_alumno != (SELECT al.cod_alumno FROM MATRICULADO mat,ASISTENCIA asi,ALUMNO al,PERIODO per WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre) AND semana =(?) AND fecha=(?);",(cod_clase,periodo,cod_clase,periodo,semana_seleccionada,dia_seleccionado,))
    return query

def alumnos_asistencia_periodo_semana_dia_clase (cod_clase,periodo,semana_seleccionada,dia_seleccionado):
    query = consulta_con_variable("SELECT * FROM (SELECT * FROM ALUMNO al, PERIODO per,Matriculado mat  WHERE al.cod_alumno = mat.cod_alumno AND mat.cod_periodo = per.cod_periodo AND mat.cod_curso_seccion = (?) AND per.descripcion=(?) ORDER BY al.nombre) as pb  WHERE pb.cod_alumno IN (SELECT cod_alumno FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre) WHERE cod_alumno != (SELECT al.cod_alumno FROM MATRICULADO mat,ASISTENCIA asi,ALUMNO al,PERIODO per WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre) AND semana =(?) AND fecha=(?));",(cod_clase,periodo,cod_clase,periodo,cod_clase,periodo,semana_seleccionada,dia_seleccionado,))
    return query

def alumnos_inasistencia_periodo_semana_dia_clase (cod_clase,periodo,semana_seleccionada,dia_seleccionado):
    query = consulta_con_variable("SELECT * FROM (SELECT * FROM ALUMNO al, PERIODO per,Matriculado mat  WHERE al.cod_alumno = mat.cod_alumno AND mat.cod_periodo = per.cod_periodo AND mat.cod_curso_seccion = (?) AND per.descripcion=(?) ORDER BY al.nombre) as pb  WHERE pb.cod_alumno NOT IN (SELECT cod_alumno FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre) WHERE cod_alumno != (SELECT al.cod_alumno FROM MATRICULADO mat,ASISTENCIA asi,ALUMNO al,PERIODO per WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre) AND semana =(?) AND fecha=(?));",(cod_clase,periodo,cod_clase,periodo,cod_clase,periodo,semana_seleccionada,dia_seleccionado,))
    return query

def cantidad_alumnos_asistencia_periodo_semana_dia_clase (cod_clase,periodo,semana_seleccionada,dia_seleccionado):
    query = consulta_con_variable("SELECT COUNT(*) FROM (SELECT * FROM ALUMNO al, PERIODO per,Matriculado mat  WHERE al.cod_alumno = mat.cod_alumno AND mat.cod_periodo = per.cod_periodo AND mat.cod_curso_seccion = (?) AND per.descripcion=(?) ORDER BY al.nombre) as pb  WHERE pb.cod_alumno IN (SELECT cod_alumno FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/7 as INT)+1 as Semana FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) ORDER BY al.nombre) WHERE cod_alumno != (SELECT al.cod_alumno FROM MATRICULADO mat,ASISTENCIA asi,ALUMNO al,PERIODO per WHERE mat.cod_alumno = al.cod_alumno AND al.cod_alumno = asi.cod_alumno AND per.cod_periodo = mat.cod_periodo AND mat.cod_curso_seccion!=(?) AND per.descripcion=(?) ORDER BY al.nombre) AND semana =(?) AND fecha=(?));",(cod_clase,periodo,cod_clase,periodo,cod_clase,periodo,semana_seleccionada,dia_seleccionado,))
    return query

def cantidad_alumnos_matriculados_clase(cod_clase):
    query = consulta_con_variable("SELECT COUNT(*) FROM MATRICULADO WHERE cod_curso_seccion = (?);",(cod_clase,))
    return query

def acumulado_asistencia_alumno(cod_clase,periodo,cod_alumno):
    query = consulta_con_variable("SELECT COUNT(*) FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) AND asi.cod_alumno = (?) ORDER BY al.nombre;",(cod_clase,periodo,cod_alumno,))
    return query

def cantidad_alumnos_asistencia_periodo_mes(cod_clase,periodo,cod_alumno,mes):
    query = consulta_con_variable("SELECT COUNT(*) FROM (SELECT * , CAST((julianday(asi.fecha_m)-julianday(per.fecha_inicio))/30 as INT)+1 as Mes FROM ALUMNO al,PERIODO per ,ASISTENCIA asi , HORARIO_CLASE hc WHERE asi.fecha_m >= per.fecha_inicio AND asi.fecha_m <= per.fecha_fin AND asi.cod_horario_clase = hc.cod_horario_clase AND al.cod_alumno = asi.cod_alumno AND hc.cod_clase = (?) AND per.descripcion = (?) AND al.cod_alumno=(?)) as pb WHERE pb.mes =(?);",(cod_clase,periodo,cod_alumno,mes,))
    return query

def dias_dictados_clase(cod_clase,cod_docente):
    query = consulta_con_variable("SELECT fecha FROM HORARIO_CLASE WHERE cod_clase=(?) and cod_docente=(?);",(cod_clase,cod_docente,))
    return query

def dia_clase_codigo(cod_horario_clase):
    query = consulta_con_variable("SELECT fecha FROM HORARIO_CLASE WHERE cod_horario_clase=(?);",(cod_horario_clase,))
    return query