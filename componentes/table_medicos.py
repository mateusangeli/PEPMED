from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt

import models.medico_models as MeModels

class TabelaMedicos():
    def __init__(self, tableWidget, janela):
        self.tableWidget = tableWidget
        self.janela = janela
        self.lista_medicos = []
        self.configTable()
        self.carregaDados()

    def carregaDados(self):
        self.lista_medicos = MeModels.getMedicos()
        self.tableWidget.setRowCount(0)
        for medicos in self.lista_medicos:
            self._addRow(medicos)

    def _addRow(self, medico):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        id = QTableWidgetItem(str(medico.id))
        id.setTextAlignment(Qt.AlignCenter)
        nome = QTableWidgetItem(medico.nome)
        idade = QTableWidgetItem(medico.idade)
        idade.setTextAlignment(Qt.AlignCenter)
        cpf = QTableWidgetItem(medico.cpf)
        cpf.setTextAlignment(Qt.AlignCenter)
        rg = QTableWidgetItem(medico.rg)
        rg.setTextAlignment(Qt.AlignCenter)
        area = QTableWidgetItem(medico.area)
        area.setTextAlignment(Qt.AlignCenter)
        telefone = QTableWidgetItem(medico.telefone)
        telefone.setTextAlignment(Qt.AlignCenter)

        self.tableWidget.setItem(rowCount, 0, id)
        self.tableWidget.setItem(rowCount, 1, nome)
        self.tableWidget.setItem(rowCount, 2, idade)
        self.tableWidget.setItem(rowCount, 3, cpf)
        self.tableWidget.setItem(rowCount, 4, rg)
        self.tableWidget.setItem(rowCount, 5, area)
        self.tableWidget.setItem(rowCount, 6, telefone)

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
        id = self.tableWidget.item(selected_row, 0). text()
        medico = MeModels.getMedico(id)
        self.janela.insereInfo(medico)

    def add(self, medico):
        MeModels.addMedico(medico)
        self.carregaDados()
        self.janela.limpaCampos()

    def atualizar(self, medico):
        MeModels.editMedico(medico)
        self.carregaDados()
        self.janela.limpaCampos()
    
    def excluir(self):
        MeModels.delMedico(self.janela.medicoAtual.id)
        self.carregaDados()
        self.janela.limpaCampos()