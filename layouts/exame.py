from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class novoExame(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/exames.ui", self)