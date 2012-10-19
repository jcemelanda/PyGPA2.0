# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from ui.view_gerador import Main_UI
from utils.Gerador import Gerador
import sys
from modelos.campos import campo_turbilhao, campo_fonte, campo_aleatorio,\
    campo_constante, campo_doublet

class controle_mat:
    def __init__(self, controle_pai, campo=None):
        
        self.funcoes = {
                        0:self.gera_aleatorio,
                        1:self.gera_constante,
                        2:self.gera_doublet,
                        3:self.gera_fonte,
                        4:self.gera_turbilhao
                        }
        self.mw = QtGui.QMainWindow()
        self.ui = Main_UI(self)
        self.ui.setupUi(self.mw)
        self.controle_pai = controle_pai
        if campo != None:
            self.inicia_campos(campo)
            
    def inicia_campos(self, campo):
        self.ui.comboBox.setCurrentIndex(campo.get_type())
        self.ui.num_mat.setText(str(campo.get_num_mat()))
        self.ui.altura.setText(str(campo.get_altura()))
        self.ui.largura.setText(str(campo.get_largura()))
        try:
            self.ui.const_1.setText(str(campo.get_const_1()))
            self.ui.ini_x.setText(str(campo.get_inicio().real))
            self.ui.ini_y.setText(str(campo.get_inicio().imag))
            self.ui.const_2.setText(str(campo.get_const_2()))
        except:
            pass        
        
                
    def gerar_matrizes(self):
        self.controle_pai.recebe_campo(self.funcoes[self.ui.comboBox.currentIndex()]())
        
    def gera_aleatorio(self):
        n = eval(str(self.ui.num_mat.text()))
        altura = eval(str(self.ui.altura.text()))
        largura = eval(str(self.ui.largura.text()))
        
        mat = Gerador.aleatorio(n, altura, largura)
        
        return campo_aleatorio(n, altura, largura, mat[:])
    
    def gera_constante(self):
        n = eval(str(self.ui.num_mat.text()))
        altura = eval(str(self.ui.altura.text()))
        largura = eval(str(self.ui.largura.text()))
        constante = eval(str(self.ui.const_1.text()))
        angulo = eval(str(self.ui.const_2.text()))
        
        mat = Gerador.constante(n, altura, largura, angulo, constante)
        return campo_constante(n, altura, largura, constante, angulo, mat)
        
    def gera_doublet(self):
        n = eval(str(self.ui.num_mat.text()))
        altura = eval(str(self.ui.altura.text()))
        largura = eval(str(self.ui.largura.text()))
        magnitude = eval(str(self.ui.const_1.text()))
        inicio = complex(eval(str(self.ui.ini_x.text())),
                  eval(str(self.ui.ini_y.text())))
        
        mat = Gerador.doublet(n, altura, largura, magnitude, inicio)
        return campo_doublet(n, altura, largura, inicio, magnitude, mat)
    
    def gera_fonte(self):
        n = eval(str(self.ui.num_mat.text()))
        altura = eval(str(self.ui.altura.text()))
        largura = eval(str(self.ui.largura.text()))
        magnitude = eval(str(self.ui.const_1.text()))
        inicio = complex(eval(str(self.ui.ini_x.text())),
                  eval(str(self.ui.ini_y.text())))
        
        mat = Gerador.sumidouro(n, altura, largura, magnitude, inicio)
        return campo_fonte(n, altura, largura, inicio, magnitude, mat)
        
    def gera_turbilhao(self):
        n = eval(str(self.ui.num_mat.text()))
        altura = eval(str(self.ui.altura.text()))
        largura = eval(str(self.ui.largura.text()))
        magnitude = eval(str(self.ui.const_1.text()))
        posicao = eval(str(self.ui.const_2.text()))
        inicio = complex(eval(str(self.ui.ini_x.text())),
                  eval(str(self.ui.ini_y.text())))
        mat = Gerador.turbilhao(n, altura, largura, magnitude, posicao, inicio)
        return campo_turbilhao(n, altura, largura, inicio, magnitude, posicao, mat)
         
if __name__ == '__main__':
    
    #controle_mat()
    app = QtGui.QApplication(sys.argv)
    c = controle_mat(None)
    c.mw.showMaximized()
    sys.exit(app.exec_())   
