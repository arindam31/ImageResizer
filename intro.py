# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageResizerMain.ui'
#
# Created: Tue Nov 11 15:46:42 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
import sys
from PyQt4.QtGui import *
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(737, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 165, 0);"))
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 491, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectFolderButton = QPushButton(self.centralwidget)
        self.selectFolderButton.setGeometry(QtCore.QRect(390, 210, 151, 81))
        self.selectFolderButton.setStyleSheet(_fromUtf8("background-color: rgb(178, 255, 102);"))
        self.selectFolderButton.setObjectName(_fromUtf8("pushButton"))
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(210, 210, 161, 81))
        self.exitButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect_Folder = QAction(MainWindow)
        self.actionSelect_Folder.setObjectName(_fromUtf8("actionSelect_Folder"))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addAction(self.actionSelect_Folder)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Resizer", None))
        self.selectFolderButton.setText(_translate("MainWindow", "Select Folder", None))
        self.exitButton.setText(_translate("MainWindow", "Exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionSelect_Folder.setText(_translate("MainWindow", "Select Folder", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">IMAGE RESIZER</span></p></body></html>", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.selectFolderButton.clicked.connect(self.showDialog)

    def exitApp(self):
        sys.exit(1)

    def showDialog(self):
        # This function is to provide a folder open dialog

        fname = QFileDialog.getExistingDirectory(self, 'Open file',
                '/home')
        d = os.listdir(fname)
        l = '\n'.join(d)
        self.textEdit.setText(l)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())

