# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/julio/Documents/TFG/gerador.ui'
#
# Created: Tue Sep 25 20:26:31 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Set_Creator_Window:
        
    def setup(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setMargin(20)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lb_num = QtGui.QLabel(self.groupBox)
        self.lb_num.setObjectName(_fromUtf8("lb_num"))

        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lb_num)
        self.num_mat = QtGui.QLineEdit(self.groupBox)
        self.num_mat.setInputMask(_fromUtf8(""))
        self.num_mat.setObjectName(_fromUtf8("num_mat"))

        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.num_mat)
        self.lb_x_ini = QtGui.QLabel(self.groupBox)
        self.lb_x_ini.setObjectName(_fromUtf8("lb_x_ini"))
        self.lb_x_ini.setVisible(False)
        
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lb_x_ini)
        self.ini_x = QtGui.QLineEdit(self.groupBox)
        self.ini_x.setObjectName(_fromUtf8("ini_x"))
        self.ini_x.setVisible(False)
        
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.ini_x)
        self.lb_y_ini = QtGui.QLabel(self.groupBox)
        self.lb_y_ini.setObjectName(_fromUtf8("lb_y_ini"))
        self.lb_y_ini.setVisible(False)
        
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lb_y_ini)
        self.ini_y = QtGui.QLineEdit(self.groupBox)
        self.ini_y.setObjectName(_fromUtf8("ini_y"))
        self.ini_y.setVisible(False)
        
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.ini_y)
        self.lb_const_1 = QtGui.QLabel(self.groupBox)
        self.lb_const_1.setObjectName(_fromUtf8("lb_const_1"))
        self.lb_const_1.setVisible(False)
        
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.lb_const_1)
        self.lb_const_2 = QtGui.QLabel(self.groupBox)
        self.lb_const_2.setObjectName(_fromUtf8("lb_const_2"))
        self.lb_const_2.setVisible(False)
        
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.lb_const_2)
        self.const_1 = QtGui.QLineEdit(self.groupBox)
        self.const_1.setFrame(True)
        self.const_1.setObjectName(_fromUtf8("const_1"))
        self.const_1.setVisible(False)
        
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.const_1)
        self.const_2 = QtGui.QLineEdit(self.groupBox)
        self.const_2.setObjectName(_fromUtf8("const_2"))
        self.const_2.setVisible(False)
        
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.const_2)
        self.lb_alt = QtGui.QLabel(self.groupBox)
        self.lb_alt.setObjectName(_fromUtf8("lb_alt"))
        
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lb_alt)
        self.altura = QtGui.QLineEdit(self.groupBox)
        self.altura.setObjectName(_fromUtf8("altura"))
        
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.altura)
        self.lb_larg = QtGui.QLabel(self.groupBox)
        self.lb_larg.setObjectName(_fromUtf8("lb_larg"))
        
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lb_larg)
        self.largura = QtGui.QLineEdit(self.groupBox)
        self.largura.setObjectName(_fromUtf8("largura"))
        
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.largura)
        self.bt_gerar = QtGui.QPushButton(self.groupBox)
        self.bt_gerar.setObjectName(_fromUtf8("bt_gerar"))
        
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.bt_gerar)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.lb_num.setBuddy(self.num_mat)
        self.lb_x_ini.setBuddy(self.ini_x)
        self.lb_y_ini.setBuddy(self.ini_y)
        self.lb_const_1.setBuddy(self.const_1)
        self.lb_const_2.setBuddy(self.const_2)
        self.lb_alt.setBuddy(self.altura)
        self.lb_larg.setBuddy(self.largura)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.num_mat)
        MainWindow.setTabOrder(self.num_mat, self.altura)
        MainWindow.setTabOrder(self.altura, self.largura)
        MainWindow.setTabOrder(self.largura, self.ini_x)
        MainWindow.setTabOrder(self.ini_x, self.ini_y)
        MainWindow.setTabOrder(self.ini_y, self.const_1)
        MainWindow.setTabOrder(self.const_1, self.const_2)
        MainWindow.setTabOrder(self.const_2, self.bt_gerar)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA-2.0 - Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Parâmetros", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_num.setText(QtGui.QApplication.translate("MainWindow", "Número de Matrizes:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_x_ini.setText(QtGui.QApplication.translate("MainWindow", "Ponto inicial em X:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_y_ini.setText(QtGui.QApplication.translate("MainWindow", "Ponto inicial em Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_const_1.setText(QtGui.QApplication.translate("MainWindow", "Constante 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_const_2.setText(QtGui.QApplication.translate("MainWindow", "Constante 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_alt.setText(QtGui.QApplication.translate("MainWindow", "Altura", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_larg.setText(QtGui.QApplication.translate("MainWindow", "Largura", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_gerar.setText(QtGui.QApplication.translate("MainWindow", "Gerar Matrizes", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Aleatório", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Constante", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Doublet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Fonte / Sumidouro", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Turbilhão", None, QtGui.QApplication.UnicodeUTF8))
        
    

