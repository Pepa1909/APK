# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QWidget)

from draw import Draw
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 708)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/images/icons/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionPoint_Polygon = QAction(MainWindow)
        self.actionPoint_Polygon.setObjectName(u"actionPoint_Polygon")
        self.actionPoint_Polygon.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/pointpol.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPoint_Polygon.setIcon(icon2)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/clear_all.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon3)
        self.actionRay_Crossing_Algorithm = QAction(MainWindow)
        self.actionRay_Crossing_Algorithm.setObjectName(u"actionRay_Crossing_Algorithm")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/ray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRay_Crossing_Algorithm.setIcon(icon4)
        self.actionWinding_Number_Algorithm = QAction(MainWindow)
        self.actionWinding_Number_Algorithm.setObjectName(u"actionWinding_Number_Algorithm")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/winding.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionWinding_Number_Algorithm.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Canvas = Draw(self.centralwidget)
        self.Canvas.setObjectName(u"Canvas")

        self.horizontalLayout.addWidget(self.Canvas)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1095, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInput = QMenu(self.menubar)
        self.menuInput.setObjectName(u"menuInput")
        self.menuAnalyze = QMenu(self.menubar)
        self.menuAnalyze.setObjectName(u"menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addAction(self.actionPoint_Polygon)
        self.menuInput.addSeparator()
        self.menuInput.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRay_Crossing_Algorithm)
        self.menuAnalyze.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPoint_Polygon)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRay_Crossing_Algorithm)
        self.toolBar.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(MainWindow.close)
        self.actionPoint_Polygon.triggered.connect(MainWindow.close)
        self.actionClear.triggered.connect(MainWindow.close)
        self.actionRay_Crossing_Algorithm.triggered.connect(MainWindow.close)
        self.actionWinding_Number_Algorithm.triggered.connect(MainWindow.close)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Point and polygon position", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open file", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"Close application", None))
#endif // QT_CONFIG(tooltip)
        self.actionPoint_Polygon.setText(QCoreApplication.translate("MainWindow", u"Point/Polygon", None))
#if QT_CONFIG(tooltip)
        self.actionPoint_Polygon.setToolTip(QCoreApplication.translate("MainWindow", u"Input point/polygon vertex", None))
#endif // QT_CONFIG(tooltip)
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.actionClear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear data", None))
#endif // QT_CONFIG(tooltip)
        self.actionRay_Crossing_Algorithm.setText(QCoreApplication.translate("MainWindow", u"Ray Crossing Algorithm", None))
        self.actionWinding_Number_Algorithm.setText(QCoreApplication.translate("MainWindow", u"Winding Number Algorithm", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuInput.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.menuAnalyze.setTitle(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

