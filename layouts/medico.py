from PyQt5.QtWidgets import QWidget, QWidgetAction
from classes.medico import Medico
from componentes.table_medicos import TabelaMedicos
import models.medico_models as MeModels
from PyQt5 import uic

class cadMedico(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cadastroM.ui", self)
        self.lista_medicos = []
        self.medicoAtual = None
        self.carregaDados()
        self.table = TabelaMedicos(self.tableWidget, self)

        self.salvar_btn.clicked.connect(self.salvarMedico)
        self.excluir_btn.clicked.connect(self.table.excluir)
        

    def carregaDados(self):
        self.lista_medicos = MeModels.getMedicos()

    def salvarMedico(self):
        medico = self.verificaCampos()
        if (medico != None) and (self.medicoAtual == None):
            self.table.add(medico)
            self.limpaCampos()
        else:
            medico.id = self.medicoAtual.id
            self.table.atualizar(medico)
            self.limpaCampos()

    def verificaCampos(self):
        nome = self.nome.text()
        idade = self.idade.text()
        cpf = self.cpf.text()
        rg = self.rg.text()
        area = self.area.text()
        telefone = self.telefone.text()

        if ((nome != "") and (idade != "") and (cpf != "") and (rg != "") and (area != "") and (telefone != "")):
            return Medico(-1, nome, idade, cpf, rg, area, telefone)
        return None

    def insereInfo(self, medico):
        self.medicoAtual = medico
        self.nome.setText(medico.nome)
        self.idade.setText(medico.idade)
        self.cpf.setText(medico.cpf)
        self.rg.setText(medico.rg)
        self.area.setText(medico.area)
        self.telefone.setText(medico.telefone)

        self.salvar_btn.setText("Atualizar")
        self.excluir_btn.setEnabled(True)

    def limpaCampos(self):
        self.medicoAtual = None
        self.nome.setText("")
        self.idade.setText("")
        self.cpf.setText("")
        self.rg.setText("")
        self.area.setText("")
        self.telefone.setText("")
        self.salvar_btn.setText("Salvar")
        self.excluir_btn.setEnabled(False)
