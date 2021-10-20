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
        self.carregaDadosConsulta()
        self.salvar_consulta.clicked.connect(self.salvarConsulta)       
        self.combo_paciente.currentIndexChanged.connect(self.index_changed_paciente)
        self.combo_medico.currentIndexChanged.connect(self.index_changed_medico)
        self.combo_consulta.currentIndexChanged.connect(self.valorTotal)
        self.cancel_btn.clicked.connect(self.excluir)
        self.valorTotal(0)
        self.combo_paciente.setCurrentIndex(1)
        self.combo_medico.setCurrentIndex(1)

    def carregaDadosConsulta(self):
        self.lista_consultas = CoModels.getConsultas()

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
        self.medicoAtual = self.lista_medicos[i]
        self.id_medico.setText(str(self.medicoAtual.id))
        self.fone_medico.setText(self.medicoAtual.telefone)
        self.area_medico.setText(self.medicoAtual.area)

    def index_changed_paciente(self, i):
        self.pacienteAtual = self.lista_pacientes[i]
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
                self.limpaCampos()
            else:
                consulta.id = self.consultaAtual.id
                self.table.atualizar(consulta)
                self.limpaCampos()


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
            self.valor.setText("R$ 100,00")
        else:
            self.valor.setText("R$ 80,00")
    


    def insereInfo(self, consulta):
        self.consultaAtual = consulta 
        self.combo_medico.setEnabled(False)
        self.id_medico.setEnabled(False)
        self.fone_medico.setEnabled(False)
        self.area_medico.setEnabled(False)
        self.combo_paciente.setEnabled(False)
        self.id_paciente.setEnabled(False)
        self.idade_paciente.setEnabled(False)
        self.fone_paciente.setEnabled(False)
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
            self.combo_consulta.setCurrentIndex(0)
        else:
            self.combo_consulta.setCurrentIndex(1)
        self.obs.setText(consulta.obs)
        data = QDateTime.fromString(consulta.data, 'dd/MM/yyyy hh:mm')
        self.data_consulta.setDateTime(data)

        self.salvar_consulta.setText("Atualizar consulta")
        self.cancel_btn.setEnabled(True)


    def excluir(self):
        CoModels.delConsulta(self.consultaAtual.id)
        self.carregaDadosConsulta()

    def limpaCampos(self):
        self.consultaAtual = None
        self.data_consulta.setDate(QDate.currentDate())
        self.obs.clear()
        self.valor.setText("")
        self.salvar_consulta.setText("Salvar consulta")
        self.cancel_btn.setEnabled(False)


        
