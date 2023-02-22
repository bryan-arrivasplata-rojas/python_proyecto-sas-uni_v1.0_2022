import pyodbc,sqlite3
#BD = "Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-K8AQG7F;Database=ASISTENCIA_DB2;Trusted_connection=yes;"
BD = "DataBase/QuerySQL/ASISTENCIA_DB2.db"
def consulta_sin_variable(string):
    #conn = pyodbc.connect(BD)
    conn = sqlite3.connect(BD)
    cur = conn.cursor()
    cur.execute(string)
    c = cur.fetchall()
    conn.commit()
    conn.close()
    return c

def consulta_con_variable(string, tupla):
    #conn = pyodbc.connect(BD)
    conn = sqlite3.connect(BD)
    cur = conn.cursor()
    cur.execute(string, tupla)
    c = cur.fetchall()
    conn.commit()
    conn.close()
    return c
