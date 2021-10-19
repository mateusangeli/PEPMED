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

class MeuBotao(QWidget):
    def __init__(self, consulta, parent, type):
        super(MeuBotao, self).__init__()
        self.consulta = consulta
        self.parent = parent

        self.w = None
        self.btn = QPushButton(self)
        self.btn.setText("")
        
        if type == TYPE['remove']:
            self.typeDelete()
        else:
            self.typeInfo()

        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeInfo(self):
        self.btn.setIcon(QIcon("icons/info.png"))
        self.btn.clicked.connect(self.maisInfo)
        self.btn.setToolTip("Mais informações sobre a venda")
        self.btn.setIconSize(QSize(20,20))

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/delete.png"))
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Excluir venda")
        self.btn.setIconSize(QSize(20,20))

    def remover(self):
        pass

    def maisInfo(self):
        self.w = InfoConsultas(self.consulta)
        self.w.show()
