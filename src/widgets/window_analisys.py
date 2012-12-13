# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Nov  4 21:44:16 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Analysis_Window:
    def setup(self, main_window):
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tabs = QtGui.QTabWidget(self.centralwidget)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.graphicPage1 = QtGui.QWidget()
        self.graphicPage1.setObjectName(_fromUtf8("graphicPage1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.graphicPage1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.stackedGraphics = QtGui.QStackedWidget(self.graphicPage1)
        self.stackedGraphics.setObjectName(_fromUtf8("stackedGraphics"))
        
        self.gridLayout_3.addWidget(self.stackedGraphics, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.Tabs.addTab(self.graphicPage1, _fromUtf8(""))
        self.vectorTab = QtGui.QWidget()
        self.vectorTab.setObjectName(_fromUtf8("vectorTab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.vectorTab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.stackedVet = QtGui.QStackedWidget(self.vectorTab)
        self.stackedVet.setObjectName(_fromUtf8("stackedVet"))
        
        self.gridLayout_6.addWidget(self.stackedVet, 0, 0, 1, 1)
        self.Tabs.addTab(self.vectorTab, _fromUtf8(""))
        self.delaunayTab = QtGui.QWidget()
        self.delaunayTab.setObjectName(_fromUtf8("delaunayTab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.delaunayTab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.stackedTriang = QtGui.QStackedWidget(self.delaunayTab)
        self.stackedTriang.setObjectName(_fromUtf8("stackedTriang"))
        
        self.gridLayout_7.addWidget(self.stackedTriang, 0, 0, 1, 1)
        self.Tabs.addTab(self.delaunayTab, _fromUtf8(""))
        self.gpaTab = QtGui.QWidget()
        self.gpaTab.setObjectName(_fromUtf8("gpaTab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gpaTab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.GPAGraphGroup = QtGui.QGroupBox(self.gpaTab)
        self.GPAGraphGroup.setObjectName(_fromUtf8("GPAGraphGroup"))
        self.gridLayout_10 = QtGui.QGridLayout(self.GPAGraphGroup)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        
        self.stackedGPA = QtGui.QStackedWidget(self.gpaTab)
        self.stackedGPA.setObjectName(_fromUtf8('stackedGPA'))
        self.gridLayout_10.addWidget(self.stackedGPA, 0, 0, 1, 1)
        
        self.gridLayout_8.addWidget(self.GPAGraphGroup, 0, 0, 1, 1)
        self.Tabs.addTab(self.gpaTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        self.controGroup = QtGui.QGroupBox(self.centralwidget)
        self.controGroup.setFlat(False)
        self.controGroup.setObjectName(_fromUtf8("controGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.controGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalSlider = QtGui.QSlider(self.controGroup)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.controGroup, 1, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Arquivo = QtGui.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName(_fromUtf8("menu_Arquivo"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(main_window)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir_Conjunto_de_Matrizes = QtGui.QAction(main_window)
        self.actionAbrir_Conjunto_de_Matrizes.setObjectName(_fromUtf8("actionAbrir_Conjunto_de_Matrizes"))
        self.menu_Arquivo.addAction(self.actionAbrir_Conjunto_de_Matrizes)
        self.menubar.addAction(self.menu_Arquivo.menuAction())

        self.retranslateUi(main_window)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, mw):
        mw.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGPA 2.0 - Análise", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.graphicPage1), QtGui.QApplication.translate("MainWindow", "Gráficos", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.vectorTab), QtGui.QApplication.translate("MainWindow", "Campo Vetorial", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.delaunayTab), QtGui.QApplication.translate("MainWindow", "Triangulação de Delaunay", None, QtGui.QApplication.UnicodeUTF8))
        self.GPAGraphGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.Tabs.setTabText(self.Tabs.indexOf(self.gpaTab), QtGui.QApplication.translate("MainWindow", "Evolução do GPA", None, QtGui.QApplication.UnicodeUTF8))
        self.controGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Controle", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Arquivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir_Conjunto_de_Matrizes.setText(QtGui.QApplication.translate("MainWindow", "Abrir Conjunto de Matrizes", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =Analysis_Window()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())

