# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'komedia.ui'
#
# Created: Fri Apr  8 16:40:30 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1049, 598)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout.addWidget(self.textEdit_2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Comics = QtGui.QAction(MainWindow)
        self.actionSave_Comics.setObjectName(_fromUtf8("actionSave_Comics"))
        self.actionExport_Config = QtGui.QAction(MainWindow)
        self.actionExport_Config.setObjectName(_fromUtf8("actionExport_Config"))
        self.actionImport_Config = QtGui.QAction(MainWindow)
        self.actionImport_Config.setObjectName(_fromUtf8("actionImport_Config"))
        self.actionVerify_Config = QtGui.QAction(MainWindow)
        self.actionVerify_Config.setObjectName(_fromUtf8("actionVerify_Config"))
        self.actionCreating_Config = QtGui.QAction(MainWindow)
        self.actionCreating_Config.setObjectName(_fromUtf8("actionCreating_Config"))
        self.actionAbout_Komedia = QtGui.QAction(MainWindow)
        self.actionAbout_Komedia.setObjectName(_fromUtf8("actionAbout_Komedia"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.prevComic)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.nextComic)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.randComic)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), MainWindow.changeComic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Alt Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "About Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Link to Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Previous Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Next Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Random Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Comics.setText(QtGui.QApplication.translate("MainWindow", "Save Comics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Config.setText(QtGui.QApplication.translate("MainWindow", "Export Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Config.setText(QtGui.QApplication.translate("MainWindow", "Import Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerify_Config.setText(QtGui.QApplication.translate("MainWindow", "Verify Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreating_Config.setText(QtGui.QApplication.translate("MainWindow", "Creating Config", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Komedia.setText(QtGui.QApplication.translate("MainWindow", "About Komedia", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
