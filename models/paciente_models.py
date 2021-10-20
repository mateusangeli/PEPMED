from sqlite3.dbapi2 import Error
from classes.paciente import Paciente
import models.database as db
import sqlite3

def getPacientes():
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * From Paciente"""
    cursor.execute(sql)
    lista_pacientes = []
    for p in cursor.fetchall():
        id = p[0]
        nome = p[1]
        sexo = p[2]
        idade = p[3]
        cpf = p[4]
        rg = p[5]
        telefone = p[6]
        plano = p[7]
        novoPaciente = Paciente(id, nome, sexo, idade, cpf, rg, telefone, plano)
        lista_pacientes.append(novoPaciente)
    conn.close()
    return lista_pacientes

def getPaciente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Paciente WHERE id = ?;"""
    cursor.execute(sql, [id])
    z = cursor.fetchall()[0]
    id = z[0]
    nome = z[1]
    sexo = z[2]
    idade = z[3]
    cpf = z[4]
    rg = z[5]
    telefone = z[6]
    plano = z[7]
    novoPaciente = Paciente(id, nome, sexo, idade, cpf, rg, telefone, plano)
    conn.close()
    return novoPaciente

def editPaciente(paciente):
    try: 
        conn = db.connect_db()
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        sql = """ UPDATE Paciente SET nome = ?, sexo = ?, idade = ?, cpf = ?, rg = ?, telefone = ?, plano = ? WHERE id = ?"""
        cursor.execute(sql, [paciente.nome, paciente.sexo, paciente.idade, paciente.cpf, paciente.rg, paciente.telefone, paciente.plano, paciente.id])
    except sqlite3.Error as er:
        print(er)
    conn.commit()
    conn.close()


def addPaciente(paciente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Paciente (nome, sexo, idade, cpf, rg, telefone, plano) VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [paciente.nome, paciente.sexo, paciente.idade, paciente.cpf, paciente.rg, paciente.telefone, paciente.plano])
    conn.commit()
    conn.close()

def delPaciente(id):
    try:
        conn = db.connect_db()
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        sql = """DELETE FROM Paciente WHERE id = ?"""
        cursor.execute(sql, [id])
    except sqlite3.Error as er:
        print(er)
    conn.commit()
    conn.close()
