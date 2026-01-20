# -*- coding: utf-8 -*-
'''
Módulo de controle do módulo que gera os campos
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtCore

#Componentes internos
from models.campos import CampoAleatorio, CampoConstante, CampoDoublet, \
    CampoFonte, CampoTurbilhao
from utils.gerador import Gerador
from view.visao_criador_conjunto import SetCreatorView


class SetCreatorCtrl:
    '''
    Controla a interface de criação de conjuntos de dados,
    '''
    def __init__(self, gen_ctrl, campo=None):
        '''
        Inicia as veriáveis e atributos da classe e instancia a interface 
        gráfica
        params:
            gen_ctrl -> GeneratorCtrl
                Instância do controlador de geração de campos que armazena os 
                campos gerados aqui
            campo -> CampoAleatorio, CampoConstante, CampoTurbilhao, 
                CampoDoublet
                opcional - campo recebido para edição de seus dados
        '''
        self.funcoes = {
                        0:self.gera_aleatorio,
                        1:self.gera_constante,
                        2:self.gera_doublet,
                        3:self.gera_fonte,
                        4:self.gera_turbilhao
                        }
        self.ui = SetCreatorView(self)
        self.ui.showMaximized()
        self.ctrl = gen_ctrl
        if campo != None:
            self.ui.inicia_campos(campo)
            
    def gerar_matrizes(self):
        '''
        Gera as matrizes e coloca o campo gerado na lista de campos do 
        GeneratorCtrl
        '''
        
        self.ctrl.recebe_campo(self.funcoes[self.ui.indice_selecionado]())
        
     
    def gera_aleatorio(self):
        '''
        Gera um campo aleatório com os parâmetros passados
        return:
            campos_aleatorio
                Campo aleatório gerado
        '''
        n = eval(str(self.ui.num_mat))
        altura = eval(str(self.ui.altura))
        largura = eval(str(self.ui.largura))
        
        mat = Gerador.aleatorio(n, altura, largura)
        
        return CampoAleatorio(n, altura, largura, mat[:])
    
    def gera_constante(self):
        '''
        Gera um campo cosntante com os parâmetros passados
        return:
            campo_constante
                Campos constante gerado
        '''
        
        n = eval(str(self.ui.num_mat))
        altura = eval(str(self.ui.altura))
        largura = eval(str(self.ui.largura))
        constante = eval(str(self.ui.const_1))
        angulo = eval(str(self.ui.const_2))
        
        mat = Gerador.constante(n, altura, largura, angulo, constante)
        return CampoConstante(n, altura, largura, constante, angulo, mat)
        
    def gera_doublet(self):
        '''
        Gera um campo doublet com os parâmetros passados
        return:
            campo_doublet
                Campo Doublet Gerado
        '''
        
        n = eval(str(self.ui.num_mat))
        altura = eval(str(self.ui.altura))
        largura = eval(str(self.ui.largura))
        magnitude = eval(str(self.ui.const_1))
        vel = eval(str(self.ui.const_2))
        inicio = complex(eval(str(self.ui.ini_x)),
                  eval(str(self.ui.ini_y)))
        
        mat = Gerador.doublet(n, altura, largura, magnitude, inicio, vel.real, vel.imag)
        return CampoDoublet(n, altura, largura, inicio, magnitude, mat)
    
    def gera_fonte(self):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        return:
            campo_fonte
                Campo Fonte/Sumidouro Gerado
        '''
        n = eval(str(self.ui.num_mat))
        altura = eval(str(self.ui.altura))
        largura = eval(str(self.ui.largura))
        magnitude = eval(str(self.ui.const_1))
        vel = eval(str(self.ui.const_2))
        inicio = complex(eval(str(self.ui.ini_x)),
                  eval(str(self.ui.ini_y)))
        
        mat = Gerador.sumidouro(n, altura, largura, magnitude, inicio, vel.real, vel.imag)
        return CampoFonte(n, altura, largura, inicio, magnitude, mat)
        
    def gera_turbilhao(self):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        return:
            campo_fonte
                Campo Turbilhão Gerado
        '''
        
        n = eval(str(self.ui.num_mat))
        altura = eval(str(self.ui.altura))
        largura = eval(str(self.ui.largura))
        magnitude = eval(str(self.ui.const_1))
        vel = eval(str(self.ui.const_2))
        posicao = 0 # Unused in new logical vortex
        inicio = complex(eval(str(self.ui.ini_x)),
                  eval(str(self.ui.ini_y)))
        
        mat = Gerador.turbilhao(n, altura, largura, magnitude, posicao, inicio, vel.real, vel.imag)
        return CampoTurbilhao(n, altura, largura, inicio, magnitude, posicao, mat)
         
    def close_window(self):
        '''
        Fecha a janela do gerador de campos
        '''
        self.ui.close()