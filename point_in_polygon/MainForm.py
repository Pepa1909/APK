# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *
import sys
import geopandas as gpd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 708)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(parent=self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/pointpol.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon3)
        self.actionClear.setObjectName("actionClear")
        self.actionRay_Crossing_Algorithm = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/ray.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRay_Crossing_Algorithm.setIcon(icon4)
        self.actionRay_Crossing_Algorithm.setObjectName("actionRay_Crossing_Algorithm")
        self.actionWinding_Number_Algorithm = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/winding.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWinding_Number_Algorithm.setIcon(icon5)
        self.actionWinding_Number_Algorithm.setObjectName("actionWinding_Number_Algorithm")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addSeparator()
        self.menuInput.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRay_Crossing_Algorithm)
        self.menuAnalyze.addAction(self.actionWinding_Number_Algorithm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRay_Crossing_Algorithm)
        self.toolBar.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        
        self.actionOpen.triggered.connect(self.openClick) # type: ignore
        self.actionClear.triggered.connect(self.clearClick) # type: ignore
        self.actionRay_Crossing_Algorithm.triggered.connect(self.rayCrossingClick) # type: ignore
        self.actionWinding_Number_Algorithm.triggered.connect(self.windingNumberClick) # type: ignore
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def openClick(self):
        
        #Open file
        data = self.openFile()
        
        #If no file selected, return
        if data is None:
            return
        
        #Clear canvas for new polygon layer
        self.Canvas.clearData()
        
        #Try to load and process the data
        correct_data = self.Canvas.loadData(data)
        
        #Alert the user if Shapefile is invalid
        if correct_data == False:
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Error Message")
            dlg.setText("Invalid Shapefile")
            dlg.exec()
            return
    
    def openFile(self):
        
        #Opens Shapefile
        filename, _ = QFileDialog.getOpenFileName(caption="Open File", directory="input_files/.", filter="Shapefile (*.shp)")
        
        #Return if no file has been opened
        if filename == "":
            return None
        
        #Return data from shapefile
        with open(filename, "r", encoding="utf-8") as f:
            data = gpd.read_file(filename)
            return(data)

        
    def clearClick(self):
        
        #Clear data
        self.Canvas.clearData()
        
        
    def rayCrossingClick(self):
        
        #Get data
        q = self.Canvas.getQ()
        mmb_list = self.Canvas.getMmb()
        polyg_list = self.Canvas.getPol()
        
        #Iterate over each min-max box
        for i in range(len(mmb_list)):
            # Store the value of the result and assign it to the polygon
            result = Algorithms.rayCrossingAlgorithm(self, q, mmb_list[i])
            self.Canvas.polyg_status[i] = result
        
        #Iterate over each polygon, that passed the min-max box test
        for i in range(len(polyg_list)):
            if self.Canvas.polyg_status[i] == 1 or self.Canvas.polyg_status[i] == -1:
                res = Algorithms.rayCrossingAlgorithm(self, q, polyg_list[i])
                self.Canvas.polyg_status[i] = res

        #Show results
        mb = QtWidgets.QMessageBox()
        mb.setWindowTitle('Analyze point and polygon position')

        #Point q inside polygon
        for i in self.Canvas.polyg_status:
            if i == 1:
                mb.setText("Point inside polygon")
                break
            
            #Point q on edge of polygon
            elif i == -1:
                mb.setText("Point on edge of polygons")
                break
        
            #Point q outside of polygon     
            elif i == 0:
                mb.setText("Point outside polygon")
                
        #Show window
        mb.exec()
        
        
    def windingNumberClick(self):
        
        #Get data
        q = self.Canvas.getQ()
        mmb_list = self.Canvas.getMmb()
        polyg_list = self.Canvas.getPol()
        
        #Iterate over each min-max box
        for i in range(len(mmb_list)):
            # Store the value of the result and assign it to the polygon
            result = Algorithms.windingNumberAlgorithm(self, q, mmb_list[i])
            self.Canvas.polyg_status[i] = result
        
        #Iterate over each polygon, that passed the min-max box test    
        for i in range(len(polyg_list)):
            if self.Canvas.polyg_status[i] == 1 or self.Canvas.polyg_status[i] == -1:
                res = Algorithms.windingNumberAlgorithm(self, q, polyg_list[i])
                self.Canvas.polyg_status[i] = res
        
        #Show results
        mb = QtWidgets.QMessageBox()
        mb.setWindowTitle('Analyze point and polygon position')
        
        #Point q inside polygon
        for i in self.Canvas.polyg_status:
            if i == 1:
                mb.setText("Point inside polygon")
                break
            
            #Point q on edge of polygon
            elif i == -1:
                mb.setText("Point on edge of polygons")
                break
            
            #Point q outside polygon     
            elif i == 0:
                mb.setText("Point outside polygon")
            
        #Show window
        mb.exec()
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear data"))
        self.actionRay_Crossing_Algorithm.setText(_translate("MainWindow", "Ray Crossing Algorithm"))
        self.actionWinding_Number_Algorithm.setText(_translate("MainWindow", "Winding Number Algorithm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())