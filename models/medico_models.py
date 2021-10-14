from classes.medico import Medico
import models.database as db

def getMedicos():
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Medicos"""
    cursor.execute(sql)
    lista_medicos = []
    for m in cursor.fetchall():
        id = m[0]
        nome = m[1]
        idade = m[2]
        cpf = m[3]
        rg = m[4]
        area = m[5]
        telefone = m[6]
        novoMedico = Medico(id, nome, idade, cpf, rg, area, telefone)
        lista_medicos.append(novoMedico)
    conn.close()
    return lista_medicos

def getMedico(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * From Medicos WHERE id = ?;"""
    cursor.execute(sql, [id])
    m = cursor.fetchall()[0]
    id = m[0]
    nome = m[1]
    idade = m[2]
    cpf = m[3]
    rg = m[4]
    area = m[5]
    telefone = m[6]
    novoMedico = Medico(id, nome, idade, cpf, rg, area, telefone)
    conn.close()
    return novoMedico

def addMedico(medico):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Medicos (nome, idade, cpf, rg, area, telefone) VALUES (?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [medico.nome, medico.idade, medico.cpf, medico.rg, medico.area, medico.telefone])
    conn.commit()
    conn.close()    

def editMedico(medico):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE Medicos SET nome = ?, idade = ?, cpf = ?, rg = ?, area = ?, telefone = ? WHERE id = ?"""
    cursor.execute(sql, [medico.nome, medico.idade, medico.cpf, medico.rg, medico.area, medico.telefone, medico.id])
    conn.commit()
    conn.close()

def delMedico(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """DELETE FROM Medicos WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()