from PyQt5 import QtWidgets, QtCore, QtGui
from widgets.window_analisys import Analysis_Window

class Analise_View(QtGui.QWindow):
    def __init__(self, controle):
        QtGui.QWindow.__init__(self)
        self.controle = controle
        self.ui = Analysis_Window()
        self.ui.setup(self)
        self.count = 3
        self.shortcut_right = QtWidgets.QShortcut(QtWidgets.QKeySequence("l"), self, self.controle.incrementa_view)
        self.shortcut_left = QtWidgets.QShortcut(QtWidgets.QKeySequence("j"), self, self.controle.decrementa_view)
        self.shortcut_end = QtWidgets.QShortcut(QtWidgets.QKeySequence("end"), self, self.controle.last_view)
        self.shortcut_home = QtWidgets.QShortcut(QtWidgets.QKeySequence("home"), self, self.controle.first_view)
        QtCore.QObject.connect(self.ui.actionAbrir_Conjunto_de_Matrizes, QtCore.SIGNAL(
                                    'triggered()'), self.controle.abrir_arquivo)
        QtCore.QObject.connect(self.ui.horizontalSlider, QtCore.SIGNAL(
                                    'valueChanged(int)'), self.controle.set_view)
        QtCore.QObject.connect(self.ui.Tabs, QtCore.SIGNAL(
                                    'currentChanged(int)'), self.controle.set_current_tab)

        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    av = Analise_View()
    av.add_widgets()
    av.showMaximized()
    sys.exit(app.exec_())
