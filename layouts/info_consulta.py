from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize, QRect

class InfoConsultas(QWidget):
    def __init__(self, consulta):
        super().__init__()
        uic.loadUi("ui/info_consultas.ui", self)