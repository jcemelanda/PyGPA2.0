# -*- coding:utf-8 -*-
'''
Módulo de controle do módulo principal
'''
#==================================Imports=====================================#

# Componentes PyQt5
from PyQt5 import QtWidgets, QtCore

# Standard Library
import sys

#Componentes Locais
from view.view_main import Main_View
from control.control_analisys import Analise_Ctrl
from control.control_generator import Generator_Ctrl

#=======================Preparação de ambiente da classe=======================#

# Configura conversão pra Unicode
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Main_Ctrl:
    '''
    Controla o módulo de seleção de funções onde o usuário escolhe entre
    gerar dados ou analisálos
    '''
    def __init__(self):
        '''
        Instancia uma nova aplicação gráfica PyQt5 que será usada por todo
        o ciclo de vida da aplicação
        '''
        app = QtWidgets.QApplication(sys.argv)
        self.ui = Main_View(self)
        self.ui.showMaximized()
        sys.exit(app.exec_())
        
    def abrir_gerador(self, arg):
        '''
        Chama o módulo de geração de campos de gradientes
        '''
        Generator_Ctrl()

    def abrir_analisador(self, arg):
        '''
        Chama o módulo de análise de campos gradientes
        '''
        Analise_Ctrl()