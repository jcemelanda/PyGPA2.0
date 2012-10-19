# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Jul 19 09:36:32 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureWidget
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as Navbar
from matplotlib.figure import Figure
from PyQt4 import QtCore, QtGui
from about import ui_sobre
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ui_analise(object):
    '''
    class ui_analise
    
    Classe que define a interfacegráfica do programa PyGPA
    
    Métodos:
        setup_ui -> None
        retranslate_ui -> None
    '''
    def __init__(self, controle):
        self.controle = controle


    def setup_ui(self, janela_principal):
        '''
        setup_ui -> None
        
        Configura a interface gráfica, seus elementos e faz a ligação entre
        elementos gráficos e métodos do controle.
        '''
        
        janela_principal.setObjectName(_fromUtf8("janela_principal"))
        janela_principal.setWindowModality(QtCore.Qt.ApplicationModal)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/icon.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela_principal.setWindowIcon(icon)
        
        self.widget_central = QtGui.QWidget(janela_principal)
        self.widget_central.setObjectName(_fromUtf8("widget_central"))
        self.gridLayout = QtGui.QGridLayout(self.widget_central)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tabs = QtGui.QTabWidget(self.widget_central)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        
        self.graphicPage1 = QtGui.QWidget()
        self.graphicPage1.setObjectName(_fromUtf8("graphicPage1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.graphicPage1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.GPAGrid = QtGui.QGridLayout()
        self.GPAGrid.setObjectName(_fromUtf8("GPAGrid"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.GPAGrid.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.GPAGrid.addItem(spacerItem1, 0, 0, 1, 1)
        self.GPAGroup = QtGui.QGroupBox(self.graphicPage1)
        self.GPAGroup.setObjectName(_fromUtf8("GPAGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.GPAGroup)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.GPALabel = QtGui.QLabel(self.GPAGroup)
        self.GPALabel.setObjectName(_fromUtf8("GPALabel"))
        self.gridLayout_5.addWidget(self.GPALabel, 0, 0, 1, 1)
        self.GPAGrid.addWidget(self.GPAGroup, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.GPAGrid, 1, 2, 1, 1)
        
        self.delaunayGroup = QtGui.QGroupBox(self.graphicPage1)
        self.delaunayGroup.setObjectName(_fromUtf8("delaunayGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.delaunayGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        
        self.gridLayout_3.addWidget(self.delaunayGroup, 1, 1, 1, 1)
        self.vetfieldGroup = QtGui.QGroupBox(self.graphicPage1)
        self.vetfieldGroup.setObjectName(_fromUtf8("vetfieldGroup"))
        self.gridLayout_9 = QtGui.QGridLayout(self.vetfieldGroup)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        
        self.gridLayout_3.addWidget(self.vetfieldGroup, 1, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.gridLayout_3.setColumnStretch(1, 8)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.Tabs.addTab(self.graphicPage1, _fromUtf8(""))
        self.vectorTab = QtGui.QWidget()
        self.vectorTab.setObjectName(_fromUtf8("vectorTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.vectorTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.vetGroupTab = QtGui.QGroupBox(self.vectorTab)
        self.vetGroupTab.setObjectName(_fromUtf8("vetGroupTab"))
        self.gridLayout_12 = QtGui.QGridLayout(self.vetGroupTab)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        
        self.gridLayout_6.addWidget(self.vetGroupTab, 0, 0, 1, 1)
        self.toolGroupVet = QtGui.QGroupBox(self.vectorTab)
        self.toolGroupVet.setObjectName(_fromUtf8("toolGroupVet"))
        self.gridLayout_13 = QtGui.QGridLayout(self.toolGroupVet)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_6.addWidget(self.toolGroupVet, 1, 0, 1, 1)
        self.gridLayout_6.setRowStretch(0, 5)
        self.gridLayout_6.setRowStretch(1, 1)
        self.Tabs.addTab(self.vectorTab, _fromUtf8(""))
        self.delaunayTab = QtGui.QWidget()
        self.delaunayTab.setObjectName(_fromUtf8("delaunayTab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.delaunayTab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.delaunayGroupTab = QtGui.QGroupBox(self.delaunayTab)
        self.delaunayGroupTab.setObjectName(_fromUtf8("delaunayGroupTab"))
        self.gridLayout_11 = QtGui.QGridLayout(self.delaunayGroupTab)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        
        self.gridLayout_7.addWidget(self.delaunayGroupTab, 0, 0, 1, 1)
        self.toolGroupDelaunay = QtGui.QGroupBox(self.delaunayTab)
        self.toolGroupDelaunay.setObjectName(_fromUtf8("toolGroupDelaunay"))
        self.gridLayout_14 = QtGui.QGridLayout(self.toolGroupDelaunay)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.gridLayout_7.addWidget(self.toolGroupDelaunay, 1, 0, 1, 1)
        self.gridLayout_7.setRowStretch(0, 5)
        self.gridLayout_7.setRowStretch(1, 1)
        self.Tabs.addTab(self.delaunayTab, _fromUtf8(""))
        self.gpaTab = QtGui.QWidget()
        self.gpaTab.setObjectName(_fromUtf8("gpaTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gpaTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.GPAGraphGroup = QtGui.QGroupBox(self.gpaTab)
        self.GPAGraphGroup.setObjectName(_fromUtf8("GPAGraphGroup"))
        self.gridLayout_10 = QtGui.QGridLayout(self.GPAGraphGroup)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        
        self.gridLayout_8.addWidget(self.GPAGraphGroup, 0, 0, 1, 1)
        self.Tabs.addTab(self.gpaTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        self.controGroup = QtGui.QGroupBox(self.widget_central)
        self.controGroup.setFlat(False)
        self.controGroup.setObjectName(_fromUtf8("controGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.controGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalSlider = QtGui.QSlider(self.controGroup)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.controGroup, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 1)
        janela_principal.setCentralWidget(self.widget_central)
        self.menubar = QtGui.QMenuBar(janela_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Arquivo = QtGui.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName(_fromUtf8("menu_Arquivo"))
        janela_principal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(janela_principal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        janela_principal.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(janela_principal)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        janela_principal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir_Conjunto_de_Matrizes = QtGui.QAction(janela_principal)
        self.actionAbrir_Conjunto_de_Matrizes.setObjectName(_fromUtf8("actionAbrir_Conjunto_de_Matrizes"))
        self.menu_Arquivo.addAction(self.actionAbrir_Conjunto_de_Matrizes)
        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.shortcut_right = QtGui.QShortcut(QtGui.QKeySequence("l"), janela_principal, self.controle.incrementa_view)
        self.shortcut_right = QtGui.QShortcut(QtGui.QKeySequence("j"), janela_principal, self.controle.decrementa_view)
        self.shortcut_right = QtGui.QShortcut(QtGui.QKeySequence("end"), janela_principal, self.controle.last_view)
        self.shortcut_right = QtGui.QShortcut(QtGui.QKeySequence("home"), janela_principal, self.controle.first_view)

        self.retranslateUi(janela_principal)
        QtCore.QObject.connect(self.actionAbrir_Conjunto_de_Matrizes, QtCore.SIGNAL(
                                    'triggered()'), self.controle.abrir_arquivo)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.controle.recarrega_dados)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(janela_principal)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA-2.0 - Análise", None, QtGui.QApplication.UnicodeUTF8))
        self.GPAGroup.setTitle(QtGui.QApplication.translate("MainWindow", "GPA", None, QtGui.QApplication.UnicodeUTF8))
        self.GPALabel.setText(QtGui.QApplication.translate("MainWindow", "0,778", None, QtGui.QApplication.UnicodeUTF8))
        self.delaunayGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Triangulação de Delaunay", None, QtGui.QApplication.UnicodeUTF8))
        self.vetfieldGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Campo Vetorial", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.graphicPage1), QtGui.QApplication.translate("MainWindow", "Gráficos", None, QtGui.QApplication.UnicodeUTF8))
        self.vetGroupTab.setTitle(QtGui.QApplication.translate("MainWindow", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.toolGroupVet.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.vectorTab), QtGui.QApplication.translate("MainWindow", "Campo Vetorial", None, QtGui.QApplication.UnicodeUTF8))
        self.delaunayGroupTab.setTitle(QtGui.QApplication.translate("MainWindow", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.toolGroupDelaunay.setTitle(QtGui.QApplication.translate("MainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.delaunayTab), QtGui.QApplication.translate("MainWindow", "Triangulação de Delaunay", None, QtGui.QApplication.UnicodeUTF8))
        self.GPAGraphGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.gpaTab), QtGui.QApplication.translate("MainWindow", "Evolução do GPA", None, QtGui.QApplication.UnicodeUTF8))
        self.controGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Controle", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Arquivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir_Conjunto_de_Matrizes.setText(QtGui.QApplication.translate("MainWindow", "Abrir Conjunto de Matrizes", None, QtGui.QApplication.UnicodeUTF8))

    def mostrar_sobre(self):
        sobre = QtGui.QDialog(self.janela)
        ui = ui_sobre()
        pix = QtGui.QPixmap(_fromUtf8("icons/icon.png"))
        text = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'\
'<html><head><meta name="qrichtext" content="1" /><style type="text/css">'\
'p, li { white-space: pre-wrap; }'\
'</style></head><body style=" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;">'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">PyGPA</span></p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Versão 0.2</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Copyleft Julio Cesar Eiras Melanda, 2011</p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Este software é distribuído sob a GPL v3.</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">http://www.gnu.org/licenses/gpl-3.0.txt</p>'\
'<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Para mais informações acesse a página do projeto</p>'\
'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000;"> </span><span style=" color:#000000;">http://gitorious.org/pygpa/pages/Home</span></a></p></body></html>'
        ui.setup_ui(sobre, pix, text)
        sobre.show()
