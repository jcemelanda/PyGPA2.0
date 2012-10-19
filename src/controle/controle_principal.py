from PyQt4 import QtGui
from controle_analise import controle_analise
from ui.view_main import Main_UI
import sys
from controle_cria_campo import controle_cria_campo
from controle_gerar_matriz import controle_mat



class Controle_principal:
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Main_UI(self)
        ui.setupUi(MainWindow)
        self.ctrl_analise = controle_analise()
        self.ctrl_cria_campos = controle_cria_campo(self)
        self.ctrl_gerador = controle_mat(self.ctrl_cria_campos)
        MainWindow.show()
        sys.exit(app.exec_())
        
    def abrir_analise(self):
        self.ctrl_analise.janela_principal.showMaximized()
        
    def abrir_compositor(self):
        self.ctrl_cria_campos.window.showMaximized()
        
if __name__ == '__main__':
    Controle_principal()