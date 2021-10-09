from classes.paciente import Paciente
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

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
        id = QTableWidgetItem(str(paciente.id))
        id.setTextAlignment(Qt.AlignCenter)
        nome = QTableWidgetItem(paciente.nome)
        idade = QTableWidgetItem(str(paciente.idade))
        idade.setTextAlignment(Qt.AlignCenter)
        telefone = QTableWidgetItem(paciente.telefone)
        telefone.setTextAlignment(Qt.AlignCenter)
        cpf = QTableWidgetItem(paciente.cpf)
        cpf.setTextAlignment(Qt.AlignCenter)
        rg = QTableWidgetItem(paciente.rg)
        rg.setTextAlignment(Qt.AlignCenter)
        sexo = QTableWidgetItem(paciente.sexo)
        sexo.setTextAlignment(Qt.AlignCenter)
        plano = QTableWidgetItem(paciente.plano)
        plano.setTextAlignment(Qt.AlignCenter)

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, nome)
        self.tableWidget.setItem(rowCount, 2, idade)
        self.tableWidget.setItem(rowCount, 3, telefone)
        self.tableWidget.setItem(rowCount, 4, cpf)
        self.tableWidget.setItem(rowCount, 5, rg)
        self.tableWidget.setItem(rowCount, 6, sexo)
        self.tableWidget.setItem(rowCount, 7, plano)


    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)
        self.tableWidget.clicked.connect(self.clicado)

    def clicado(self):
        selected_row = self.tableWidget.currentRow()    
        id = self.tableWidget.item(selected_row, 0).text()
        paciente = PaModels.getPaciente(id)
        self.janela.insereInfo(paciente)

    def atualizar(self, paciente):
        PaModels.editPaciente(paciente)
        self.carregaDados()

    def excluir(self, paciente):
        PaModels.delPaciente(paciente.id)
        self.carregaDados()                                                          

                                                      

