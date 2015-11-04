"""
What all works in this one:

1) Single file selection dialog works..Returns the name of the file
2) Folder selection works too.
3) Layout management works.
4) Continuous photo selection also works
"""


import sys
from PyQt4 import QtGui, QtCore
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):      
        self.selectFileButton = QtGui.QPushButton('Browse file', self)
        self.selectFolderButton = QtGui.QPushButton('Browse folder', self)
        self.list_pics = QtGui.QListWidget(self)
        self.pic = QtGui.QLabel('', self)


        self.layoutManager()
        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Photo Display')

    def layoutManager(self):
        hbox1 = QtGui.QHBoxLayout()
        self.hbox2 = QtGui.QHBoxLayout()
        hbox1.addStretch(1)
        self.hbox2.addStretch(1)
        optionsGroup = QtGui.QGroupBox("Options")
        echoLabel = QtGui.QLabel("Resize:")
        echoComboBox = QtGui.QComboBox()
        echoComboBox.addItem("Percentage %")
        echoComboBox.addItem("Pixel")
        self.echoLineEdit = QtGui.QLineEdit()
        self.echoLineEdit.setFocus()

        echoLayout = QtGui.QGridLayout()
        echoLayout.addWidget(echoLabel, 0, 0)
        echoLayout.addWidget(echoComboBox, 0, 1)
        echoLayout.addWidget(self.echoLineEdit, 0, 2)
        optionsGroup.setLayout(echoLayout)

        hbox1.addWidget(self.selectFolderButton)
        hbox1.addWidget(self.selectFileButton)
        hbox1.addWidget(self.list_pics)
        hbox1.addWidget(optionsGroup)
        self.hbox2.addWidget(self.pic)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

    def showDialog(self):
        # This function is to provide a folder open dialog

        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open file',
                '/home')
        if fname:
            d = os.listdir(fname)
            print d

        self.list_pics.addItems(d)

    def selectFile(self):
        filedialog = QtGui.QFileDialog(self)
        name = filedialog.getOpenFileName()
        print name
        if hasattr(self, 'pic'):
            self.pic.clear()
            self.setLayout(self.vbox)
        self.setPicture(name)

    def setPicture(self, file_name):
        pixmap = QtGui.QPixmap(file_name)
        pixmap = pixmap.scaledToHeight(200)
        self.pic.setPixmap(pixmap)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
