# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/TFG/insecao.ui'
#
# Created: Fri Dec  7 20:18:25 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Generator_Window:
    def setup(self, MainWindow):
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.botao_editar = QtGui.QPushButton(self.centralwidget)
        self.botao_editar.setObjectName(_fromUtf8("botao_editar"))
        self.horizontalLayout.addWidget(self.botao_editar)
        self.botao_limpar = QtGui.QPushButton(self.centralwidget)
        self.botao_limpar.setObjectName(_fromUtf8("botao_limpar"))
        self.horizontalLayout.addWidget(self.botao_limpar)
        self.botao_remove = QtGui.QPushButton(self.centralwidget)
        self.botao_remove.setObjectName(_fromUtf8("botao_remove"))
        self.horizontalLayout.addWidget(self.botao_remove)
        self.botao_novo_campo = QtGui.QPushButton(self.centralwidget)
        self.botao_novo_campo.setObjectName(_fromUtf8("botao_novo_campo"))
        self.horizontalLayout.addWidget(self.botao_novo_campo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.botao_combinar = QtGui.QPushButton(self.centralwidget)
        self.botao_combinar.setObjectName(_fromUtf8("botao_combinar"))
        self.horizontalLayout_2.addWidget(self.botao_combinar)
        self.botao_analisar = QtGui.QPushButton(self.centralwidget)
        self.botao_analisar.setObjectName(_fromUtf8("botao_analisar"))
        self.horizontalLayout_2.addWidget(self.botao_analisar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_editar.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_limpar.setText(QtGui.QApplication.translate("MainWindow", "Limpar Lista", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_remove.setText(QtGui.QApplication.translate("MainWindow", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_novo_campo.setText(QtGui.QApplication.translate("MainWindow", "Novo Campo", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_combinar.setText(QtGui.QApplication.translate("MainWindow", "Combinar Campos", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_analisar.setText(QtGui.QApplication.translate("MainWindow", "Analisar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Generator_Window()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

