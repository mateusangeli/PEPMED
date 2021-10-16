from classes.consulta import Consulta
import models.paciente_models as PaModels
import models.medico_models as MeModels
import models.database as db

def getConsultas():
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Consulta"""
    cursor.execute(sql)
    lista_consultas = []
    for c in cursor.fetchall():
        id = c[0]
        tipo = c[1]
        data = c[2]
        obs = c[3]
        valor = c[4]
        id_paciente = c[5]
        id_medico = c[6]
        paciente = PaModels.getPaciente(id_paciente)
        medico = MeModels.getMedico(id_medico)
        novaConsulta = Consulta(id, tipo, data, obs, valor, paciente, medico)
        lista_consultas.append(novaConsulta)
    conn.close()
    return lista_consultas

def getConsulta(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * from Consulta WHERE id = ?;"""
    cursor.execute(sql, [id])
    c = cursor.fetchall()[0]
    id = c[0]
    tipo = c[1]
    data = c[2]
    obs = c[3]
    valor = c[4]
    id_paciente = c[5]
    id_medico = c[6]
    paciente = PaModels.getPaciente(id_paciente)
    medico = MeModels.getMedico(id_medico)
    novaConsulta = Consulta(id, tipo, data, obs, valor, paciente, medico)
    conn.close()
    return novaConsulta

def editConsulta(consulta):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE Consulta SET tipo = ?, data = ?, obs = ?, valor = ? WHERE id = ?"""
    cursor.execute(sql, [consulta.tipo, consulta.data, consulta.obs, consulta.valor, consulta.id])
    conn.commit()
    conn.close()

def addConsulta(consulta):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Consulta (tipo, data, obs, valor, id_paciente, id_medico) VALUES (?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [consulta.tipo, consulta.data, consulta.obs, consulta.valor, consulta.paciente.id, consulta.medico.id])
    conn.commit()
    conn.close()

def delConsulta(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM Consulta WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()
