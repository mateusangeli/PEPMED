from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import models.consulta_models as CoModels
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from layouts.info_consulta import InfoConsultas

TYPE = {'remove': 0, 'info': 1 }

class tabelaTelaConsultas():
    def __init__ (self, tableWidget, janela):
        self.tableWidget = tableWidget
        self.janela = janela
        self.lista_consultas = []
        self.carregaDados()
        self.configTable()

    def carregaDados(self):
        self.lista_consultas = CoModels.getConsultas()
        self.tableWidget.setRowCount(0)
        for consultas in self.lista_consultas:
            self._addRow(consultas)

    def _addRow(self, consulta):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        id = QTableWidgetItem(str(consulta.id))
        id.setTextAlignment(Qt.AlignCenter)
        paciente = QTableWidgetItem(consulta.paciente.nome)
        medico = QTableWidgetItem(consulta.medico.nome)
        data = QTableWidgetItem(consulta.data)
        data.setTextAlignment(Qt.AlignCenter)
        valor = QTableWidgetItem(consulta.valor)
        valor.setTextAlignment(Qt.AlignCenter)

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, paciente)
        self.tableWidget.setItem(rowCount, 2, medico)
        self.tableWidget.setItem(rowCount, 3, data)
        self.tableWidget.setItem(rowCount, 4, valor)
        self.tableWidget.setCellWidget(rowCount, 5, MeuBotao(consulta, self, TYPE['info']))

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                 QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch) 


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

