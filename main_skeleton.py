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
        self.createTopGroupBox()
        self.createOptionsGroupBox()
        self.createDisplayAreaBox()

        #Vbox Main
        self.vboxMain = QtGui.QVBoxLayout()
        #self.vboxMain.setMenuBar(self.menuBar)

        self.vboxMain.addWidget(self.topGroupBox)
        self.vboxMain.addWidget(self.optionsGroupBox)
        self.vboxMain.addWidget(self.displayGroupBox)

        self.setLayout(self.vboxMain)

    def createTopGroupBox(self):
        self.topGroupBox = QtGui.QGroupBox("Top Group Area")
        #Buttons for selectors
        self.selectFileButton = QtGui.QPushButton('Browse file', self)
        self.selectFolderButton = QtGui.QPushButton('Browse folder', self)
        self.clearListButton = QtGui.QPushButton('Clear', self)

        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)
        self.clearListButton.clicked.connect(self.clearList)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.selectFileButton)
        layout.addWidget(self.selectFolderButton)
        layout.addWidget(self.clearListButton)
        self.topGroupBox.setLayout(layout)

    def createOptionsGroupBox(self):
        self.optionsGroupBox = QtGui.QGroupBox("Options Area")
        #layout = QtGui.QHBoxLayout()
        optionsLayout = QtGui.QGridLayout()
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

        optionsLayout.addWidget(optionsLabel, 0, 0)
        optionsLayout.addWidget(optionsComboBox, 0, 1)
        optionsLayout.addWidget(self.optionsLineEdit, 1, 0, 1, 2)
        optionsLayout.addWidget(self.checkBoxProportion, 2, 0)
        optionsLayout.addWidget(self.ProportionLabel, 2, 1)
        self.optionsGroupBox.setLayout(optionsLayout)


    def createDisplayAreaBox(self):
        self.displayGroupBox = QtGui.QGroupBox("Display Area")
        layout = QtGui.QHBoxLayout()

        #List for images list
        self.list_pics = QtGui.QListWidget(self)

        #Pic show area
        self.pic = QtGui.QLabel('No image', self)

        layout.addWidget(self.list_pics)
        layout.addWidget(self.pic)
        self.displayGroupBox.setLayout(layout)

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
            self.setLayout(self.vboxMain)
        self.setPicture(name)

    def setPicture(self, file_name):
        pixmap = QtGui.QPixmap(file_name)
        pixmap = pixmap.scaledToHeight(100)
        self.pic.setPixmap(pixmap)

    def clearList(self):
        self.list_pics.clear()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
