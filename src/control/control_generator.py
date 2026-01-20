# -*- coding: utf-8 -*-
'''
Módulo de controle do módulo de geração dos campos
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtCore, QtWidgets

# Componentes internos
from control.control_set_creator import Set_Creator_Ctrl
from control.control_analisys import Analise_Ctrl
from models.campos import campo_combinado
from utils.Constants import nomes_dos_campos
from view.view_generator import Generator_View


class Generator_Ctrl:
    '''
    Controla o módulo do gerador de campos de gradientes
    '''
    def __init__(self):
        '''
        Instancia atributos da classe e cria a interface gráfica
        '''
        self.pilha = []
        self.ui = Generator_View(self)
        self.ui.showMaximized()
        self.status = "" 

    def gerar_novo_campo(self):
        '''
        Chama ainterface de criação de um novo campo de gradientes
        '''
        self.ctrl_set_creator = Set_Creator_Ctrl(self)
        self.status = 'novo'
        
    def recebe_campo(self, campo):
        '''
        Recebe o campo gerado e acrescenta à lista de campos
            params:
                campo -> campo_aleatorio, campo_combinado, campo_constante,
                    campo_doublet, campo_fonte, campo_turbilhao
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
            i = self.ui.getListWidget().currentRow()
            if i < 0:
                message = QtWidgets.QMessageBox(self.ui)
                message.setText('Selecione um elemento da lista para editar')
                message.show()
                pass
            else:
                campo = self.pilha[self.ui.getListWidget().currentRow()]
                self.ctrl_set_creator = Set_Creator_Ctrl(self, campo)
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
                campo -> campo_aleatorio, campo_combinado, campo_constante,
                    campo_doublet, campo_fonte, campo_turbilhao
                    um campo de gradientes
        '''
        i = self.ui.getListWidget().currentRow()
        self.pilha[i] = campo
        self.ui.getListWidget().takeItem(i)
        self.ui.getListWidget().insertItem(i, QtWidgets.QListWidgetItem(nomes_dos_campos[campo.get_type()]))
        
    def add_novo_campo(self, campo):
        '''
        Adiciona uma nova entrada de campo de gradientes à lista
            params:
                campo -> campo_aleatorio, campo_combinado, campo_constante,
                    campo_doublet, campo_fonte, campo_turbilhao
                    um campo de gradientes
        '''
        self.pilha.insert(0, campo)
        self.ui.getListWidget().insertItem(0, QtWidgets.QListWidgetItem(nomes_dos_campos[campo.get_type()]))
        
    def combina_campos(self):
        '''
        Combina todos os campos da lista em um único através de operações
        matemáticas
        '''
        mat = []
        for campo in self.pilha:
            mat.append(campo.get_mat())
        m1 = list(zip(*mat))
        m2 = [list(zip(*m1[i])) for i in range(len(m1))]
        super_mat = []
        for matriz in m2:
            m = []
            for linha in matriz:
                novaLinha = list(zip(*linha))
                l = []
                for elemento in novaLinha:
                    l.append(tuple(map(sum, zip(*elemento))))
                m.append(l)
            super_mat.append(m)
            
        combinado = campo_combinado(len(super_mat), 
                                    len(super_mat[0]), 
                                    len(super_mat[0][0]), 
                                    super_mat[:], 
                                    self.pilha[:])
        self.pilha = []
        self.ui.getListWidget().clear()
        self.add_novo_campo(combinado)
        
        
    def remove_item(self):
        '''
        Remove uma entrada da lista de Campos de Gradientes
        '''
        i = self.ui.getListWidget().currentRow()
        if self.pilha:
            self.pilha.pop(i)
        else:
            message = QtWidgets.QMessageBox(self.ui)
            message.setText('A lista de campos está vazia')
            message.show()
        self.ui.getListWidget().takeItem(i)
        
    def limpa_lista(self):
        '''
        Limpa a lista de campos de gradientes
        '''
        self.pilha = []
        self.ui.getListWidget().clear()
        
    def analisar(self):
        '''
        Chama a interface de análise dos campos de gradientes para a entrada
        selecionada
        '''
        super_mat = (self.pilha[self.ui.getListWidget().currentRow()]).get_mat()
        c = Analise_Ctrl(super_mat)
        c.processa_matrizes()
 
