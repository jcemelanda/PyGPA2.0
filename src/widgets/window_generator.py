# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/TFG/insecao.ui'
#
# Created: Fri Dec  7 20:18:25 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Generator_Window:
    def setup(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setMargin(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.botao_novo_campo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_novo_campo.setObjectName(_fromUtf8("botao_novo_campo"))
        self.horizontalLayout.addWidget(self.botao_novo_campo)
        self.botao_editar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_editar.setObjectName(_fromUtf8("botao_editar"))
        self.horizontalLayout.addWidget(self.botao_editar)
        self.botao_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_limpar.setObjectName(_fromUtf8("botao_limpar"))
        self.horizontalLayout.addWidget(self.botao_limpar)
        self.botao_remove = QtWidgets.QPushButton(self.centralwidget)
        self.botao_remove.setObjectName(_fromUtf8("botao_remove"))
        self.horizontalLayout.addWidget(self.botao_remove)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.botao_combinar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_combinar.setObjectName(_fromUtf8("botao_combinar"))
        self.horizontalLayout_2.addWidget(self.botao_combinar)
        self.botao_analisar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_analisar.setObjectName(_fromUtf8("botao_analisar"))
        self.horizontalLayout_2.addWidget(self.botao_analisar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow"))
        self.botao_editar.setText(QtWidgets.QApplication.translate("MainWindow", "Editar"))
        self.botao_limpar.setText(QtWidgets.QApplication.translate("MainWindow", "Limpar Lista"))
        self.botao_remove.setText(QtWidgets.QApplication.translate("MainWindow", "Remover"))
        self.botao_novo_campo.setText(QtWidgets.QApplication.translate("MainWindow", "Novo Campo"))
        self.botao_combinar.setText(QtWidgets.QApplication.translate("MainWindow", "Combinar Campos"))
        self.botao_analisar.setText(QtWidgets.QApplication.translate("MainWindow", "Analisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtGui.QWindow()
    ui = Generator_Window()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

