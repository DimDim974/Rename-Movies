import sys 
from PyQt5.QtWidgets import QApplication, Qwidget
application = Qapplication(sys.argv)
widget = QWidget() widget.resize(250, 250)
widget.setWindowTitle("Bonjour tout le monde !") 
widget.show()
application.exec_()