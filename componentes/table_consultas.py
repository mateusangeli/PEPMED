from classes.consulta import Consulta
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt

import models.consulta_models as CoModels

class TabelaConsulta():
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
        area = QTableWidgetItem(consulta.medico.area)
        area.setTextAlignment(Qt.AlignCenter)

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, paciente)
        self.tableWidget.setItem(rowCount, 2, medico)
        self.tableWidget.setItem(rowCount, 3, area)
        self.tableWidget.setItem(rowCount, 4, data)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.clicked.connect(self.clicado)

    def clicado(self):
        selected_row = self.tableWidget.currentRow()
        id = self.tableWidget.item(selected_row, 0). text()
        consulta = CoModels.getConsulta(id)
        self.janela.insereInfo(consulta)

    def add(self, consulta):
        CoModels.addConsulta(consulta)
        self.carregaDados()

    def atualizar(self, consulta):
        CoModels.editConsulta(consulta)
        self.carregaDados()      


