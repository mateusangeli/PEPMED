from PyQt5.QtWidgets import QWidget, QWidgetAction
from classes.medico import Medico
import models.medico_models as MeModels
from PyQt5 import uic

class cadMedico(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cadastroM.ui", self)
        self.lista_medicos = []
        self.carregaDados()
        

    def carregaDados(self):
        self.lista_medicos = MeModels.getMedicos()
