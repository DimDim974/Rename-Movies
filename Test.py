import sys
from tkinter import Widget
from wsgiref.util import application_uri 
from PyQt5.QtWidgets import QApplication, Qwidget
application = application_uri(sys.argv)
widget = Widget()
widget.resize(250, 250)
widget.setWindowTitle("Bonjour tout le monde !") 
widget.show()
application.exec_()