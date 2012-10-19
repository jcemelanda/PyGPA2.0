from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ui_sobre(object):
    def setup_ui(self, Sobre, pix, text):
        Sobre.setObjectName(_fromUtf8("Sobre"))
        Sobre.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Sobre)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.GPALabel = QtGui.QLabel(Sobre)
        self.GPALabel.setText(_fromUtf8(""))
        self.GPALabel.setObjectName(_fromUtf8("GPALabel"))
        self.GPALabel.setPixmap(pix)
        self.gridLayout.addWidget(self.GPALabel, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Sobre)
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setText(_fromUtf8(text))
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Sobre)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslate_ui(Sobre)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Sobre.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Sobre.reject)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslate_ui(self, Sobre):
        Sobre.setWindowTitle(QtGui.QApplication.translate("Sobre", "Sobre", None, QtGui.QApplication.UnicodeUTF8))


