import sys
from PyQt5.QtWidgets import QApplication
from layouts.mainwindow import MainWindow
from qt_material import apply_stylesheet
       
        
        
    

app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_cyan.xml')
window = MainWindow()
window.show()
app.exec()

    
