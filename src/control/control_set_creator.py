# -*- coding: utf-8 -*-
'''
Módulo de controle do módulo que gera os campos
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtCore

#Componentes internos
from models.campos import campo_aleatorio, campo_constante, campo_doublet, \
    campo_fonte, campo_turbilhao
from utils.Gerador import Gerador
from view.view_set_creator import Set_Creator_View


class Set_Creator_Ctrl:
    '''
    Controla a interface de criação de conjuntos de dados,
    '''
    def __init__(self, gen_ctrl, campo=None):
        '''
        Inicia as veriáveis e atributos da classe e instancia a interface 
        gráfica
        params:
            gen_ctrl -> Generator_Ctrl
                Instância do controlador de geração de campos que armazena os 
                campos gerados aqui
            campo -> campo_aleatorio, campo_constante, campo_turbilhao, 
                campo_doublet
                opcional - campo recebido para edição de seus dados
        '''
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
        '''
        Gera as matrizes e coloca o campo gerado na lista de campos do 
        Generator_Ctrl
        '''
        
        self.ctrl.recebe_campo(self.funcoes[self.ui.get_indice_selecionado()]())
        
     
    def gera_aleatorio(self):
        '''
        Gera um campo aleatório com os parâmetros passados
        return:
            campos_aleatorio
                Campo aleatório gerado
        '''
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        
        mat = Gerador.aleatorio(n, altura, largura)
        
        return campo_aleatorio(n, altura, largura, mat[:])
    
    def gera_constante(self):
        '''
        Gera um campo cosntante com os parâmetros passados
        return:
            campo_constante
                Campos constante gerado
        '''
        
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        constante = eval(str(self.ui.get_const_1()))
        angulo = eval(str(self.ui.get_const_2()))
        
        mat = Gerador.constante(n, altura, largura, angulo, constante)
        return campo_constante(n, altura, largura, constante, angulo, mat)
        
    def gera_doublet(self):
        '''
        Gera um campo doublet com os parâmetros passados
        return:
            campo_doublet
                Campo Doublet Gerado
        '''
        
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        magnitude = eval(str(self.ui.get_const_1()))
        inicio = complex(eval(str(self.ui.get_ini_x())),
                  eval(str(self.ui.get_ini_y())))
        
        mat = Gerador.doublet(n, altura, largura, magnitude, inicio)
        return campo_doublet(n, altura, largura, inicio, magnitude, mat)
    
    def gera_fonte(self):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        return:
            campo_fonte
                Campo Fonte/Sumidouro Gerado
        '''
        n = eval(str(self.ui.get_num_mat()))
        altura = eval(str(self.ui.get_altura()))
        largura = eval(str(self.ui.get_largura()))
        magnitude = eval(str(self.ui.get_const_1()))
        inicio = complex(eval(str(self.ui.get_ini_x())),
                  eval(str(self.ui.get_ini_y())))
        
        mat = Gerador.sumidouro(n, altura, largura, magnitude, inicio)
        return campo_fonte(n, altura, largura, inicio, magnitude, mat)
        
    def gera_turbilhao(self):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        return:
            campo_fonte
                Campo Turbilhão Gerado
        '''
        
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
        '''
        Fecha a janela do gerador de campos
        '''
        self.ui.close()