# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/julio/Documents/TFG/main.ui'
#
# Created: Wed Sep 26 08:41:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Main_UI(object):
    def __init__(self, controle):
        self.controle = controle
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Ferramentas = QtGui.QMenu(self.menubar)
        self.menu_Ferramentas.setObjectName(_fromUtf8("menu_Ferramentas"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAn_lise_GPA = QtGui.QAction(MainWindow)
        self.actionAn_lise_GPA.setObjectName(_fromUtf8("actionAn_lise_GPA"))
        self.actionCria_o_de_Campos_Artificiais = QtGui.QAction(MainWindow)
        self.actionCria_o_de_Campos_Artificiais.setObjectName(_fromUtf8("actionCria_o_de_Campos_Artificiais"))
        self.menu_Ferramentas.addAction(self.actionAn_lise_GPA)
        self.menu_Ferramentas.addAction(self.actionCria_o_de_Campos_Artificiais)
        self.menubar.addAction(self.menu_Ferramentas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionAn_lise_GPA, QtCore.SIGNAL(_fromUtf8("triggered()")), self.controle.abrir_analise)
        QtCore.QObject.connect(self.actionCria_o_de_Campos_Artificiais, QtCore.SIGNAL(_fromUtf8("triggered()")), self.controle.abrir_compositor)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA-2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Ferramentas.setTitle(QtGui.QApplication.translate("MainWindow", "&Ferramentas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAn_lise_GPA.setText(QtGui.QApplication.translate("MainWindow", "Análise &GPA", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCria_o_de_Campos_Artificiais.setText(QtGui.QApplication.translate("MainWindow", "Criação de &Campos Artificiais", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Main_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

