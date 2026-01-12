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
from view.view_analisys import Analise_View
from widgets.widget_detail import Detail_widget
from widgets.widget_graphs import Grafics_widget

# PIL
from PIL import Image

# Standard Library
import time


class Analise_Ctrl:
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
        self.ui = Analise_View(self)
        self.ui.showMaximized()
        self.matrizes = mat
        self.figuras_vet = []
        self.GAs = []
        self.figuras_triang = []
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
        Muda o conjunto de dados sendo exibido para o próximo da ‭lista
        '''
        
        self.pos += 1
        if self.current_tab == 0:
            self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        elif self.current_tab == 1:
            self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        elif self.current_tab == 2:
            self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        else:
            self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        time.sleep(.10)
    
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
        Muda o conjunto de dados sendo exibido para o anterior da ‭lista
        '''
        
        self.pos -= 1
        if self.current_tab == 0:
            self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        elif self.current_tab == 1:
            self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        elif self.current_tab == 2:
            self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        else:
            self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        time.sleep(.10)
                
    def last_view(self):
        '''
        Muda a exibição para o último conjunto da ‭lista
        '''

        self.pos = self.ui.ui.stackedGraphics.count() - 1
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.setValue(self.pos)
    
    def first_view(self):
        '''
        Muda a exibição para o prieiro conjunto da ‭lista
        '''

        self.pos = 0
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        time.sleep(.10)
                
    def set_view(self, pos):
        '''
        Ajusta a posição da ‭lista de dados para a posição passada como
        parâmetro
        params:
            pos -> int
                Posição da ‭lista que será exibida
        '''
        
        self.pos = pos
        self.ui.ui.stackedGraphics.setCurrentIndex(self.pos)
        self.ui.ui.stackedVet.setCurrentIndex(self.pos)
        self.ui.ui.stackedTriang.setCurrentIndex(self.pos)
        self.ui.ui.stackedGPA.setCurrentIndex(self.pos)
        self.ui.ui.horizontalSlider.setValue(self.pos)
        time.sleep(.10)
                
    def abrir_arquivo(self):
        '''
        Abre um arquivo contendo uma matriz bidimensional de dados ou uma 
        imagem e gera a matriz de dados interna do programa
        '''
        
        self.figuras_vet = []
        self.figuras_triang = []
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
            axes = self.figuras_GA[-1].add_subplot(111)
            axes.plot(range(len(self.GAs)), self.GAs)
            axes.plot(i, self.GAs[i], 'ro')
            
    def get_dx(self):
        '''
        Gera uma matriz com as derivadas parciais em x para a matriz de
        dados lida
        return:
            mat -> list
                lista que contém as matrizes de derivadas parciais em x
        '''
        
        if self.ABERTURA == 'normal':
            dx = []
            dlg = QtWidgets.QProgressDialog(u'Calculando dx', u'Cancelar',
                                        0, len(self.matriz[:-1]))
            dlg.setModal(True)
            dlg.setMinimumDuration(0)
            dlg.setAutoClose(True)
            dlg.setWindowTitle(u'Cálculo da derivada')
            dlg.show()
            a = 0

            for linha in self.matriz[:]:
                linha_dx = []
                for i in range(len(linha)):
                    if i == 0:
                        linha_dx.append(
                                (-3 * linha[0] + 4 * linha[1] - linha[2]) / 2.0)
                    elif i == len(linha) - 1:
                        linha_dx.append(
                            (3 * linha[-1] - 4 * linha[-2] + linha[-3]) / 2.0)
                    else:
                        linha_dx.append((linha[i + 1] - linha[i - 1]) / 2.0)
                dx.append(linha_dx)
                dlg.setValue(a)
                a += 1
                dlg.close()
            return dx
        else:
            mat = []
            for l in self.matriz[:]:
                mat.append(list(next(zip(*l))))
            return mat
                
    def get_dy(self):
        '''
        Gera uma matriz com as derivadas parciais em y para a matriz de
        dados lida
        return:
            mat -> list
                lista que contém as matrizes de derivadas parciais em x
        '''
        if self.ABERTURA == 'normal':
            dy = []
            dlg = QtWidgets.QProgressDialog(u'Calculando dy', u'Cancelar',
                                        0, len(self.matriz[:-1]))
            dlg.setModal(True)
            dlg.setMinimumDuration(0)
            dlg.setAutoClose(True)
            dlg.setWindowTitle(u'Cálculo da derivada')
            dlg.show()
            a = 0
            for linha in zip(*self.matriz[:]):
                linha_dy = []
                for i in range(len(linha)):
                    if i == 0:
                        linha_dy.append(
                                        (-3 * linha[0] + 4 * linha[1] - linha[2]) / 2.0)
                    elif i == len(linha) - 1:
                        linha_dy.append(
                                        (3 * linha[-1] - 4 * linha[-2] + linha[-3]) / 2.0)
                    else:
                        linha_dy.append((linha[i + 1] - linha[i - 1]) / 2.0)
                dy.append(linha_dy)
                dlg.setValue(a)
                a += 1
                if dlg.wasCanceled():
                    return
            dlg.close()
            return list(zip(*dy))
        else:
            mat = []
            for l in self.matriz[:]:
                mat.append(list(list(zip(*l))[1]))
            return mat
        
    def normaliza_derivadas(self):
        '''
        Normaliza as derivadas em função do maior valor que se tornará 1
        Todos os valores passam a ter norma entre 0 e 1 inclusive
        '''
        if self.normalizado:
            return

        maximo = 0.0

        for linha in self.dx:
            m = max([abs(l) for l in linha])
            if m > maximo:
                maximo = m
        for linha in self.dy:
            m = max([abs(l) for l in linha])
            if m > maximo:
                maximo = m
        self.dx = [[d / maximo for d in linha] for linha in self.dx]
        self.dy = [[d / maximo for d in linha] for linha in self.dy]
      
    def gerar_vetores(self):
        '''
        Gera o campo de gradientes do conjunto de dados a partir das derivadas 
        parciais em x e y de cada elemento do conjunto
        '''
        self.dx = self.get_dx()
        self.dy = self.get_dy()

        self.normaliza_derivadas()
        self.anular()

        minx = -1
        maxx = round(max(list(zip(*self.dx))[-1]))
        miny = -1
        maxy = round(max(self.dy[-1]))

        self.figuras_vet.append(Figure(dpi=120))
        axes = self.figuras_vet[-1].add_subplot(111, aspect='equal')
        q = axes.quiver(self.dx, self.dy, angles='xy', scale=1.0,
                                scale_units='xy', minshaft=2, minlength=1)
        axes.quiverkey(q, 0, miny - 2, 1, '', coordinates='data')
        axes.set_xlim(minx, len(self.dx[0]) + maxx)
        axes.set_ylim(miny, len(self.dx) + maxy)
        
    def anular(self):
        '''
        Coloca norma zero para os pares de vetores que se anulam.
        '''
        vects = [list(zip(x, y)) for x, y in zip(self.dx, self.dy)]

        dlg = QtWidgets.QProgressDialog(u'Otimizando campo', u'Cancelar',
                                    0, len(vects))
        dlg.setModal(True)
        dlg.setMinimumDuration(0)
        dlg.setAutoClose(True)
        dlg.setWindowTitle(u'Eliminar vetores')
        dlg.show()
        for i in range(len(vects)):
            for j in range(len(vects[0])):
                for k in range(i, len(vects)):
                    for w in range(len(vects[0])):
                        a = vects[i][j]
                        b = vects[k][w]
                        if a == (0, 0):
                            break
                        if (a[0] == -b[0]) and (a[1] == -b[1]):
                                vects[i][j] = vects[k][w] = (0, 0)
                                break
            dlg.setValue(i)
            if dlg.wasCanceled():
                return
        dlg.close()
        dlg.destroy
        v = [list(zip(*l)) for l in vects]
        self.dx, self.dy = zip(*v)
        
    def gerar_triangulacao(self):
        '''
        Gera a triangulação de Delaunay para o conjunto de dados,
        plota os triângulos e exibe o número de arestas encontradas
        '''
        vects = [list(zip(x, y)) for x, y in zip(self.dx, self.dy)]
        points = []
        for i in range(len(vects)):
            line = []
            for j in range(len(vects[0])):
                x, y = vects[i][j]
                if (abs(x) > 0.0) or (abs(y) > 0.0):
                    if [x + j, y + i] not in points:
                        line.append([x + j, y + i])
            points += line

        x, y = zip(*points)
        t = tri.Triangulation(x, y)
        self.figuras_triang.append(Figure(dpi=120))
        axes = self.figuras_triang[-1].add_subplot(111, aspect='equal')
        minx = round(min(list(zip(*self.dx))[0])) - 1
        maxx = round(max(list(zip(*self.dx))[-1]))
        miny = round(min(self.dy[0])) - 1
        maxy = round(max(self.dy[-1]))
        if miny >= 0:
            miny = -1
        if minx >= 0:
            minx = -1
        axes.set_xlim(minx, len(self.dx[0]) + maxx)
        axes.set_ylim(miny, len(self.dx) + maxy)
        axes.triplot(t)

        self.GAs.append((len(t.edges) - len(x)) / len(x))
        
    def gerar_widgets(self):
        '''
        Gera todos os widgets dos gráficos que serão colocados nas telas
        '''

        for indice in range(len(self.matrizes)):
            graph_widget = Grafics_widget()
            graph_widget.setup()
            
            graph_widget.label.setText("%1.6f" % self.GAs[indice])
            
            widget_vector = FigureWidget(self.figuras_vet[indice])
            widget_vector.setObjectName("widget_vector")
            widget_vector.setParent(graph_widget.groupBox)

            widget_delaunay = FigureWidget(self.figuras_triang[indice])
            widget_delaunay.setObjectName("widget_delaunay")
            widget_delaunay.setParent(graph_widget.groupBox_2)

            
            graph_widget.gridLayout_3.addWidget(widget_vector, 0, 0, 1, 1)
            graph_widget.gridLayout_4.addWidget(widget_delaunay, 0, 0, 1, 1)
            
            vect_widget = Detail_widget()
            vect_widget.setup()
            
            widget_vector_tab = FigureWidget(self.figuras_vet[indice])
            widget_vector_tab.setObjectName("widget_vector_tab")
            widget_vector_tab.setParent(vect_widget.groupBox)
            vect_widget.gridLayout_1.addWidget(widget_vector_tab, 0, 0, 1, 1)
            
            navbar_vetor = Navbar(widget_vector_tab, self.ui.ui.centralwidget)
            vect_widget.gridLayout_2.addWidget(navbar_vetor, 0, 0, 1, 1)
            
            trian_widget = Detail_widget()
            trian_widget.setup()
            
            widget_delaunay_tab = FigureWidget(self.figuras_triang[indice])
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
    Analise_Ctrl()
