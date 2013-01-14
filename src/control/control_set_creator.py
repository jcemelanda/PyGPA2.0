# -*- coding: utf-8 -*-
'''
Módulo de controle do módulo que gera os campos
'''
#==================================Imports=====================================#

# Componentes PyQt4
from PyQt4 import QtCore

#Componentes internos
from models.campos import campo_aleatorio, campo_constante, campo_doublet, \
    campo_fonte, campo_turbilhao
from utils.Gerador import Gerador
from view.view_set_creator import Set_Creator_View

#=======================Preparação de ambiente da classe=======================#

# Configura conversão pra Unicode
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        
     
    def gera_aleatorio(self, n=3, altura=3, largura=3):
        '''
        Gera um campo aleatório com os parâmetros passados
        params:
            n -> int
                Número de matrizes do campos gerado. Default: 3
            altura -> int
                Altura das matrizes que compõem o campo. Default: 3
            largura -> int
                Largura das matrizes que compõem o campo. Default: 3
        return:
            campos_aleatorio
                Campo aleatório gerado
        '''
        mat = Gerador.aleatorio(n, altura, largura)
        
        return campo_aleatorio(n, altura, largura, mat[:])
    
    def gera_constante(self, n=3, altura=3, largura=3, constante=1, angulo=0):
        '''
        Gera um campo cosntante com os parâmetros passados
        params:
            n -> int
                Número de matrizes do campos gerado. Default: 3
            altura -> int
                Altura das matrizes que compõem o campo. Default: 3
            largura -> int
                Largura das matrizes que compõem o campo. Default: 3
            constante -> int
                Constante usada para a geração do módulo dos vetores do campo 
                cosntante. Default:1
            angulo -> int
                Angulo dos vetores do campos constante
        return:
            campo_constante
                Campos constante gerado
        '''
        
        mat = Gerador.constante(n, altura, largura, angulo, constante)
        return campo_constante(n, altura, largura, constante, angulo, mat)
        
    def gera_doublet(self, n=3, altura=3, largura=3, magnitude=1, inicio=0+0j):
        '''
        Gera um campo doublet com os parâmetros passados
        params:
            n -> int
                Número de matrizes do campos gerado. Default: 3
            altura -> int
                Altura das matrizes que compõem o campo. Default: 3
            largura -> int
                Largura das matrizes que compõem o campo. Default: 3
            magnitude -> int
                magnitude usada para a geração do vetores do campo doublet. 
                Default:1
            inicio -> complex
                Ponto de início da movimentação do padrão doublet
        return:
            campo_doublet
                Campo Doublet Gerado
        '''
        mat = Gerador.doublet(n, altura, largura, magnitude, inicio)
        return campo_doublet(n, altura, largura, inicio, magnitude, mat)
    
    def gera_fonte(self, n, altura, largura, magnitude, inicio):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        params:
            n -> int
                Número de matrizes do campos gerado. Default: 3
            altura -> int
                Altura das matrizes que compõem o campo. Default: 3
            largura -> int
                Largura das matrizes que compõem o campo. Default: 3
            magnitude -> int
                magnitude usada para a geração do vetores do campo fonte. 
                Default:1
            inicio -> complex
                Ponto de início da movimentação do padrão fonte
        return:
            campo_fonte
                Campo Fonte/Sumidouro Gerado
        '''
        mat = Gerador.sumidouro(n, altura, largura, magnitude, inicio)
        return campo_fonte(n, altura, largura, inicio, magnitude, mat)
        
    def gera_turbilhao(self, n=3, altura=3, largura=3, magnitude=1, posicao=1, 
                       inicio=0+0j):
        '''
        Gera um campo fonte/sumidouro com os parâmetros passados
        params:
            n -> int
                Número de matrizes do campos gerado. Default: 3
            altura -> int
                Altura das matrizes que compõem o campo. Default: 3
            largura -> int
                Largura das matrizes que compõem o campo. Default: 3
            magnitude -> int
                magnitude usada para a geração do vetores do campo turbilhão. 
                Default:1
            posicao -> int
                posição. Default 1
            inicio -> complex
                Ponto de início da movimentação do padrão turbilhão
        return:
            campo_fonte
                Campo Turbilhão Gerado
        '''
        mat = Gerador.turbilhao(n, altura, largura, magnitude, posicao, inicio)
        return campo_turbilhao(n, altura, largura, inicio, magnitude, posicao, mat)
         
    def close_window(self):
        '''
        Fecha a janela do gerador de campos
        '''
        self.ui.close()