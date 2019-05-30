# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui',
# licensing of 'main_gui.ui' applies.
#
# Created: Mon May 27 17:14:16 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1161, 711))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.REGISTER = QtWidgets.QPushButton(self.tab)
        self.REGISTER.setGeometry(QtCore.QRect(30, 10, 141, 41))
        self.REGISTER.setCheckable(True)
        self.REGISTER.setObjectName("REGISTER")
        self.ADD_PROG = QtWidgets.QPushButton(self.tab)
        self.ADD_PROG.setGeometry(QtCore.QRect(30, 70, 141, 41))
        self.ADD_PROG.setCheckable(True)
        self.ADD_PROG.setObjectName("ADD_PROG")
        self.ADD_ASSEMBLER = QtWidgets.QPushButton(self.tab)
        self.ADD_ASSEMBLER.setEnabled(True)
        self.ADD_ASSEMBLER.setGeometry(QtCore.QRect(30, 130, 141, 41))
        self.ADD_ASSEMBLER.setCheckable(True)
        self.ADD_ASSEMBLER.setObjectName("ADD_ASSEMBLER")
        self.ADD_LONGTEST = QtWidgets.QPushButton(self.tab)
        self.ADD_LONGTEST.setGeometry(QtCore.QRect(30, 190, 141, 41))
        self.ADD_LONGTEST.setCheckable(True)
        self.ADD_LONGTEST.setObjectName("ADD_LONGTEST")
        self.ADD_QC = QtWidgets.QPushButton(self.tab)
        self.ADD_QC.setGeometry(QtCore.QRect(30, 250, 141, 41))
        self.ADD_QC.setCheckable(True)
        self.ADD_QC.setObjectName("ADD_QC")
        self.ADD_TESTROOM = QtWidgets.QPushButton(self.tab)
        self.ADD_TESTROOM.setGeometry(QtCore.QRect(30, 310, 141, 41))
        self.ADD_TESTROOM.setCheckable(True)
        self.ADD_TESTROOM.setObjectName("ADD_TESTROOM")
        self.ADD_PACKER = QtWidgets.QPushButton(self.tab)
        self.ADD_PACKER.setGeometry(QtCore.QRect(30, 370, 141, 41))
        self.ADD_PACKER.setCheckable(True)
        self.ADD_PACKER.setObjectName("ADD_PACKER")
        self.DELETE = QtWidgets.QPushButton(self.tab)
        self.DELETE.setGeometry(QtCore.QRect(30, 490, 141, 41))
        self.DELETE.setCheckable(True)
        self.DELETE.setObjectName("DELETE")
        self.ADD_CALIB = QtWidgets.QPushButton(self.tab)
        self.ADD_CALIB.setGeometry(QtCore.QRect(30, 430, 141, 41))
        self.ADD_CALIB.setCheckable(True)
        self.ADD_CALIB.setObjectName("ADD_CALIB")
        self.START = QtWidgets.QPushButton(self.tab)
        self.START.setGeometry(QtCore.QRect(30, 590, 141, 61))
        self.START.setObjectName("START")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(660, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.exc_label = QtWidgets.QLabel(self.tab)
        self.exc_label.setGeometry(QtCore.QRect(360, 60, 791, 71))
        self.exc_label.setAutoFillBackground(False)
        self.exc_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exc_label.setText("")
        self.exc_label.setObjectName("exc_label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(660, 240, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.output_label = QtWidgets.QLabel(self.tab)
        self.output_label.setGeometry(QtCore.QRect(360, 330, 791, 221))
        self.output_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(920, 610, 181, 26))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.REGISTER_HUB = QtWidgets.QPushButton(self.tab_2)
        self.REGISTER_HUB.setGeometry(QtCore.QRect(30, 10, 141, 41))
        self.REGISTER_HUB.setCheckable(True)
        self.REGISTER_HUB.setObjectName("REGISTER_HUB")
        self.ADD_PROG_HUB = QtWidgets.QPushButton(self.tab_2)
        self.ADD_PROG_HUB.setGeometry(QtCore.QRect(30, 70, 141, 41))
        self.ADD_PROG_HUB.setCheckable(True)
        self.ADD_PROG_HUB.setObjectName("ADD_PROG_HUB")
        self.ADD_ASSEMBLER_HUB = QtWidgets.QPushButton(self.tab_2)
        self.ADD_ASSEMBLER_HUB.setEnabled(True)
        self.ADD_ASSEMBLER_HUB.setGeometry(QtCore.QRect(30, 130, 141, 41))
        self.ADD_ASSEMBLER_HUB.setCheckable(True)
        self.ADD_ASSEMBLER_HUB.setObjectName("ADD_ASSEMBLER_HUB")
        self.ADD_LONGTEST_HUB = QtWidgets.QPushButton(self.tab_2)
        self.ADD_LONGTEST_HUB.setGeometry(QtCore.QRect(30, 190, 141, 41))
        self.ADD_LONGTEST_HUB.setCheckable(True)
        self.ADD_LONGTEST_HUB.setObjectName("ADD_LONGTEST_HUB")
        self.ADD_QC_HUB = QtWidgets.QPushButton(self.tab_2)
        self.ADD_QC_HUB.setGeometry(QtCore.QRect(30, 250, 141, 41))
        self.ADD_QC_HUB.setCheckable(True)
        self.ADD_QC_HUB.setObjectName("ADD_QC_HUB")
        self.ADD_PACKER_HUB = QtWidgets.QPushButton(self.tab_2)
        self.ADD_PACKER_HUB.setGeometry(QtCore.QRect(30, 310, 141, 41))
        self.ADD_PACKER_HUB.setCheckable(True)
        self.ADD_PACKER_HUB.setObjectName("ADD_PACKER_HUB")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(660, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.exc_label_hub = QtWidgets.QLabel(self.tab_2)
        self.exc_label_hub.setGeometry(QtCore.QRect(360, 60, 791, 71))
        self.exc_label_hub.setAutoFillBackground(False)
        self.exc_label_hub.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exc_label_hub.setText("")
        self.exc_label_hub.setObjectName("exc_label_hub")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(660, 240, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.output_label_hub = QtWidgets.QLabel(self.tab_2)
        self.output_label_hub.setGeometry(QtCore.QRect(360, 330, 791, 221))
        self.output_label_hub.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_label_hub.setText("")
        self.output_label_hub.setObjectName("output_label_hub")
        self.DELETE_HUB = QtWidgets.QPushButton(self.tab_2)
        self.DELETE_HUB.setGeometry(QtCore.QRect(30, 370, 141, 41))
        self.DELETE_HUB.setCheckable(True)
        self.DELETE_HUB.setObjectName("DELETE_HUB")
        self.START_HUB = QtWidgets.QPushButton(self.tab_2)
        self.START_HUB.setGeometry(QtCore.QRect(30, 590, 141, 61))
        self.START_HUB.setObjectName("START_HUB")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.REGISTER.setText(QtWidgets.QApplication.translate("MainWindow", "REGISTER", None, -1))
        self.ADD_PROG.setText(QtWidgets.QApplication.translate("MainWindow", "ADD PROG", None, -1))
        self.ADD_ASSEMBLER.setText(QtWidgets.QApplication.translate("MainWindow", "ADD ASSEMBLER", None, -1))
        self.ADD_LONGTEST.setText(QtWidgets.QApplication.translate("MainWindow", "ADD LONGTEST", None, -1))
        self.ADD_QC.setText(QtWidgets.QApplication.translate("MainWindow", "ADD QC", None, -1))
        self.ADD_TESTROOM.setText(QtWidgets.QApplication.translate("MainWindow", "ADD TESTROOM", None, -1))
        self.ADD_PACKER.setText(QtWidgets.QApplication.translate("MainWindow", "ADD PACKER", None, -1))
        self.DELETE.setText(QtWidgets.QApplication.translate("MainWindow", "DELETE", None, -1))
        self.ADD_CALIB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD CALIB", None, -1))
        self.START.setText(QtWidgets.QApplication.translate("MainWindow", "START", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Exceptions", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "BD OUTPUT", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Device", None, -1))
        self.REGISTER_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "REGISTER", None, -1))
        self.ADD_PROG_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD PROG", None, -1))
        self.ADD_ASSEMBLER_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD ASSEMBLER", None, -1))
        self.ADD_LONGTEST_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD LONGTEST", None, -1))
        self.ADD_QC_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD QC", None, -1))
        self.ADD_PACKER_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "ADD PACKER", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Exceptions", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "BD OUTPUT", None, -1))
        self.DELETE_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "DELETE", None, -1))
        self.START_HUB.setText(QtWidgets.QApplication.translate("MainWindow", "START", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Central", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))

