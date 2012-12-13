# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from models.campos import campo_aleatorio, campo_constante, campo_doublet, \
    campo_fonte, campo_turbilhao
from utils.Gerador import Gerador
from view.view_set_creator import Set_Creator_View
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Set_Creator_Ctrl:
    def __init__(self, gen_ctrl, campo=None):
        self.funcoes = {
                        0:self.gera_aleatorio,
                        1:self.gera_constante,
                        2:self.gera_doublet,
                        3:self.gera_fonte,
                        4:self.gera_turbilhao
                        }
        self.ui = Set_Creator_View(self)
        self.ui.showMaximized()
        self.ctrl = gen_ctrl
        if campo != None:
            self.ui.inicia_campos(campo)
            
    def gerar_matrizes(self):
        self.ctrl.recebe_campo(self.funcoes[self.ui.get_indice_selecionado()]())
        
     
    def gera_aleatorio(self):
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        
        mat = Gerador.aleatorio(n, altura, largura)
        
        return campo_aleatorio(n, altura, largura, mat[:])
    
    def gera_constante(self):
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        constante = eval(str(self.ui.get_const_1()))
        angulo = eval(str(self.ui.get_const_2()))
        
        mat = Gerador.constante(n, altura, largura, angulo, constante)
        return campo_constante(n, altura, largura, constante, angulo, mat)
        
    def gera_doublet(self):
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        magnitude = eval(str(self.ui.get_const_1()))
        inicio = complex(eval(str(self.ui.get_ini_x())),
                  eval(str(self.ui.get_ini_y())))
        
        mat = Gerador.doublet(n, altura, largura, magnitude, inicio)
        return campo_doublet(n, altura, largura, inicio, magnitude, mat)
    
    def gera_fonte(self):
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        magnitude = eval(str(self.ui.get_const_1()))
        inicio = complex(eval(str(self.ui.get_ini_x())),
                  eval(str(self.ui.get_ini_y())))
        
        mat = Gerador.sumidouro(n, altura, largura, magnitude, inicio)
        return campo_fonte(n, altura, largura, inicio, magnitude, mat)
        
    def gera_turbilhao(self):
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        magnitude = eval(str(self.ui.get_const_1()))
        posicao = eval(str(self.ui.get_const_2()))
        inicio = complex(eval(str(self.ui.get_ini_x())),
                  eval(str(self.ui.get_ini_y())))
        mat = Gerador.turbilhao(n, altura, largura, magnitude, posicao, inicio)
        return campo_turbilhao(n, altura, largura, inicio, magnitude, posicao, mat)
         
    def close_window(self):
        self.ui.close()