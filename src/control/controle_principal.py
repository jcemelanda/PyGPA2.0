# -*- coding:utf-8 -*-
'''
Módulo de controle do módulo principal
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtWidgets, QtCore

# Standard Library
import sys

#Componentes Locais
from view.visao_principal import MainView
from control.controle_analise import AnaliseCtrl
from control.controle_gerador import GeneratorCtrl

class MainCtrl:
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
        self.ui = MainView(self)
        self.ui.showMaximized()
        sys.exit(app.exec())
        
    def abrir_gerador(self, arg):
        '''
        Chama o módulo de geração de campos de gradientes
        '''
        GeneratorCtrl()

    def abrir_analisador(self, arg):
        '''
        Chama o módulo de análise de campos gradientes
        '''
        AnaliseCtrl()