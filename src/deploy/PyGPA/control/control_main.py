# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
import sys   
from view.view_main import Main_View
from control.control_analisys import Analise_Ctrl
from control.control_generator import Generator_Ctrl
    
class Main_Ctrl:
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.ui = Main_View(self)
        self.ui.showMaximized()
        sys.exit(app.exec_())
        
    def abrir_gerador(self):
        Generator_Ctrl()
    
    def abrir_analisador(self):
        Analise_Ctrl()