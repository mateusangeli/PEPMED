from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        self.stackedWidget_geral.setCurrentIndex(0)
        self.log_btn.clicked.connect(self.login)
        self.cad_btn.clicked.connect(self.cadastro)
        self.entrar_btn.clicked.connect(self.iniciarSistema)

    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)
            
    def cadastro(self):
        self.stackedWidget_geral.setCurrentIndex(2)

    def login(self):
        self.stackedWidget_geral.setCurrentIndex(0)

