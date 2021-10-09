from PyQt5.QtWidgets import QWidget
from classes.paciente import Paciente
from componentes.table_pacientes import TabelaPaciente
import models.paciente_models as PaModels
from PyQt5 import uic

TYPE = {'info': 0}

class cadPaciente(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cadastroC.ui", self)
        self.lista_pacientes = []
        self.carregaDados()
        self.pacienteAtual = None
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

    def insereInfo(self, paciente):
        self.pacienteAtual = paciente
        self.nome.setText(paciente.nome)
        if paciente.sexo == 'Masculino':
            self.combo_sexo.setCurrentIndex(0)
        else:
            self.combo_sexo.setCurrentIndex(1)
        self.idade.setText(str(paciente.idade))
        self.cpf.setText(paciente.cpf)
        self.rg.setText(paciente.rg)
        self.fone.setText(paciente.telefone)
        if paciente.plano == "Sim":
            self.combo_plano.setCurrentIndex(0)
        else:
            self.combo_plano.setCurrentIndex(1)


        self.salvar_btn.setText("Atualizar")
        

    def add(self, paciente):
        PaModels.addPaciente(paciente)
        self.carregaDados()


    def limpaCampos(self):
        self.nome.setText("")
        self.idade.setText("")
        self.cpf.setText("")
        self.rg.setText("")
        self.fone.setText("")



