# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtWidgets
from widgets.janela_criador_conjunto import SetCreatorWindow

 
class SetCreatorView(QtWidgets.QMainWindow):
    def __init__(self, controle):
        self.funcoes = {
                        0:self.set_aleatorio,
                        1:self.set_constante,
                        2:self.set_doublet,
                        3:self.set_fonte,
                        4:self.set_turbilhao}
        
        super().__init__()
        self.controle = controle
        self.ui = SetCreatorWindow()
        self.ui.setup(self)
        
        self.ui.comboBox.currentIndexChanged.connect(self.selecionado)
        self.ui.bt_gerar.clicked.connect(self.gerar_matrizes)
        self._indice_selecionado = 0
        
    def selecionado(self, i):
        self._indice_selecionado = i
        self.zerar_campos()
        self.funcoes[i]()
        
    def inicia_campos(self, campo):
        self.ui.comboBox.setCurrentIndex(campo.type)
        self.ui.num_mat.setText(str(campo.num_mat))
        self.ui.altura.setText(str(campo.altura))
        self.ui.largura.setText(str(campo.largura))
        try:
            self.ui.const_1.setText(str(campo.const_1))
        except Exception as e:
            print(e)
        try:
            self.ui.const_2.setText(str(campo.const_2))
        except Exception as e:
            print(e)
        try:
            self.ui.ini_x.setText(str(campo.inicio.real))
        except Exception as e:
            print(e)
        try:
            self.ui.ini_y.setText(str(campo.inicio.imag))
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
        
        self.ui.lb_const_1.setText('Constante')
        self.ui.lb_const_2.setText('Ângulo')
    
    def set_fonte(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(True)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(True)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText('Magnitude')
        self.ui.lb_const_2.setText('Velocidade (a+bj)')
        
    def set_doublet(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(True)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(True)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText('Magnitude (complexo a+bj)')
        self.ui.lb_const_2.setText('Velocidade (a+bj)')
        
    def set_turbilhao(self):
        self.ui.lb_const_1.setVisible(True)
        self.ui.lb_const_2.setVisible(True)
        self.ui.lb_x_ini.setVisible(True)
        self.ui.lb_y_ini.setVisible(True)
        
        self.ui.const_1.setVisible(True)
        self.ui.const_2.setVisible(True)
        self.ui.ini_x.setVisible(True)
        self.ui.ini_y.setVisible(True)
        
        self.ui.lb_const_1.setText('Circulação')
        self.ui.lb_const_2.setText('Velocidade (a+bj)')
        
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

    @property
    def indice_selecionado(self):
        return self._indice_selecionado
    
    @property
    def largura(self):
        return self.ui.largura.text()
    
    @property
    def altura(self):
        return self.ui.altura.text()
    
    @property
    def const_1(self):
        return self.ui.const_1.text()
    
    @property
    def const_2(self):
        return self.ui.const_2.text()
    
    @property
    def ini_x(self):
        return self.ui.ini_x.text()

    @property
    def ini_y(self):
        return self.ui.ini_y.text()
    
    @property
    def num_mat(self):
        return self.ui.num_mat.text()
