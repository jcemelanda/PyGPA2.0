# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficos.ui'
#
# Created: Sun Nov  4 20:43:31 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Grafics_widget(QtWidgets.QWidget):
    def setup(self):
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("self", "Form"))
        self.groupBox.setTitle(QtCore.QCoreApplication.translate("self", "Campo Vetorial"))
        self.groupBox_2.setTitle(QtCore.QCoreApplication.translate("self", "Triangulação"))
        self.groupBox_3.setTitle(QtCore.QCoreApplication.translate("self", "GPA"))
        self.label.setText(QtCore.QCoreApplication.translate("self", "0.788"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    g = Grafics_widget()
    g.setup()
    g.show()
    sys.exit(app.exec())

