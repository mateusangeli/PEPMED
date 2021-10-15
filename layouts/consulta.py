from PyQt5.QtWidgets import QWidget
from classes.consulta import Consulta
from classes.medico import Medico
from classes.paciente import Paciente
from componentes.table_medicos import TabelaMedicos
import models.medico_models as MeModels
import models.paciente_models as PaModels
from PyQt5 import uic

class novaConsulta(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/consulta.ui", self)
        self.lista_medicos = []
        self.lista_pacientes = []
        self.medicoAtual = None
        self.pacienteAtual = None
        self.carregaDadosMedico()
        self.carregaDadosPaciente()
        self.combo_paciente.currentIndexChanged.connect(self.index_changed_paciente)
        self.combo_medico.currentIndexChanged.connect(self.index_changed_medico)

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
