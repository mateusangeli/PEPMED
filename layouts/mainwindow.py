from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QListWidgetItem, QWidget, QLabel
from PyQt5 import uic

from layouts.login import cadLogin

class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent = None):
        super(CustomQWidget, self).__init__(parent)

        label_icon = QLabel(icon)
        label_text = QLabel(text)
        layout = QHBoxLayout()
        layout.addWidget(label_icon)
        layout.addWidget(label_text)
        layout.addWidget(label_icon)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainwindow.ui", self)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("*", "Pacientes")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(0, item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("@", "Médicos")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1, item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("$", "Financeiro")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(2, item)
        self.listWidget.setItemWidget(item, item_widget)

        self.listWidget.setCurrentRow(0)

        self.stackedWidget_geral.setCurrentIndex(0)
        self.log_btn.clicked.connect(self.login)
        self.cad_btn.clicked.connect(self.cadastro)
        self.entrar_btn.clicked.connect(self.iniciarSistema)
        self.janela_cadLogin = cadLogin(self)

    def iniciarSistema(self):
        self.stackedWidget_geral.setCurrentIndex(1)
            
    def cadastro(self):
        self.stackedWidget_geral.setCurrentIndex(2)

    def login(self):
        self.stackedWidget_geral.setCurrentIndex(0)

