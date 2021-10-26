from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from componentes.table_consultas import TabelaConsulta
from componentes.table_exames import TabelaExame
import models.exame_models as ExModels
import models.paciente_models as PaModels
from PyQt5.QtCore import QDate, QDateTime, Qt
from classes.exame import Exame

class novoExame(QWidget):
    def __init__(self, exame):
        super().__init__()
        uic.loadUi("ui/exames.ui", self)
        self.lista_pacientes = []
        self.carregaDadosPaciente()
        self.combo_paciente.currentIndexChanged.connect(self.index_changed_paciente)


    def carregaDadosPaciente(self):
        self.lista_pacientes = PaModels.getPacientes()
        lista_combopac = []
        for p in self.lista_pacientes:
            lista_combopac.append(p.nome)
        self.combo_paciente.addItems(lista_combopac)

    def index_changed_paciente(self, i):
        if i == 0:
            self.limpaCamposPaciente()
        else:
            self.pacienteAtual = self.lista_pacientes[i-1]
            self.id_paciente.setText(str(self.pacienteAtual.id))
            self.cpf.setText(self.pacienteAtual.cpf)
            self.rg.setText(self.pacienteAtual.rg)
            self.fone.setText(self.pacienteAtual.telefone)
            if self.pacienteAtual.sexo == 'Masculino':
                self.combo_sexo.setCurrentIndex(0)
            else:
                self.combo_sexo.setCurrentIndex(1)
            self.idade.setText(str(self.pacienteAtual.idade))
            if self.pacienteAtual.plano == 'Sim':
                self.combo_plano.setCurrentIndex(1)
            else: 
                self.combo_plano.setCurrentIndex(2)
    
    def salvarExame(self):
        exame = self.verificaCampos()
        if exame != None:
            if self.exameAtual == None:
                self.table.add(exame)
                self.limpaCamposPaciente()
                self.limparCamposExame()
    
    def verificaCampos(self):
        procedimento = self.combo_procedimento.currentText()
        data = self.data_exame.dateTime().toString('dd/MM/yyyy hh:mm')
        valor = self.valor.text()

        if ((procedimento != "") and (data != "") and (valor != "") and (self.pacienteAtual != None)):
            return Exame(-1, procedimento, data, valor, self.pacienteAtual)
        return None
    
    def valorTotal(self, plano):
        if  plano == 1:
            self.valor.setText("Pago pelo plano")
        else:
            self.valor.setText("R$ 50,00")

    '''def excluir(self):
        self.table.'''
        
            
        

    def limpaCamposPaciente(self):
        self.id_paciente.setText("")
        self.cpf.setText("")
        self.rg.setText("")
        self.fone.setText("")
        self.combo_sexo.setCurrentIndex(0)
        self.idade.setText("")
        self.combo_plano.setCurrentIndex(0)

    def limparCamposExame(self):
        self.data_consulta.setDate(QDate.currentDate)
        self.objetivo.setText("")
        self.combo_procedimento.setCurrentIndex(0)
