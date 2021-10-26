from classes.usuario import Usuario
import models.database as db

def getUsuarios():
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Usuarios"""
    lista_usuarios = []
    for u in cursor.fetchall():
        id = u[0]
        nome = u[1]
        usuario = u[2]
        senha = u[3]
        tipousuario = u[4]
        novoUsuario = Usuario(id, nome, usuario, senha, tipousuario)
        lista_usuarios.append(novoUsuario)
    conn.close()
    return lista_usuarios

def getUsuario(usuario, senha):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM Usuarios WHERE usuario = ? AND senha = ?;"""
    cursor.execute(sql, [usuario, senha])
    lista_users = []
    for u in cursor.fetchall():
        id = u[0]
        nome = u[1]
        usuario = u[2]
        senha = u[3]
        tipousuario = u[4]
        new = Usuario(id, nome, usuario, senha, tipousuario)
        lista_users.append(new)
    conn.close()
    return lista_users

def addUsuario(usuario):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Usuarios (nome, usuario, senha, tipousuario) VALUES (?, ?, ?, ?);"""
    cursor.execute(sql,[usuario.nome, usuario.usuario, usuario.senha, usuario.tipousuario])
    conn.commit()
    conn.close()

