from classes.paciente import Paciente
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import Qt

import models.paciente_models as PaModels

class TabelaPaciente():
    def __init__(self, tableWidget, janela):
        self.tableWidget = tableWidget
        self.janela = janela
        self.lista_pacientes = []
        self.configTable()
        self.carregaDados()

    def carregaDados(self):
        self.lista_pacientes = PaModels.getPacientes()
        self.tableWidget.setRowCount(0)
        for pacientes in self.lista_pacientes:
            self._addRow(pacientes)
            
    def _addRow(self, paciente):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        nome = QTableWidgetItem(paciente.nome)
        idade = QTableWidgetItem(paciente.idade)
        idade.setTextAlignment(Qt.AlignCenter)
        telefone = QTableWidgetItem(paciente.telefone)
        telefone.setTextAlignment(Qt.AlignCenter)

        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, idade)
        self.setItem(rowCount, 3, telefone)


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)

