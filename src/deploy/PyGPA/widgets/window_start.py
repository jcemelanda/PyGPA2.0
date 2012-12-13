# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created: Thu Dec  6 21:35:31 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Start_Window:
    def setup(self, MainWindow):
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(54, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.botao_editar = QtGui.QPushButton(self.centralwidget)
        self.botao_editar.setObjectName(_fromUtf8("botao_editar"))
        self.gridLayout.addWidget(self.botao_editar, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(53, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.botao_novo_campo = QtGui.QPushButton(self.centralwidget)
        self.botao_novo_campo.setObjectName(_fromUtf8("botao_novo_campo"))
        self.gridLayout.addWidget(self.botao_novo_campo, 1, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(54, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setFrameShape(QtGui.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA 2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_editar.setText(QtGui.QApplication.translate("MainWindow", "Gerar Conjunto", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_novo_campo.setText(QtGui.QApplication.translate("MainWindow", "Abrir Analisador", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Start_Window()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())

