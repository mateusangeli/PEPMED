from PyQt5.QtWidgets import QWidget
from classes.consulta import Consulta
from componentes.table_consultas import TabelaConsulta
import models.medico_models as MeModels
import models.paciente_models as PaModels
import models.consulta_models as CoModels
from PyQt5 import uic
from PyQt5.QtCore import QDate

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
        if (consulta != None) and (self.consultaAtual == None):            
            self.table.add(consulta)
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
        if consulta.tipo == '1° Consulta':
            self.combo_consulta.setCurrentIndex(0)
        else:
            self.combo_consulta.setCurrentIndex(1)
        self.obs.append(consulta.obs)

        self.salvar_consulta.setText("Atualizar consulta")
        self.excluir_btn.setEnabled(True)


    def excluir(self):
        CoModels.delConsulta(self.consultaAtual.id)
        self.carregaDadosConsulta()

    def limpaCampos(self):
        self.consultaAtual = None
        self.data_consulta.setDate(QDate.currentDate())
        self.obs.setText("")
        self.valor.setText("")
        self.salvar_consulta.setText("Salvar consulta")
        self.excluir_btn.setEnabled(False)


        

