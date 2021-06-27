# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
from widgets.window_generator import Generator_Window
class Generator_View(QtGui.QWindow):
    def __init__(self, controle):
        QtGui.QWindow.__init__(self)
        self.controle = controle
        self.ui = Generator_Window()
        self.ui.setup(self)
        
        QtCore.QObject.connect(self.ui.botao_editar, QtCore.SIGNAL(
                                    'clicked()'), self.controle.atualizar_campo)
        QtCore.QObject.connect(self.ui.botao_novo_campo, QtCore.SIGNAL(
                                    'clicked()'), self.controle.gerar_novo_campo)
        QtCore.QObject.connect(self.ui.botao_analisar, QtCore.SIGNAL(
                                    'clicked()'), self.controle.analisar)
        QtCore.QObject.connect(self.ui.botao_combinar, QtCore.SIGNAL(
                                    'clicked()'), self.controle.combina_campos)
        QtCore.QObject.connect(self.ui.botao_limpar, QtCore.SIGNAL(
                                    'clicked()'), self.controle.limpa_lista)
        QtCore.QObject.connect(self.ui.botao_remove, QtCore.SIGNAL(
                                    'clicked()'), self.controle.remove_item)

    def getListWidget(self):
        return self.ui.listWidget