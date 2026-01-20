# -*- coding:utf-8 -*-
'''
Módulo de controle do módulo de análise
'''
#==================================Imports=====================================#

# Componentes PyQt6
from PyQt6 import QtWidgets, QtCore

# Componentes Matplotlib
from matplotlib import tri
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg \
    as FigureWidget, NavigationToolbar2QT as Navbar
from matplotlib.figure import Figure

# Componentes internos
from view.visao_analise import AnaliseView
from widgets.widget_detalhe import DetailWidget
from widgets.widget_graficos import GraphicsWidget

# PIL
from PIL import Image

# Standard Library
import time


class AnaliseCtrl:
    '''
    Controla o funcionamento do módulo de análise de gradientes
    '''
    def __init__(self, mat=[]):
        '''
        Inicializa os atributos e variáveis da classe
        params:
            mat -> list
                Opcional - lista de campos de gradientes que serão análisados
        '''
        self.ui = AnaliseView(self)
        self.ui.showMaximized()
        self.matrizes = mat
        self.figuras_vet = []
        self.figuras_vet_detail = []  # Separate figures for detailed tab
        self.GAs = []
        self.figuras_triang = []
        self.figuras_triang_detail = []  # Separate figures for detailed tab
        self.figuras_GA = []
        self.pos = 0
        self.current_tab = 0
        if len(self.matrizes) > 0:
            self.ABERTURA = 'direta'
            self.normalizado = False
        else:
            self.ABERTURA = 'normal'
        
    def incrementa_view(self):
        '''
        Muda o conjunto de dados sendo exibido para o próximo da lista
        '''
        
        self.pos += 1
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(True)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(False)
    
    def set_current_tab(self, tab):
        '''
        Ajusta a aba que deve ser exibida
        params: 
            tab -> int 
                indice da aba que será exibida
        '''
        
        self.current_tab = tab
        self.set_view(self.pos)
        
    def decrementa_view(self):
        '''
        Muda o conjunto de dados sendo exibido para o anterior da lista
        '''
        
        self.pos -= 1
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(True)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(False)
                
    def last_view(self):
        '''
        Muda a exibição para o último conjunto da lista
        '''

        self.pos = self.ui.ui.stackedGraphics.count() - 1
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(True)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(False)
    
    def first_view(self):
        '''
        Muda a exibição para o prieiro conjunto da lista
        '''

        self.pos = 0
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(True)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        self.ui.ui.horizontalSlider.blockSignals(False)
                
    def set_view(self, pos):
        '''
        Ajusta a posição da lista de dados para a posição passada como
        parâmetro
        params:
            pos -> int
                Posição da lista que será exibida
        '''
        
        self.pos = pos
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        # Only block signals if we're changing the slider value programmatically
        # and it's different from the current value
        if self.ui.ui.horizontalSlider.value() != self.pos:
            self.ui.ui.horizontalSlider.blockSignals(True)
            self.ui.ui.horizontalSlider.setValue(self.pos)
            self.ui.ui.horizontalSlider.blockSignals(False)
                
    def abrir_arquivo(self):
        '''
        Abre um arquivo contendo uma matriz bidimensional de dados ou uma 
        imagem e gera a matriz de dados interna do programa
        '''
        
        self.figuras_vet = []
        self.figuras_vet_detail = []
        self.figuras_triang = []
        self.figuras_triang_detail = []
        self.figuras_GA = []
        self.normalizado = False
        self.matrizes = []
        fd = QtWidgets.QFileDialog()
        file_path, _ = fd.getOpenFileName(parent=None,
                                caption=u'Abrir arquivo',
        filter=u'Dados textuais (*.txt *.dat);;Imagens (*.png *.bmp *.jpg)')
        if file_path[-3:] in ['png', 'jpg', 'bmp']:
            try:
                im = Image.open(file_path, 'r')
                mat = []
                im = im.convert('L')
                w, h = im.size
                mat = []
                dlg = QtWidgets.QProgressDialog(u'Lendo Arquivo', u'Cancelar',
                                        0, h)
                dlg.setModal(True)
                dlg.setMinimumDuration(0)
                dlg.setAutoClose(True)
                dlg.setWindowTitle(u'Leitura de Arquivo')
                dlg.show()
                for i in range(h):
                    line = []
                    for j in range(w):
                        line.append(im.getpixel((j, i)))
                    mat.append(line)
                    dlg.setValue(i)
                    if dlg.wasCanceled():
                        return
                mat.reverse()
                self.matriz = mat[:]
                self.matrizes.append(self.matriz)
            except IOError as e:
                print('Abertura de arquivo falhou ', e)
                return
        else:
            try:
                with open(file_path, 'r') as f:
                    mat_lines = f.readlines()
            except IOError as e:
                print('Abertura de arquivo falhou ', e)
                return
            supermatriz = []
            matriz = []
            self.matriz = []
            a = 0
            if mat_lines[-1] == '':
                mat_lines.pop()
            for line in mat_lines:
                a += 1
                if line == '\n':
                    matriz.reverse()
                    supermatriz.append(matriz[:])
                    matriz = []
                    continue
                row = line.strip('\n').split(' ')
                if row[-1] == '':
                    matriz.append([eval(e) for e in row[:-1]])
                else:
                    matriz.append([eval(e) for e in row])
                    a += 1
            matriz.reverse()
            supermatriz.append(matriz[:])
            
            self.matrizes = supermatriz[:]
        self.processa_matrizes()
        
        self.first_view()
        
        
    def processa_matrizes(self):
        '''
        Opera sobre o conjunto de matrizes gerando os vetores, 
        triangulações e widgets
        '''
        
        for mat in self.matrizes:
            self.matriz = mat[:]
            self.gerar_vetores()
            self.gerar_triangulacao()
        self.gerar_grafico_GA()
        self.gerar_widgets()
        
    def gerar_grafico_GA(self):
        '''
        Gera o gráfico de graus de assimetria dos conjuntos de dados
        '''
        
        for i in range(len(self.matrizes)):
            self.figuras_GA.append(Figure(dpi=120))
            eixos = self.figuras_GA[-1].add_subplot(111)
            eixos.plot(range(len(self.GAs)), self.GAs)
            eixos.plot(i, self.GAs[i], 'ro')
            
      
    def gerar_vetores(self):
        '''
        Gera o campo de gradientes do conjunto de dados a partir das componentes
        NumPy arrays: self.matriz é array complexo (h, w)
        '''
        import numpy as np
        
        # Se aberto de arquivo (imagem), pode ser lista de listas.
        # Verifica tipo
        if isinstance(self.matriz, list):
             self.matriz = np.array(self.matriz)
        
        # Se for array complexo do Gerador
        if np.iscomplexobj(self.matriz):
             # U = Real, V = Imag
             # Sistema de coordenadas: indexação de matriz (linha, col)
             # Quiver espera X, Y, U, V.
             self.dx = self.matriz.real
             self.dy = self.matriz.imag
             # Extração direta das componentes real e imaginária
        else:
             # Campo escalar (Importação de imagem)
             # Usa np.gradient
             self.dy, self.dx = np.gradient(self.matriz)
             # Nota: gradient retorna (gradiente eixo 0, gradiente eixo 1) -> (dy, dx)
             
        # Normalização
        norm = np.hypot(self.dx, self.dy)
        max_val = np.max(norm)
        if max_val > 0:
             self.dx /= max_val
             self.dy /= max_val
             
        # Plotagem
        min_x = -1
        max_x = self.dx.shape[1] # largura
        min_y = -1
        max_y = self.dx.shape[0] # altura
        
        # Cria figura para aba de visão geral
        self.figuras_vet.append(Figure(dpi=120))
        eixos = self.figuras_vet[-1].add_subplot(111, aspect='equal')
        # Quiver no mpl aceita arrays 2D diretamente
        # Grade X, Y
        X, Y = np.meshgrid(np.arange(max_x), np.arange(max_y))
        
        q = eixos.quiver(X, Y, self.dx, self.dy, angles='xy', scale=1.0,
                                scale_units='xy', minshaft=2, minlength=1)
        eixos.quiverkey(q, 0, min_y - 2, 1, '', coordinates='data')
        eixos.set_xlim(min_x, max_x)
        eixos.set_ylim(min_y, max_y)
        
        # Cria figura separada para aba de detalhes
        self.figuras_vet_detail.append(Figure(dpi=120))
        eixos_detalhe = self.figuras_vet_detail[-1].add_subplot(111, aspect='equal')
        q_detalhe = eixos_detalhe.quiver(X, Y, self.dx, self.dy, angles='xy', scale=1.0,
                                scale_units='xy', minshaft=2, minlength=1)
        eixos_detalhe.quiverkey(q_detalhe, 0, min_y - 2, 1, '', coordinates='data')
        eixos_detalhe.set_xlim(min_x, max_x) # largura
        eixos_detalhe.set_ylim(min_y, max_y) # altura
        

        
    def gerar_triangulacao(self):
        '''
        Gera a triangulação de Delaunay para o conjunto de dados,
        plota os triângulos e exibe o número de arestas encontradas
        (Versão Vetorizada NumPy)
        '''
        import numpy as np
        
        # Self.dx e self.dy são arrays (h, w) normalizados
        h, w = self.dx.shape
        
        # Cria coordenadas da grade
        X, Y = np.meshgrid(np.arange(w), np.arange(h))
        
        # Vetorizado P_final
        # Px = X + dx
        # Py = Y + dy
        Px = X + self.dx
        Py = Y + self.dy
        
        # Linearizar para Delaunay
        # Filtrar vetores pequenos (ruído)
        
        mascara = (np.abs(self.dx) > 1e-6) | (np.abs(self.dy) > 1e-6)
        x_filtrado = Px[mascara]
        y_filtrado = Py[mascara]
        
        if len(x_filtrado) < 3:
             # Pontos insuficientes para triangulação
             self.GAs.append(0)
             # Cria figura vazia
             self.figuras_triang.append(Figure(dpi=120))
             self.figuras_triang_detail.append(Figure(dpi=120))
             return

        # Triangulação Matplotlib
        try:
            t = tri.Triangulation(x_filtrado, y_filtrado)
            
            # Cria figura para aba de visão geral
            self.figuras_triang.append(Figure(dpi=120))
            eixos = self.figuras_triang[-1].add_subplot(111, aspect='equal')
            
            min_x = np.min(x_filtrado) - 1
            max_x = np.max(x_filtrado) + 1
            min_y = np.min(y_filtrado) - 1
            max_y = np.max(y_filtrado) + 1
            
            eixos.set_xlim(min_x, max_x)
            eixos.set_ylim(min_y, max_y)
            eixos.triplot(t)
            
            # Cria figura separada para aba de detalhes
            self.figuras_triang_detail.append(Figure(dpi=120))
            eixos_detalhe = self.figuras_triang_detail[-1].add_subplot(111, aspect='equal')
            eixos_detalhe.set_xlim(min_x, max_x)
            eixos_detalhe.set_ylim(min_y, max_y)
            eixos_detalhe.triplot(t)
    
            # Cálculo do GA (Grau de Assimetria)
            # Original: (len(arestas) - len(pontos)) / len(pontos)
            num_arestas = len(t.edges)
            num_pontos = len(x_filtrado)
            if num_pontos > 0:
                self.GAs.append((num_arestas - num_pontos) / num_pontos)
            else:
                 self.GAs.append(0)
                 
        except Exception as e:
            print(f"Falha na triangulação: {e}")
            self.GAs.append(0)
            self.figuras_triang.append(Figure(dpi=120))
            self.figuras_triang_detail.append(Figure(dpi=120))
        
    def gerar_widgets(self):
        '''
        Gera todos os widgets dos gráficos que serão colocados nas telas
        '''

        for indice in range(len(self.matrizes)):
            graph_widget = GraphicsWidget()
            graph_widget.setup()
            
            graph_widget.label.setText("%1.6f" % self.GAs[indice])
            
            # Usa figuras de visão geral para a primeira aba
            widget_vector = FigureWidget(self.figuras_vet[indice])
            widget_vector.setObjectName("widget_vector")
            widget_vector.setParent(graph_widget.groupBox)

            widget_delaunay = FigureWidget(self.figuras_triang[indice])
            widget_delaunay.setObjectName("widget_delaunay")
            widget_delaunay.setParent(graph_widget.groupBox_2)

            
            graph_widget.gridLayout_3.addWidget(widget_vector, 0, 0, 1, 1)
            graph_widget.gridLayout_4.addWidget(widget_delaunay, 0, 0, 1, 1)
            
            vect_widget = DetailWidget()
            vect_widget.setup()
            
            # Usa figuras de detalhe para a aba de vetores detalhada
            widget_vector_tab = FigureWidget(self.figuras_vet_detail[indice])
            widget_vector_tab.setObjectName("widget_vector_tab")
            widget_vector_tab.setParent(vect_widget.groupBox)
            vect_widget.gridLayout_1.addWidget(widget_vector_tab, 0, 0, 1, 1)
            
            navbar_vetor = Navbar(widget_vector_tab, self.ui.ui.centralwidget)
            vect_widget.gridLayout_2.addWidget(navbar_vetor, 0, 0, 1, 1)
            
            trian_widget = DetailWidget()
            trian_widget.setup()
            
            # Usa figuras de detalhe para a aba de triangulação detalhada
            widget_delaunay_tab = FigureWidget(self.figuras_triang_detail[indice])
            widget_delaunay_tab.setObjectName("widget_delaunay_tab")
            widget_delaunay_tab.setParent(trian_widget.groupBox)
            trian_widget.gridLayout_1.addWidget(widget_delaunay_tab, 0, 0, 1, 1)
            
            navbar_delaunay = Navbar(widget_delaunay_tab, self.ui.ui.centralwidget)
            trian_widget.gridLayout_2.addWidget(navbar_delaunay, 0, 0, 1, 1)
        
            widget_gpa_ev = FigureWidget(self.figuras_GA[indice])
            widget_gpa_ev.setObjectName("widget_gpa_ev")
            widget_gpa_ev.setParent(self.ui.ui.GPAGraphGroup)
            
            self.ui.ui.stackedGraphics.addWidget(graph_widget)
            self.ui.ui.stackedVet.addWidget(vect_widget)
            self.ui.ui.stackedTriang.addWidget(trian_widget)
            self.ui.ui.stackedGPA.addWidget(widget_gpa_ev)
            
        self.ui.ui.horizontalSlider.setMaximum(len(self.matrizes) - 1)
        self.ui.ui.horizontalSlider.setSingleStep(1)
        self.ui.ui.horizontalSlider.setPageStep(1)
            
#Se for executado standalone
if __name__ == '__main__':
    AnaliseCtrl()
