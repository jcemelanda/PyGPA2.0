from PyQt6 import QtWidgets, QtGui
from widgets.janela_analise import AnalysisWindow

class AnaliseView(QtWidgets.QMainWindow):
    def __init__(self, controle):
        super().__init__()
        self.controle = controle
        self.ui = AnalysisWindow()
        self.ui.setup(self)
        self.count = 3
        self.shortcut_right = QtGui.QShortcut(QtGui.QKeySequence("l"), self)
        self.shortcut_right.activated.connect(self.controle.incrementa_view)
        self.shortcut_left = QtGui.QShortcut(QtGui.QKeySequence("j"), self)
        self.shortcut_left.activated.connect(self.controle.decrementa_view)
        self.shortcut_end = QtGui.QShortcut(QtGui.QKeySequence("end"), self)
        self.shortcut_end.activated.connect(self.controle.last_view)
        self.shortcut_home = QtGui.QShortcut(QtGui.QKeySequence("home"), self)
        self.shortcut_home.activated.connect(self.controle.first_view)
        self.ui.actionAbrir_Conjunto_de_Matrizes.triggered.connect(self.controle.abrir_arquivo)
        self.ui.horizontalSlider.valueChanged.connect(self.controle.set_view)
        self.ui.Tabs.currentChanged.connect(self.controle.set_current_tab)

        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    av = AnaliseView()
    av.add_widgets()
    av.showMaximized()
    sys.exit(app.exec())
