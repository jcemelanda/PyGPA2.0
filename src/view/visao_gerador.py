# -*- coding: utf-8 -*-
from PyQt6 import QtWidgets
from widgets.janela_gerador import GeneratorWindow

class GeneratorView(QtWidgets.QMainWindow):
    def __init__(self, controle):
        super().__init__()
        self.controle = controle
        self.ui = GeneratorWindow()
        self.ui.setup(self)
        
        self.ui.botao_editar.clicked.connect(self.controle.atualizar_campo)
        self.ui.botao_novo_campo.clicked.connect(self.controle.gerar_novo_campo)
        self.ui.botao_analisar.clicked.connect(self.controle.analisar)
        self.ui.botao_combinar.clicked.connect(self.controle.combina_campos)
        self.ui.botao_limpar.clicked.connect(self.controle.limpa_lista)
        self.ui.botao_remove.clicked.connect(self.controle.remove_item)

    @property
    def list_widget(self):
        return self.ui.listWidget