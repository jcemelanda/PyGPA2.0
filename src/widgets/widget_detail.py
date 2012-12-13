# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'widgets.ui'
#
# Created: Sun Nov  4 23:42:12 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Detail_widget(QtGui.QWidget):
    def setup(self):
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_1 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_1.setObjectName(_fromUtf8("gridLayout_1"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("self", "self", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("self", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("self", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    self = QtGui.QWidget()
    ui = Detail_widget()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())

