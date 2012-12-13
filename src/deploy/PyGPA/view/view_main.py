from PyQt4 import QtGui, QtCore
from widgets.window_start import Start_Window

class Main_View(QtGui.QMainWindow):
    def __init__(self, controle):
        QtGui.QMainWindow.__init__(self)
        self.controle = controle
        self.ui = Start_Window()
        self.ui.setup(self)

        QtCore.QObject.connect(self.ui.botao_editar, QtCore.SIGNAL(
                                    'clicked()'), self.controle.abrir_gerador)
        QtCore.QObject.connect(self.ui.botao_novo_campo, QtCore.SIGNAL(
                                    'clicked()'), self.controle.abrir_analisador)

        
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = Main_View()
    av.add_widgets()
    av.showMaximized()
    sys.exit(app.exec_())