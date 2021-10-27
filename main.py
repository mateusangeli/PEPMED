import sys
from PyQt5.QtWidgets import QApplication
from layouts.mainwindow import MainWindow
from qt_material import apply_stylesheet
from PyQt5.QtGui import QIcon
        
        
        
    

app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_cyan.xml')
app.setWindowIcon(QIcon("icons/pepmed.png"))
window = MainWindow()
window.show()
app.exec()

    
