from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QListWidgetItem, QWidget, QLabel
from PyQt5 import uic
from componentes.table_pacientes import TabelaPaciente

from layouts.login import cadLogin
from layouts.paciente import cadPaciente



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)


        self.listWidget.setCurrentRow(0)

        self.stackedWidget_geral.setCurrentIndex(0)
        self.log_btn.clicked.connect(self.login)
        self.cad_btn.clicked.connect(self.cadastro)
        self.entrar_btn.clicked.connect(self.iniciarSistema)
        self.janela_cadLogin = cadLogin(self)
        self.carregaJanelas()

    def carregaJanelas(self):
        self.stackedWidget.insertWidget(0, cadPaciente())

    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)
            
    def cadastro(self):
        self.stackedWidget_geral.setCurrentIndex(2)

    def login(self):
        self.stackedWidget_geral.setCurrentIndex(0)

