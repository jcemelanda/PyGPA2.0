# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Nov  4 21:44:16 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Analysis_Window:
    def setup(self, main_window):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.graphicPage1 = QtWidgets.QWidget()
        self.graphicPage1.setObjectName(_fromUtf8("graphicPage1"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graphicPage1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.stackedGraphics = QtWidgets.QStackedWidget(self.graphicPage1)
        self.stackedGraphics.setObjectName(_fromUtf8("stackedGraphics"))
        
        self.gridLayout_3.addWidget(self.stackedGraphics, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.Tabs.addTab(self.graphicPage1, _fromUtf8(""))
        self.vectorTab = QtWidgets.QWidget()
        self.vectorTab.setObjectName(_fromUtf8("vectorTab"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.vectorTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.stackedVet = QtWidgets.QStackedWidget(self.vectorTab)
        self.stackedVet.setObjectName(_fromUtf8("stackedVet"))
        
        self.gridLayout_6.addWidget(self.stackedVet, 0, 0, 1, 1)
        self.Tabs.addTab(self.vectorTab, _fromUtf8(""))
        self.delaunayTab = QtWidgets.QWidget()
        self.delaunayTab.setObjectName(_fromUtf8("delaunayTab"))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.delaunayTab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.stackedTriang = QtWidgets.QStackedWidget(self.delaunayTab)
        self.stackedTriang.setObjectName(_fromUtf8("stackedTriang"))
        
        self.gridLayout_7.addWidget(self.stackedTriang, 0, 0, 1, 1)
        self.Tabs.addTab(self.delaunayTab, _fromUtf8(""))
        self.gpaTab = QtWidgets.QWidget()
        self.gpaTab.setObjectName(_fromUtf8("gpaTab"))
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gpaTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.GPAGraphGroup = QtWidgets.QGroupBox(self.gpaTab)
        self.GPAGraphGroup.setObjectName(_fromUtf8("GPAGraphGroup"))
        self.gridLayout_10 = QtWidgets.QGridLayout(self.GPAGraphGroup)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        
        self.stackedGPA = QtWidgets.QStackedWidget(self.gpaTab)
        self.stackedGPA.setObjectName(_fromUtf8('stackedGPA'))
        self.gridLayout_10.addWidget(self.stackedGPA, 0, 0, 1, 1)
        
        self.gridLayout_8.addWidget(self.GPAGraphGroup, 0, 0, 1, 1)
        self.Tabs.addTab(self.gpaTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        self.controGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.controGroup.setFlat(False)
        self.controGroup.setObjectName(_fromUtf8("controGroup"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalSlider = QtWidgets.QSlider(self.controGroup)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.controGroup, 1, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName(_fromUtf8("menu_Arquivo"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(main_window)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir_Conjunto_de_Matrizes = QtWidgets.QAction(main_window)
        self.actionAbrir_Conjunto_de_Matrizes.setObjectName(_fromUtf8("actionAbrir_Conjunto_de_Matrizes"))
        self.menu_Arquivo.addAction(self.actionAbrir_Conjunto_de_Matrizes)
        self.menubar.addAction(self.menu_Arquivo.menuAction())

        self.retranslateUi(main_window)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, mw):
        mw.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PyGPA 2.0 - Análise"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.graphicPage1), QtWidgets.QApplication.translate("MainWindow", "Gráficos"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.vectorTab), QtWidgets.QApplication.translate("MainWindow", "Campo Vetorial"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.delaunayTab), QtWidgets.QApplication.translate("MainWindow", "Triangulação de Delaunay"))
        self.GPAGraphGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Gráfico"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.gpaTab), QtWidgets.QApplication.translate("MainWindow", "Evolução do GPA"))
        self.controGroup.setTitle(QtWidgets.QApplication.translate("MainWindow", "Controle"))
        self.menu_Arquivo.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Arquivo"))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar"))
        self.actionAbrir_Conjunto_de_Matrizes.setText(QtWidgets.QApplication.translate("MainWindow", "Abrir Conjunto de Matrizes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui =Analysis_Window()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())

