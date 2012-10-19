# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/julio/Documents/TFG/insecao.ui'
#
# Created: Wed Sep 26 09:10:00 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class cria_campos_UI(object):
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bt_novo = QtGui.QPushButton(self.centralwidget)
        self.bt_novo.setObjectName(_fromUtf8("bt_novo"))
        self.verticalLayout.addWidget(self.bt_novo)
        self.bt_remove = QtGui.QPushButton(self.centralwidget)
        self.bt_remove.setObjectName(_fromUtf8("bt_remove"))
        self.verticalLayout.addWidget(self.bt_remove)
        self.bt_limpa = QtGui.QPushButton(self.centralwidget)
        self.bt_limpa.setObjectName(_fromUtf8("bt_limpa"))
        self.verticalLayout.addWidget(self.bt_limpa)
        self.bt_editar = QtGui.QPushButton(self.centralwidget)
        self.bt_editar.setObjectName(_fromUtf8("bt_editar"))
        self.verticalLayout.addWidget(self.bt_editar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout.addWidget(self.listWidget)
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
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAnalisar = QtGui.QAction(MainWindow)
        self.actionAnalisar.setObjectName(_fromUtf8("actionAnalisar"))
        self.menu_Ferramentas.addAction(self.actionAnalisar)
        self.actionCombinar = QtGui.QAction(MainWindow)
        self.actionCombinar.setObjectName(_fromUtf8("actionCombinar"))
        self.menu_Ferramentas.addAction(self.actionCombinar)
        self.menubar.addAction(self.menu_Ferramentas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.bt_novo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ctrl.gerar_novo_campo)
        QtCore.QObject.connect(self.bt_remove, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ctrl.remove_item)
        QtCore.QObject.connect(self.bt_limpa, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ctrl.limpa_lista)
        QtCore.QObject.connect(self.bt_editar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ctrl.atualizar_campo)
        QtCore.QObject.connect(self.actionAnalisar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ctrl.analisar)
        QtCore.QObject.connect(self.actionCombinar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.ctrl.combina_campos)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA-2.0 - Campos", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_novo.setText(QtGui.QApplication.translate("MainWindow", "Novo Campo", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_remove.setText(QtGui.QApplication.translate("MainWindow", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_limpa.setText(QtGui.QApplication.translate("MainWindow", "Limpar Lista", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Ferramentas.setTitle(QtGui.QApplication.translate("MainWindow", "&Ferramentas", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalisar.setText(QtGui.QApplication.translate("MainWindow", "Analisar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCombinar.setText(QtGui.QApplication.translate("MainWindow", "Combinar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = cria_campos_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

