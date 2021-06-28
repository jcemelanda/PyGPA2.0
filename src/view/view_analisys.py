from PyQt5 import QtWidgets, QtGui
from widgets.window_analisys import Analysis_Window

class Analise_View(QtWidgets.QMainWindow):
    def __init__(self, controle):
        super().__init__()
        self.controle = controle
        self.ui = Analysis_Window()
        self.ui.setup(self)
        self.count = 3
        self.shortcut_right = QtWidgets.QShortcut(QtGui.QKeySequence("l"), self, self.controle.incrementa_view)
        self.shortcut_left = QtWidgets.QShortcut(QtGui.QKeySequence("j"), self, self.controle.decrementa_view)
        self.shortcut_end = QtWidgets.QShortcut(QtGui.QKeySequence("end"), self, self.controle.last_view)
        self.shortcut_home = QtWidgets.QShortcut(QtGui.QKeySequence("home"), self, self.controle.first_view)
        self.ui.actionAbrir_Conjunto_de_Matrizes.triggered.connect(self.controle.abrir_arquivo)
        self.ui.horizontalSlider.valueChanged.connect(self.controle.set_view)
        self.ui.Tabs.currentChanged.connect(self.controle.set_current_tab)

        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    av = Analise_View()
    av.add_widgets()
    av.showMaximized()
    sys.exit(app.exec_())
