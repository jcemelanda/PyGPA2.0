from PyQt6 import QtGui, QtCore, QtWidgets
from widgets.window_start import StartWindow

class MainView(QtWidgets.QMainWindow):
    def __init__(self, controle):
        super().__init__()
        self.controle = controle
        self.ui = StartWindow()
        self.ui.setup(self)

        self.ui.botao_editar.clicked.connect(self.controle.abrir_gerador)
        self.ui.botao_novo_campo.clicked.connect(self.controle.abrir_analisador)

        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    av = MainView()
    av.add_widgets()
    av.showMaximized()
    sys.exit(app.exec())