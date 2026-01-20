# -*- coding: utf-8 -*-
'''
Módulo de controle do módulo de geração dos campos
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtCore, QtWidgets

# Componentes internos
from control.controle_criador_conjunto import SetCreatorCtrl
from control.controle_analise import AnaliseCtrl
from models.campos import CampoCombinado
from utils.constantes import nomes_dos_campos
from view.visao_gerador import GeneratorView


class GeneratorCtrl:
    '''
    Controla o módulo do gerador de campos de gradientes
    '''
    def __init__(self):
        '''
        Instancia atributos da classe e cria a interface gráfica
        '''
        self.pilha = []
        self.ui = GeneratorView(self)
        self.ui.showMaximized()
        self.status = "" 

    def gerar_novo_campo(self):
        '''
        Chama ainterface de criação de um novo campo de gradientes
        '''
        self.ctrl_set_creator = SetCreatorCtrl(self)
        self.status = 'novo'
        
    def recebe_campo(self, campo):
        '''
        Recebe o campo gerado e acrescenta à lista de campos
            params:
                campo -> CampoAleatorio, CampoCombinado, CampoConstante,
                    CampoDoublet, CampoFonte, CampoTurbilhao
                    um campo de gradientes
        '''
        if self.status == 'novo':
            self.add_novo_campo(campo)
        else:
            self.atualiza_campo(campo)
        self.ctrl_set_creator.close_window()
        del(self.ctrl_set_creator)
        
    def atualizar_campo(self):
        '''
        Chama a interface que atualiza os dados do campos de gradientes
        '''
        if len(self.pilha) > 0:
            i = self.ui.list_widget.currentRow()
            if i < 0:
                message = QtWidgets.QMessageBox(self.ui)
                message.setText('Selecione um elemento da lista para editar')
                message.show()
                pass
            else:
                campo = self.pilha[self.ui.list_widget.currentRow()]
                self.ctrl_set_creator = SetCreatorCtrl(self, campo)
                self.status = 'edita'
        else:
            message = QtWidgets.QMessageBox(self.ui)
            message.setText('Para inserir um campo, clique em Novo')
            message.show()
            pass
        
    def atualiza_campo(self, campo):
        '''
        Atualiza os dados de um campo de gradientes selecionado
            params:
                campo -> CampoAleatorio, CampoCombinado, CampoConstante,
                    CampoDoublet, CampoFonte, CampoTurbilhao
                    um campo de gradientes
        '''
        i = self.ui.list_widget.currentRow()
        self.pilha[i] = campo
        self.ui.list_widget.takeItem(i)
        self.ui.list_widget.insertItem(i, QtWidgets.QListWidgetItem(nomes_dos_campos[campo.type]))
        
    def add_novo_campo(self, campo):
        '''
        Adiciona uma nova entrada de campo de gradientes à lista
            params:
                campo -> CampoAleatorio, CampoCombinado, CampoConstante,
                    CampoDoublet, CampoFonte, CampoTurbilhao
                    um campo de gradientes
        '''
        self.pilha.insert(0, campo)
        self.ui.list_widget.insertItem(0, QtWidgets.QListWidgetItem(nomes_dos_campos[campo.type]))
        
    def combina_campos(self):
        '''
        Combina todos os campos da lista em um único através de operações
        matemáticas
        '''
        import numpy as np
        # Extrai matrizes. Elas já são arrays numpy graças a atualização do Gerador
        # Lista de arrays [mat1, mat2, ...] 
        # Cada mat é (n, h, w)
        matrizes = [campo.mat for campo in self.pilha]
        
        # Verifica se tem o mesmo formato? Assumindo que sim pela lógica da UI.
        # Mas e se n for diferente?
        # Vamos confiar nas restrições da UI ou broadcast. 
        # Na verdade campos só podem ser combinados se os formatos coincidirem.
        # Assumindo lógica simples de adição:
        
        if not matrizes:
             return

        # Soma Vetorizada
        # Se todas as mat são (n, h, w), sum(axis=0) cria (n, h, w) campo mas superposto?
        # Não, queremos somar os campos elemento a elemento.
        # super_matriz = sum(mat1, mat2, ...)
        
        # Empilhando: shape (k, n, h, w)
        # Soma ao longo do eixo 0 -> (n, h, w)
        try:
             super_matriz = np.sum(matrizes, axis=0)
        except ValueError as e:
             # Lida com incompatibilidade de formato potencialmente
             message = QtWidgets.QMessageBox(self.ui)
             message.setText(f'Erro ao combinar campos: {e}')
             message.show()
             return
            
        # formato super_matriz é (n, h, w) para complex128
        n, h, w = super_matriz.shape
        
        combinado = CampoCombinado(n, 
                                    h, 
                                    w, 
                                    super_matriz, 
                                    self.pilha[:])
        self.pilha = []
        self.ui.list_widget.clear()
        self.add_novo_campo(combinado)
        
        
    def remove_item(self):
        '''
        Remove uma entrada da lista de Campos de Gradientes
        '''
        i = self.ui.list_widget.currentRow()
        if self.pilha:
            self.pilha.pop(i)
        else:
            message = QtWidgets.QMessageBox(self.ui)
            message.setText('A lista de campos está vazia')
            message.show()
        self.ui.list_widget.takeItem(i)
        
    def limpa_lista(self):
        '''
        Limpa a lista de campos de gradientes
        '''
        self.pilha = []
        self.ui.list_widget.clear()
        
    def analisar(self):
        '''
        Chama a interface de análise dos campos de gradientes para a entrada
        selecionada
        '''
        super_mat = (self.pilha[self.ui.list_widget.currentRow()]).mat
        c = AnaliseCtrl(super_mat)
        c.processa_matrizes()
 
