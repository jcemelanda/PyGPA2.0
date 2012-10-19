# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from controle_gerar_matriz import controle_mat
from ui.view_cria_campos import cria_campos_UI
from utils.Constants import *
from controle_analise import controle_analise
from modelos.campos import campo_combinado
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
class controle_cria_campo:
    def __init__(self, controle_principal):
        
        self.pilha = []
        
        self.window = QtGui.QMainWindow()
        self.ui = cria_campos_UI(self)
        self.ui.setupUi(self.window)

    def gerar_novo_campo(self):
        self.ctrl_gen = controle_mat(self)
        self.ctrl_gen.mw.showMaximized()
        self.status = 'novo'
        
    def recebe_campo(self, campo):
        if self.status == 'novo':
            self.add_novo_campo(campo)
        else:
            self.atualiza_campo(campo)
        self.ctrl_gen.mw.close()
        del(self.ctrl_gen)
        
    def atualizar_campo(self):
        if len(self.pilha) > 0:
            i = self.ui.listWidget.currentRow()
            if i<0:
                message = QtGui.QMessageBox(self.window)
                message.setText('Selecione um elemento da lista para editar')
                message.show()
            else:
                campo = self.pilha[self.ui.listWidget.currentRow()]
                self.ctrl_gen = controle_mat(self, campo)
                self.ctrl_gen.mw.showMaximized()
                self.status = 'edita'
        else:
            message = QtGui.QMessageBox(self.window)
            message.setText('Para inserir um campo, clique em Novo')
            message.show()
        
    def atualiza_campo(self, campo):
        i = self.ui.listWidget.currentRow()
        self.pilha[i] = campo
        self.ui.listWidget.takeItem(i)
        self.ui.listWidget.insertItem(i, QtGui.QListWidgetItem(_fromUtf8(nomes_dos_campos[campo.get_type()])))
        
    def add_novo_campo(self, campo):
        self.pilha.append(campo)
        self.ui.listWidget.addItem(QtGui.QListWidgetItem(_fromUtf8(nomes_dos_campos[campo.get_type()])))
        
    def combina_campos(self):
        mat = []
        for campo in self.pilha:
            mat.append(campo.get_mat())
        m1 = zip(*mat)
    
        m2 = [zip(*m1[i]) for i in range(len(m1))]
        super_mat = []
        for matriz in m2:
            m = []
            for linha in matriz:
                novaLinha = zip(*linha)
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
        self.ui.listWidget.clear()
        self.add_novo_campo(combinado)
        
        
    def remove_item(self):
        i = self.ui.listWidget.currentRow()
        self.pilha.pop(i)
        self.ui.listWidget.takeItem(i)
        
    def limpa_lista(self):
        self.pilha = []
        self.ui.listWidget.clear()
        
    def analisar(self):
        super_mat = (self.pilha[self.ui.listWidget.currentRow()]).get_mat()
        c = controle_analise(super_mat)
        c.janela_principal.showMaximized()
        c.processa_matrizes()
    
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    controle_cria_campo().window.showMaximized()
    sys.exit(app.exec_())
