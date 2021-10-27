from os import truncate
from PyQt5.QtWidgets import QWidget
from classes.consulta import Consulta
from componentes.table_consultas import TabelaConsulta
import models.medico_models as MeModels
import models.paciente_models as PaModels
import models.consulta_models as CoModels
from PyQt5 import uic
from PyQt5.QtCore import QDate, QDateTime, Qt



class novaConsulta(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/consulta.ui", self)
        self.table = TabelaConsulta(self.tableWidget, self)
        self.lista_medicos = []
        self.lista_pacientes = []
        self.lista_consultas = []
        self.medicoAtual = None
        self.pacienteAtual = None
        self.consultaAtual = None
        self.carregaDadosMedico()
        self.carregaDadosPaciente()
        self.salvar_consulta.clicked.connect(self.salvarConsulta)       
        self.combo_paciente.currentIndexChanged.connect(self.index_changed_paciente)
        self.combo_medico.currentIndexChanged.connect(self.index_changed_medico)
        self.combo_consulta.currentIndexChanged.connect(self.valorTotal)
        self.limpar_btn.clicked.connect(self.limparTodosCampos)
        self.cancel_btn.clicked.connect(self.excluir)
        self.valorTotal(0)
        self.combo_paciente.setCurrentIndex(0)
        self.combo_medico.setCurrentIndex(0)
        self.limpar_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)

    def carregaDadosMedico(self):
        self.lista_medicos = MeModels.getMedicos()
        lista_combomed = []
        for m in self.lista_medicos:
            lista_combomed.append(m.nome)
        self.combo_medico.addItems(lista_combomed)

    def carregaDadosPaciente(self):
        self.lista_pacientes = PaModels.getPacientes()
        lista_combopac = []
        for p in self.lista_pacientes:
            lista_combopac.append(p.nome)
        self.combo_paciente.addItems(lista_combopac)

    def index_changed_medico(self, i):
        if i == 0:
            self.limpaCamposMedico()
        else:
            self.medicoAtual = self.lista_medicos[i-1]
            self.id_medico.setText(str(self.medicoAtual.id))
            self.fone_medico.setText(self.medicoAtual.telefone)
            self.area_medico.setText(self.medicoAtual.area)

    def index_changed_paciente(self, i):
        if i == 0:
            self.limpaCamposPaciente()
        else:
            self.pacienteAtual = self.lista_pacientes[i-1]
            self.id_paciente.setText(str(self.pacienteAtual.id))
            self.fone_paciente.setText(self.pacienteAtual.telefone)
            self.idade_paciente.setText(str(self.pacienteAtual.idade))
            if self.pacienteAtual.plano == 'Sim':
                self.combo_plano.setCurrentIndex(0)
            else:
                self.combo_plano.setCurrentIndex(1)

    def salvarConsulta(self):
        consulta = self.verificaCampos()
        if consulta != None:
            if self.consultaAtual == None:            
                self.table.add(consulta)
                self.limparTodosCampos()
            else:
                consulta.id = self.consultaAtual.id
                self.table.atualizar(consulta)
                self.limparTodosCampos()


    def verificaCampos(self):
        tipo = self.combo_consulta.currentText()
        data = self.data_consulta.dateTime().toString('dd/MM/yyyy hh:mm')
        obs = self.obs.toPlainText()
        valor = self.valor.text()        

        
        if ((tipo != "") and (data != "") and (obs != "") and (valor != "") and (self.pacienteAtual != None) and (self.medicoAtual != None)):
            return Consulta(-1, tipo, data, obs, valor, self.pacienteAtual, self.medicoAtual)
        return None

    def valorTotal(self, tipo):
        if tipo == 0:
            self.limparCamposConsulta()    
        if tipo == 1:
            self.valor.setText("R$ 100,00")
        if tipo == 2:
            self.valor.setText("R$ 80,00")
    


    def insereInfo(self, consulta):
        self.consultaAtual = consulta 
        self.combo_medico.setEnabled(False)
        self.combo_paciente.setEnabled(False)
        self.combo_plano.setEnabled(False)
        for m in self.lista_medicos:
            if consulta.medico.id == m.id:
                index = self.combo_medico.findText(m.nome, Qt.MatchFixedString)
                if index >= 0:
                    self.combo_medico.setCurrentIndex(index)
                self.id_medico.setText(str(m.id))    
                self.fone_medico.setText(m.telefone)
                self.area_medico.setText(m.area)
        for p in self.lista_pacientes:
            if consulta.paciente.id == p.id:
                index = self.combo_paciente.findText(p.nome, Qt.MatchFixedString)
                if index >= 0:
                    self.combo_paciente.setCurrentIndex(index)
                self.id_paciente.setText(str(p.id))
                self.fone_paciente.setText(p.telefone)
                self.idade_paciente.setText(str(p.idade))
                if consulta.paciente.plano == 'Sim':
                    self.combo_plano.setCurrentIndex(0)
                else:
                    self.combo_plano.setCurrentIndex(1)

        if consulta.tipo == '1° Consulta':
            self.combo_consulta.setCurrentIndex(1)
        else:
            self.combo_consulta.setCurrentIndex(2)
        self.obs.setText(consulta.obs)
        data = QDateTime.fromString(consulta.data, 'dd/MM/yyyy hh:mm')
        self.data_consulta.setDateTime(data)

        self.salvar_consulta.setText("Atualizar consulta")
        self.limpar_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)


    def excluir(self):
        self.table.excluir(self.consultaAtual.id)
        self.limparTodosCampos()
        


    def limpaCampos(self):
        self.consultaAtual = None
        self.data_consulta.setDateTime(QDateTime.currentDateTime())
        self.obs.clear()
        self.valor.setText("")
        self.salvar_consulta.setText("Salvar consulta")
        self.cancel_btn.setEnabled(False)

    def limpaCamposPaciente(self):
        self.combo_paciente.setCurrentIndex(0)
        self.id_paciente.setText("")
        self.fone_paciente.setText("")
        self.idade_paciente.setText("")

    def limpaCamposMedico(self):
        self.combo_medico.setCurrentIndex(0)
        self.id_medico.setText("")
        self.fone_medico.setText("")
        self.area_medico.setText("")

    def limparCamposConsulta(self):
        self.combo_consulta.setCurrentIndex(0)
        self.data_consulta.setDateTime(QDateTime.currentDateTime())
        self.obs.clear()
        self.valor.setText("")

    def limparTodosCampos(self):
        self.limparCamposConsulta()
        self.limpaCamposMedico()
        self.limpaCamposPaciente()
        self.limpaCampos()
        self.combo_paciente.setEnabled(True)
        self.combo_medico.setEnabled(True)
        self.combo_plano.setEnabled(True)
        self.limpar_btn.setEnabled(False)

        

