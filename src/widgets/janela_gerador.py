# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents/TFG/insecao.ui'
#
# Created: Fri Dec  7 20:18:25 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class GeneratorWindow:
    def setup(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setMargin(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_novo_campo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_novo_campo.setObjectName("botao_novo_campo")
        self.horizontalLayout.addWidget(self.botao_novo_campo)
        self.botao_editar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_editar.setObjectName("botao_editar")
        self.horizontalLayout.addWidget(self.botao_editar)
        self.botao_limpar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_limpar.setObjectName("botao_limpar")
        self.horizontalLayout.addWidget(self.botao_limpar)
        self.botao_remove = QtWidgets.QPushButton(self.centralwidget)
        self.botao_remove.setObjectName("botao_remove")
        self.horizontalLayout.addWidget(self.botao_remove)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botao_combinar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_combinar.setObjectName("botao_combinar")
        self.horizontalLayout_2.addWidget(self.botao_combinar)
        self.botao_analisar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_analisar.setObjectName("botao_analisar")
        self.horizontalLayout_2.addWidget(self.botao_analisar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "MainWindow"))
        self.botao_editar.setText(QtCore.QCoreApplication.translate("MainWindow", "Editar"))
        self.botao_limpar.setText(QtCore.QCoreApplication.translate("MainWindow", "Limpar Lista"))
        self.botao_remove.setText(QtCore.QCoreApplication.translate("MainWindow", "Remover"))
        self.botao_novo_campo.setText(QtCore.QCoreApplication.translate("MainWindow", "Novo Campo"))
        self.botao_combinar.setText(QtCore.QCoreApplication.translate("MainWindow", "Combinar Campos"))
        self.botao_analisar.setText(QtCore.QCoreApplication.translate("MainWindow", "Analisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeneratorWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

