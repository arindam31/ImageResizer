"""
What all works in this one:

1) Single file selection dialog works..Returns the name of the file
2) Folder selection works too.
3) Layout management works.
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

        self.selectFileButton = QtGui.QPushButton('Browse file',self)
        self.selectFolderButton = QtGui.QPushButton('Browse folder',self)
        self.pic = QtGui.QLabel('Arindam Rocks', self)
        self.layoutManager()
        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')


    def layoutManager(self):
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        hbox1.addStretch(1)
        hbox2.addStretch(1)
        hbox1.addWidget(self.selectFolderButton)
        hbox1.addWidget(self.selectFileButton)
        hbox2.addWidget(self.pic)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

    def showDialog(self):
        # This function is to provide a folder open dialog
        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open file',
                '/home')
        if fname:
            d = os.listdir(fname)
            l = '\n'.join(d)
            print l

    def selectFile(self):
        filedialog = QtGui.QFileDialog(self)
        name = filedialog.getOpenFileName()
        print name
        self.setPicture(name)

    def setPicture(self, FILENAME):

        pixmap = QtGui.QPixmap(FILENAME)
        pixmap = pixmap.scaledToHeight(200)
        self.pic.setPixmap(pixmap)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
