# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created: Thu Dec  6 21:35:31 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Start_Window:
    def setup(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.botao_editar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_editar.setObjectName(_fromUtf8("botao_editar"))
        self.gridLayout.addWidget(self.botao_editar, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.botao_novo_campo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_novo_campo.setObjectName(_fromUtf8("botao_novo_campo"))
        self.gridLayout.addWidget(self.botao_novo_campo, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PyGPA 2.0"))
        self.botao_editar.setText(QtWidgets.QApplication.translate("MainWindow", "Gerar Conjunto"))
        self.botao_novo_campo.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir Analisador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Start_Window()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())

