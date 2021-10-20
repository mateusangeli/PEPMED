from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtCore import QDateTime
import models.consulta_models as CoModels
import models.medico_models as MeModels
import models.paciente_models as PaModels

class InfoConsultas(QWidget):
    def __init__(self, consulta):
        super().__init__()
        uic.loadUi("ui/info_consultas.ui", self)
        self.lista_consultas = []
        self.lista_medicos = []
        self.lista_pacientes = []
        self.insereInfo(consulta)

    
    def carregaDadosConsultas(self):
        self.lista_consultas = CoModels.getConsultas()

    def carregaDadosMedicos(self):
        self.lista_medicos = MeModels.getMedicos()

    def carregaDadosPacientes(self):
        self.lista_pacientes = PaModels.getPacientes

    def insereInfo(self, consulta):
        self.nome.setText(consulta.paciente.nome)
        self.cpf.setText(consulta.paciente.cpf)
        self.rg.setText(consulta.paciente.rg)
        self.idade.setText(str(consulta.paciente.idade))
        self.telefone.setText(consulta.paciente.telefone)
        if consulta.tipo == '1° Consulta':
            self.combo_tipo.setCurrentIndex(0)
        else:
            self.combo_tipo.setCurrentIndex(1)
        self.obs.append(consulta.obs)
        data = QDateTime.fromString(consulta.data, 'dd/MM/yyyy hh:mm')
        self.data_consulta.setDateTime(data)
        self.valor.setText(consulta.valor)
        if consulta.paciente.sexo == 'Masculino':
            self.combo_sexo.setCurrentIndex(0)
        else:
            self.combo_sexo.setCurrentIndex(1)
        
        if consulta.paciente.plano == 'Sim':
            self.combo_plano.setCurrentIndex(0)
        else:
            self.combo_plano.setCurrentIndex(1)


