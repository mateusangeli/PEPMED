from PyQt5.QtWidgets import QWidget
from classes.paciente import Paciente
from componentes.table_pacientes import TabelaPaciente
import models.paciente_models as PaModels
from PyQt5 import uic

class cadPaciente(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cadastroC.ui", self)
        self.lista_pacientes = []
        self.carregaDados()
        self.table = TabelaPaciente(self.tableWidget, self)


        self.salvar_btn.clicked.connect(self.salvarPaciente)

    def carregaDados(self):
        self.lista_pacientes = PaModels.getPacientes()

    def salvarPaciente(self):
        paciente = self.verificaCampos()
        if paciente != None:
            self.add(paciente)
            self.limpaCampos()

            

    def verificaCampos(self):
        nome = self.nome.text()
        sexo = self.combo_sexo.currentText()
        idade = self.idade.text()
        cpf = self.cpf.text()
        rg = self.rg.text()
        telefone = self.fone.text()
        plano = self.combo_plano.currentText()


        if ((nome != "") and (sexo != "") and (idade != "") and (cpf != "") and (rg != "") and (telefone != "") and (plano != "")):
            return Paciente(-1, nome, sexo, idade, cpf, rg, telefone, plano)
        return None
        

    def add(self, paciente):
        PaModels.addPaciente(paciente)
        self.carregaDados()

    def limpaCampos(self):
        self.nome.setText("")
        self.idade.setText("")
        self.cpf.setText("")
        self.rg.setText("")
        self.fone.setText("")


