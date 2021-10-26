'''from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt
from classes.exame import Exame
import models.exame_models as ExModels


class TabelaExame():
    def __init__ (self, tableWidget, janela):
        self.tableWidget = tableWidget
        self.janela = janela
        self.lista_exames = []
        self.carregaDados()
        self.configTable()

    def carregaDados(self):
        self.lista_exames = ExModels.getExames()
        self.tableWidget.setRowCount(0)
        for exames in self.lista_exames:
            self._addRow(exames)

    def _addRow(self, exames):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        id = QTableWidgetItem(str(exames.id))
        id.setTextAlignment(Qt.AlignCenter)
        procedimento = QTableWidgetItem(exames.procedimento)
        paciente = QTableWidgetItem(exames.paciente.nome)
        data = QTableWidgetItem(exames.data)
        data.setTextAlignment(Qt.AlignCenter)
        valor = QTableWidgetItem(exames.valor)
        valor.setTextAlignment(Qt.AlignCenter)


        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, procedimento)
        self.tableWidget.setItem(rowCount, 2, paciente)
        self.tableWidget.setItem(rowCount, 3, data)
        self.tableWidget.setItem(rowCount, 4, valor)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                 QHeaderView.Stretch)
                                                                 
        self.tableWidget.clicked.connect(self.clicado)                                                      

    def clicado(self):
        selected_row = self.tableWidget.currentRow()
        id = self.tableWidget.item(selected_row, 0). text()
        exame = ExModels.getExame(id)

    def add(self, exame):
        ExModels.addExame(exame)
        self.carregaDados()

    def excluir(self, id):
        ExModels.delExame(id)
        self.carregaDados()'''
    


            