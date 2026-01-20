# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'widgets.ui'
#
# Created: Sun Nov  4 23:42:12 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class DetailWidget(QtWidgets.QWidget):
    def setup(self):
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("self", "self"))
        self.groupBox.setTitle(QtCore.QCoreApplication.translate("self", "Gráfico"))
        self.groupBox_2.setTitle(QtCore.QCoreApplication.translate("self", "Toolbox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = DetailWidget()
    ui.setup()
    ui.show()
    sys.exit(app.exec())

