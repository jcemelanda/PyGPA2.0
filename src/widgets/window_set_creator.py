# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/julio/Documents/TFG/gerador.ui'
#
# Created: Tue Sep 25 20:26:31 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Set_Creator_Window:
        
    def setup(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lb_num = QtWidgets.QLabel(self.groupBox)
        self.lb_num.setObjectName(_fromUtf8("lb_num"))

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_num)
        self.num_mat = QtWidgets.QLineEdit(self.groupBox)
        self.num_mat.setInputMask(_fromUtf8(""))
        self.num_mat.setObjectName(_fromUtf8("num_mat"))

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_mat)
        self.lb_x_ini = QtWidgets.QLabel(self.groupBox)
        self.lb_x_ini.setObjectName(_fromUtf8("lb_x_ini"))
        self.lb_x_ini.setVisible(False)
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lb_x_ini)
        self.ini_x = QtWidgets.QLineEdit(self.groupBox)
        self.ini_x.setObjectName(_fromUtf8("ini_x"))
        self.ini_x.setVisible(False)
        
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ini_x)
        self.lb_y_ini = QtWidgets.QLabel(self.groupBox)
        self.lb_y_ini.setObjectName(_fromUtf8("lb_y_ini"))
        self.lb_y_ini.setVisible(False)
        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lb_y_ini)
        self.ini_y = QtWidgets.QLineEdit(self.groupBox)
        self.ini_y.setObjectName(_fromUtf8("ini_y"))
        self.ini_y.setVisible(False)
        
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ini_y)
        self.lb_const_1 = QtWidgets.QLabel(self.groupBox)
        self.lb_const_1.setObjectName(_fromUtf8("lb_const_1"))
        self.lb_const_1.setVisible(False)
        
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lb_const_1)
        self.lb_const_2 = QtWidgets.QLabel(self.groupBox)
        self.lb_const_2.setObjectName(_fromUtf8("lb_const_2"))
        self.lb_const_2.setVisible(False)
        
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lb_const_2)
        self.const_1 = QtWidgets.QLineEdit(self.groupBox)
        self.const_1.setFrame(True)
        self.const_1.setObjectName(_fromUtf8("const_1"))
        self.const_1.setVisible(False)
        
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.const_1)
        self.const_2 = QtWidgets.QLineEdit(self.groupBox)
        self.const_2.setObjectName(_fromUtf8("const_2"))
        self.const_2.setVisible(False)
        
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.const_2)
        self.lb_alt = QtWidgets.QLabel(self.groupBox)
        self.lb_alt.setObjectName(_fromUtf8("lb_alt"))
        
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_alt)
        self.altura = QtWidgets.QLineEdit(self.groupBox)
        self.altura.setObjectName(_fromUtf8("altura"))
        
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.altura)
        self.lb_larg = QtWidgets.QLabel(self.groupBox)
        self.lb_larg.setObjectName(_fromUtf8("lb_larg"))
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lb_larg)
        self.largura = QtWidgets.QLineEdit(self.groupBox)
        self.largura.setObjectName(_fromUtf8("largura"))
        
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.largura)
        self.bt_gerar = QtWidgets.QPushButton(self.groupBox)
        self.bt_gerar.setObjectName(_fromUtf8("bt_gerar"))
        
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.bt_gerar)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PyGPA-2.0 - Editor"))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Parâmetros"))
        self.lb_num.setText(QtWidgets.QApplication.translate("MainWindow", "Número de Matrizes:"))
        self.lb_x_ini.setText(QtWidgets.QApplication.translate("MainWindow", "Ponto inicial em X:"))
        self.lb_y_ini.setText(QtWidgets.QApplication.translate("MainWindow", "Ponto inicial em Y:"))
        self.lb_const_1.setText(QtWidgets.QApplication.translate("MainWindow", "Constante 1:"))
        self.lb_const_2.setText(QtWidgets.QApplication.translate("MainWindow", "Constante 2:"))
        self.lb_alt.setText(QtWidgets.QApplication.translate("MainWindow", "Altura"))
        self.lb_larg.setText(QtWidgets.QApplication.translate("MainWindow", "Largura"))
        self.bt_gerar.setText(QtWidgets.QApplication.translate("MainWindow", "Gerar Matrizes"))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Aleatório"))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Constante"))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Doublet"))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Fonte / Sumidouro"))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Turbilhão"))
        
    

