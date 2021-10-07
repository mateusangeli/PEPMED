from PyQt5.QtWidgets import QWidget
from classes.usuario import Usuario
import models.usuario_models as UsModels

class cadLogin():
    def __init__(self, janela):
        self.janela = janela
        self.lista_usuarios = []
        self.carregaDados()

        
        self.janela.confirmar_btn.clicked.connect(self.salvarCadastro)


    def carregaDados(self):
        self.lista_usuarios = UsModels.getUsuarios()

    def salvarCadastro(self):
        user = self.verificaCampos()
        if user != None:
            self.add(user)
            self.limpaCampos()
            self.janela.statusBar().showMessage(str("Cadastro feito com sucesso"), 5000)
        else:
            self.janela.statusBar().showMessage(str("Erro ao cadastrar, tente novamente!"), 5000)      
 

    def verificaCampos(self):
        nome = self.janela.nome.text()
        usuario = self.janela.usuario.text()
        senha = self.janela.senha.text()
        tipousuario = self.janela.combo_tipo.currentText()

        if ((nome != "") and (usuario != "") and (senha != "") and (tipousuario != "")):
            return Usuario(-1, nome, usuario, senha, tipousuario)
        return None

    def add(self, usuario):
        UsModels.addUsuario(usuario)
        self.carregaDados()

    def limpaCampos(self):
        self.janela.nome.setText("")
        self.janela.usuario.setText("")
        self.janela.senha.setText("")
