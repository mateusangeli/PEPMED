from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon
from componentes.table_consultas import TabelaConsulta
from componentes.table_telaConsultas import tabelaTelaConsultas
from layouts.consulta import novaConsulta
from layouts.info_consulta import InfoConsultas
import models.consulta_models as CoModels
from PyQt5 import uic

TYPE = {'remove': 0, 'info': 1 }

class telaConsultas(QWidget):
    def __init__(self, main):
        super(). __init__()
        uic.loadUi("ui/tela_consultas.ui", self)
        self.table = tabelaTelaConsultas(self.tableWidget, self)
        self.main = main
        self.nova_btn.clicked.connect(self.novaConsulta)


    def novaConsulta(self):
        self.main.display(2)


