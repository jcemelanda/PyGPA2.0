# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from widgets.window_set_creator import Set_Creator_Window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Set_Creator_View(QtWidgets.QMainWindow):
    def __init__(self, controle):
        self.funcoes = {
                        0:self.set_aleatorio,
                        1:self.set_constante,
                        2:self.set_doublet,
                        3:self.set_fonte,
                        4:self.set_turbilhao}
        
        super().__init__()
        self.controle = controle
        self.ui = Set_Creator_Window()
        self.ui.setup(self)
        
        self.ui.comboBox.currentIndexChanged.connect(self.selecionado)
        self.ui.bt_gerar.clicked.connect(self.gerar_matrizes)
        self.indice_selecionado = 0
        
    def selecionado(self, i):
        self.indice_selecionado = i
        self.zerar_campos()
        self.funcoes[i]()
        
    def inicia_campos(self, campo):
        self.ui.comboBox.setCurrentIndex(campo.get_type())
        self.ui.num_mat.setText(str(campo.get_num_mat()))
        self.ui.altura.setText(str(campo.get_altura()))
        self.ui.largura.setText(str(campo.get_largura()))
        try:
            self.ui.const_1.setText(str(campo.get_const_1()))
        except Exception as e:
            print(e)
        try:
            self.ui.const_2.setText(str(campo.get_const_2()))
        except Exception as e:
            print(e)
        try:
            self.ui.ini_x.setText(str(campo.get_inicio().real))
        except Exception as e:
            print(e)
        try:
            self.ui.ini_y.setText(str(campo.get_inicio().imag))
        except Exception as e:
            print(e)
        
    def set_aleatorio(self):
        self.ui.lb_const_1.setVisible(False)
        self.ui.lb_const_2.setVisible(False)
        self.ui.lb_x_ini.setVisible(False)
        self.ui.lb_y_ini.setVisible(False)
        
        self.ui.const_1.setVisible(False)
        self.ui.const_2.setVisible(False)
        self.ui.ini_x.setVisible(False)
        self.ui.ini_y.setVisible(False)
    
    def set_constante(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(True)
        self.ui.lb_x_ini.setVisible(False)
        self.ui.lb_y_ini.setVisible(False)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(True)
        self.ui.ini_x.setVisible(False)
        self.ui.ini_y.setVisible(False)
        
        self.ui.lb_const_1.setText(_fromUtf8('Constante'))
        self.ui.lb_const_2.setText(_fromUtf8('Ângulo'))
    
    def set_fonte(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(False)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(False)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText(_fromUtf8('Magnitude'))
        
    def set_doublet(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(False)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(False)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText(_fromUtf8('Magnitude (complexo a+bj)'))
        
    def set_turbilhao(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(True)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(True)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText(_fromUtf8('Magnitude'))
        self.ui.lb_const_2.setText(_fromUtf8('Posição (complexo a+bj)'))
        
    def gerar_matrizes(self):
        self.controle.gerar_matrizes()
        
    def zerar_campos(self):
        self.ui.num_mat.setText('')
        self.ui.altura.setText('')
        self.ui.largura.setText('')
        self.ui.ini_x.setText('')
        self.ui.ini_y.setText('')
        self.ui.const_1.setText('')
        self.ui.const_2.setText('')

    def get_indice_selecionado(self):
        return self.indice_selecionado
    
    def get_largura(self):
        return self.ui.largura.text()
    
    def get_altura(self):
        return self.ui.altura.text()
    
    def get_const_1(self):
        return self.ui.const_1.text()
    
    def get_const_2(self):
        return self.ui.const_2.text()
    
    def get_ini_x(self):
        return self.ui.ini_x.text()

    def get_ini_y(self):
        return self.ui.ini_y.text()
    
    def get_num_mat(self):
        return self.ui.num_mat.text()
