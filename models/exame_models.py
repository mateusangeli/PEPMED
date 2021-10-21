from classes.exame import Exame
import models.database as db
import models.paciente_models as PaModels


def getExames():
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Exames"""
    cursor.execute(sql)
    lista_exames = []
    for e in cursor.fetchall():
        id = e[0]
        procedimento = e[1]
        data = e[2]
        valor = e[3]
        id_paciente = e[4]
        paciente = PaModels.getPaciente(id_paciente)
        novoExame = Exame(id, procedimento, data, valor, paciente)
        lista_exames.append(novoExame)
    conn.close()
    return lista_exames

def getExame(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Exame WHERE id = ?;"""
    cursor.execute(sql, [id])
    e = cursor.fetchall()[0]
    id = e[0]
    procedimento = e[1]
    data = e[2]
    valor = e[3]
    id_paciente = e[4]
    paciente = PaModels.getPaciente(id_paciente)
    novoExame = Exame(id, procedimento, data, valor, paciente)
    conn.close()
    return novoExame

def editExame(exame):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE Exame SET procedimento = ?, data = ?, valor = ? WHERE id = ?"""
    cursor.execute(sql, [exame.procedimento, exame.data, exame.valor, exame.id])
    conn.commit()
    conn.close()

def addExame(exame):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Exame (procedimento, data, valor, id_paciente) VALUES (?, ?, ?, ?);"""
    cursor.execute(sql, [exame.procedimento, exame.data, exame.valor, exame.paciente.id])
    conn.commit()
    conn.close()

def delExame(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM Exame WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()