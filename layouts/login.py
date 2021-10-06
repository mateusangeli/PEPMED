from PyQt5.QtWidgets import QWidget
import utils.tipousuario
from classes.usuario import Usuario
import models.usuario_models as UsModels

class cadLogin():
    def __init__(self, janela):
        self.janela = janela
        self.lista_usuarios = []
        self.carregaDados(self)


    def carregaDados(self):
        self.lista_usuarios = UsModels.getUsuarios()
    
    def index_changed_tipo(self):
        self.combo_tipo.addItem("Secretária")
        self.combo_tipo.addItem("Médico")
        self.combo_tipo.addItem("Administrador")

    def verificaCampos(self):
        nome = self.janela.nome.text()
        usuario = self.janela.usuario.text()
        senha = self.janela.senha.text()

