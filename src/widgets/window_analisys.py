# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Nov  4 21:44:16 2012
#      by: PyQt5 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtGui, QtWidgets

class AnalysisWindow:
    def setup(self, main_window):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setObjectName("Tabs")
        self.graphicPage1 = QtWidgets.QWidget()
        self.graphicPage1.setObjectName("graphicPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graphicPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedGraphics = QtWidgets.QStackedWidget(self.graphicPage1)
        self.stackedGraphics.setObjectName("stackedGraphics")
        
        self.gridLayout_3.addWidget(self.stackedGraphics, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.Tabs.addTab(self.graphicPage1, "")
        self.vectorTab = QtWidgets.QWidget()
        self.vectorTab.setObjectName("vectorTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.vectorTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedVet = QtWidgets.QStackedWidget(self.vectorTab)
        self.stackedVet.setObjectName("stackedVet")
        
        self.gridLayout_6.addWidget(self.stackedVet, 0, 0, 1, 1)
        self.Tabs.addTab(self.vectorTab, "")
        self.delaunayTab = QtWidgets.QWidget()
        self.delaunayTab.setObjectName("delaunayTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.delaunayTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedTriang = QtWidgets.QStackedWidget(self.delaunayTab)
        self.stackedTriang.setObjectName("stackedTriang")
        
        self.gridLayout_7.addWidget(self.stackedTriang, 0, 0, 1, 1)
        self.Tabs.addTab(self.delaunayTab, "")
        self.gpaTab = QtWidgets.QWidget()
        self.gpaTab.setObjectName("gpaTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gpaTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.GPAGraphGroup = QtWidgets.QGroupBox(self.gpaTab)
        self.GPAGraphGroup.setObjectName("GPAGraphGroup")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.GPAGraphGroup)
        self.gridLayout_10.setObjectName("gridLayout_10")
        
        self.stackedGPA = QtWidgets.QStackedWidget(self.gpaTab)
        self.stackedGPA.setObjectName('stackedGPA')
        self.gridLayout_10.addWidget(self.stackedGPA, 0, 0, 1, 1)
        
        self.gridLayout_8.addWidget(self.GPAGraphGroup, 0, 0, 1, 1)
        self.Tabs.addTab(self.gpaTab, "")
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        self.controGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.controGroup.setFlat(False)
        self.controGroup.setObjectName("controGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.controGroup)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.controGroup, 1, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Arquivo = QtWidgets.QMenu(self.menubar)
        self.menu_Arquivo.setObjectName("menu_Arquivo")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(main_window)
        self.toolBar.setObjectName("toolBar")
        main_window.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionAbrir_Conjunto_de_Matrizes = QtGui.QAction(main_window)
        self.actionAbrir_Conjunto_de_Matrizes.setObjectName("actionAbrir_Conjunto_de_Matrizes")
        self.menu_Arquivo.addAction(self.actionAbrir_Conjunto_de_Matrizes)
        self.menubar.addAction(self.menu_Arquivo.menuAction())

        self.retranslateUi(main_window)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, mw):
        mw.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "PyGPA 2.0 - Análise"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.graphicPage1), QtCore.QCoreApplication.translate("MainWindow", "Gráficos"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.vectorTab), QtCore.QCoreApplication.translate("MainWindow", "Campo Vetorial"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.delaunayTab), QtCore.QCoreApplication.translate("MainWindow", "Triangulação de Delaunay"))
        self.GPAGraphGroup.setTitle(QtCore.QCoreApplication.translate("MainWindow", "Gráfico"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.gpaTab), QtCore.QCoreApplication.translate("MainWindow", "Evolução do GPA"))
        self.controGroup.setTitle(QtCore.QCoreApplication.translate("MainWindow", "Controle"))
        self.menu_Arquivo.setTitle(QtCore.QCoreApplication.translate("MainWindow", "&Arquivo"))
        self.toolBar.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "toolBar"))
        self.actionAbrir_Conjunto_de_Matrizes.setText(QtCore.QCoreApplication.translate("MainWindow", "Abrir Conjunto de Matrizes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AnalysisWindow()
    mw = QtWidgets.QMainWindow()
    ui.setup(mw)
    mw.show()
    sys.exit(app.exec())

