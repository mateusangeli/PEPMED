from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QListWidgetItem, QWidget, QLabel
from PyQt5 import uic
from componentes.table_pacientes import TabelaPaciente
from layouts.consulta import novaConsulta
from layouts.exame import novoExame

from layouts.login import cadLogin
from layouts.paciente import cadPaciente
from layouts.medico import cadMedico
from layouts.consulta import novaConsulta
from layouts.tela_consultas import telaConsultas
from layouts.exame import novoExame
from layouts.tela_exames import telaExames
import models.usuario_models as UsModels



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        self.listWidget.setCurrentRow(0)
        self.stackedWidget_geral.setCurrentIndex(0)
        self.listWidget.setCurrentRow(0)
        self.listWidget.currentRowChanged.connect(self.display)
        self.log_btn.clicked.connect(self.login)
        self.cad_btn.clicked.connect(self.cadastro)
        self.entrar_btn.clicked.connect(self.verificaSenha)
        self.lista_users = []
        self.janela_cadLogin = cadLogin(self)
        self.carregaJanelas()

    def carregaJanelas(self):
        self.stackedWidget.insertWidget(0, cadPaciente())
        self.stackedWidget.insertWidget(1, cadMedico())
        self.stackedWidget.insertWidget(2, novaConsulta())
        self.stackedWidget.insertWidget(3, telaConsultas(self))
        self.stackedWidget.insertWidget(4, telaExames())


    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)
        self.carregaJanelas()
            
    def cadastro(self):
        self.stackedWidget_geral.setCurrentIndex(2)

    def login(self):
        self.stackedWidget_geral.setCurrentIndex(0)

    def display(self, index):
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)

    def verificaSenha(self):
        login_user = self.login_user.text()
        senha_user = self.senha_user.text()
        self.lista_users = UsModels.getUsuario(login_user, senha_user)
        if len(self.lista_users) > 0:
            self.iniciarSistema()
        else:
            self.statusBar().showMessage(str("Usuário ou senha incorreto, tente novamente!"), 5000)


