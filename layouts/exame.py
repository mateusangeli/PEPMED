from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from classes.exame import Exame
import models.paciente_models as PaModels
from PyQt5.QtCore import QDate


class novoExame(QWidget):
    def __init__(self, parente):
        super().__init__()
        uic.loadUi("ui/exames.ui", self)
        self.marcar_btn.clicked.connect(self.marcarConsulta) 
        self.limpar_btn.clicked.connect(self.limparCampos)
        self.parente = parente
        self.exameAtual = None
        self.lista_pacientes = []
        self.carregaDadosPaciente()
        self.combo_paciente.currentIndexChanged.connect(self.index_changed_paciente)
        self.pacienteAtual = None

    def carregaDadosPaciente(self):
        self.lista_pacientes = PaModels.getPacientes()
        lista_combopac = []
        for p in self.lista_pacientes:
            lista_combopac.append(p.nome)
        self.combo_paciente.addItems(lista_combopac)
    
    def index_changed_paciente(self, i):
        if i == 0:
            self.limparCampos()
        else:
            self.pacienteAtual = self.lista_pacientes[i-1]
            self.cpf.setText(self.pacienteAtual.cpf)
            if self.pacienteAtual.plano == 'Sim':
                self.combo_plano.setCurrentIndex(1)
            else: 
                self.combo_plano.setCurrentIndex(2)

    def marcarConsulta(self):
        procedimento = self.combo_procedimento.currentText()
        data = self.data_exame.dateTime().toString('dd/MM/yyyy hh:mm')
        valor = self.valor.text()
        if ((procedimento != "") and (data != "") and (valor != "") and (self.pacienteAtual != None)):
            newExame = Exame(-1, procedimento, data, valor, self.pacienteAtual)
            self.parente.add(newExame)
            self.parente.carregaDados()
        else:
            self.label_msg.setText("Preencha todos os campos")
        # Pegar todos os dados e salvar no banco de dados, e depois atualizar a tabela

    def limparCampos(self):
        print("Teste")
        self.cpf.setText("")
        self.combo_plano.setCurrentIndex(0)
        self.combo_paciente.setCurrentIndex(0)
        self.combo_procedimento.setCurrentIndex(0)
        self.data_exame.setDate(QDate.currentDate())
        self.valor.setText("")

    def deletar(self):
        self.parente.excluir(self.exameAtual.id)
        self.parente.carregaDados()
