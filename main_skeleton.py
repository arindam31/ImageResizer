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

        self.layoutManager()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Photo Display')

    def layoutManager(self):

        #Buttons for selectors
        self.selectFileButton = QtGui.QPushButton('Browse file', self)
        self.selectFolderButton = QtGui.QPushButton('Browse folder', self)

        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)

        #List for images list
        self.list_pics = QtGui.QListWidget(self)

        #Pic show area
        self.pic = QtGui.QLabel('No image', self)

        #Hbox 1
        hbox1 = QtGui.QHBoxLayout()

        #Hbox 2
        self.hbox2 = QtGui.QHBoxLayout()

        #Add stretch capability

        hbox1.addStretch(1)
        self.hbox2.addStretch(1)

        #Group for options
        optionsGroup = QtGui.QGroupBox("Options")
        optionsLabel = QtGui.QLabel("Resize:")

        #Declare items in options
        optionsComboBox = QtGui.QComboBox()
        self.checkBoxProportion = QtGui.QCheckBox()
        self.ProportionLabel = QtGui.QLabel('Keep Proportion Ratio')

        #Add to combo box
        optionsComboBox.addItem("Percentage %")
        optionsComboBox.addItem("Pixel")

        #Set default state of checkbox
        self.checkBoxProportion.setChecked(True)

        self.optionsLineEdit = QtGui.QLineEdit()
        self.optionsLineEdit.setFocus()

        optionsLayout = QtGui.QGridLayout()
        optionsLayout.addWidget(optionsLabel, 0, 0)
        optionsLayout.addWidget(optionsComboBox, 0, 1)
        optionsLayout.addWidget(self.optionsLineEdit, 1, 0, 1, 2)
        optionsLayout.addWidget(self.checkBoxProportion, 2, 0)
        optionsLayout.addWidget(self.ProportionLabel, 2, 1)

        optionsGroup.setLayout(optionsLayout)

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
