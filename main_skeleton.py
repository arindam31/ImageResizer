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
import resizer

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

        self.setGeometry(300, 100, 800, 400)
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
        """
        Top box has buttons
        1) Browse File
        2) Browse Folder
        3) Clear
        """
        self.topGroupBox = QtGui.QGroupBox("Top Group Area")
        #Buttons for selectors
        self.selectFileButton = QtGui.QPushButton('Browse file', self)
        self.selectFolderButton = QtGui.QPushButton('Browse folder', self)
        self.clearListButton = QtGui.QPushButton('Clear', self)
        self.convertButton = QtGui.QPushButton('Convert', self)

        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)
        self.clearListButton.clicked.connect(self.clearList)
        self.convertButton.clicked.connect(self.Process)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.selectFileButton)
        layout.addWidget(self.selectFolderButton)
        layout.addWidget(self.clearListButton)
        layout.addWidget(self.convertButton)
        self.topGroupBox.setLayout(layout)

    def createOptionsGroupBox(self):
        """
        Option box has buttons
        1) Options combobox
        2) Resize label
        3) Checkbox for proportion
        """
        self.optionsGroupBox = QtGui.QGroupBox("Options Area")
        #layout = QtGui.QHBoxLayout()
        optionsLayout = QtGui.QGridLayout()
        #Group for options
        optionsGroup = QtGui.QGroupBox("Options")
        optionsLabel = QtGui.QLabel("Resize:")

        #Declare items in options
        self.optionsComboBox = QtGui.QComboBox()
        self.checkBoxProportion = QtGui.QCheckBox()
        self.ProportionLabel = QtGui.QLabel('Keep Proportion Ratio')

        #Add to combo box
        self.optionsComboBox.addItem("Percentage %")
        self.optionsComboBox.addItem("Pixel")

        #Set default state of checkbox
        self.checkBoxProportion.setChecked(True)

        #Edit box
        self.optionsLineEdit = QtGui.QLineEdit()  # This is a text box for percentage or base width
        self.optionsLineEdit.setFocus()

        optionsLayout.addWidget(optionsLabel, 0, 0)
        optionsLayout.addWidget(self.optionsComboBox, 0, 1)
        optionsLayout.addWidget(self.optionsLineEdit, 1, 0, 1, 2)
        optionsLayout.addWidget(self.checkBoxProportion, 2, 0)
        optionsLayout.addWidget(self.ProportionLabel, 2, 1)
        self.optionsGroupBox.setLayout(optionsLayout)

    def createDisplayAreaBox(self):
        """
        Display Box has following items:
        1) Table
        """
        self.displayGroupBox = QtGui.QGroupBox("Display Area")
        layout = QtGui.QVBoxLayout()

        #List for images list
        self.table_pics = QtGui.QTableWidget(self)

        self.table_pics.setRowCount(4)  # Set no of rows needed at first launch
        self.table_pics.setColumnCount(4)  # Set no of columns needed at first launch
        self.table_pics.setColumnWidth(0, 300)  # 0 in the column number, 500 the width
        self.table_pics.setColumnWidth(1, 100)  # 1 is the 2nd column
        self.table_pics.setColumnWidth(2, 80)  # 2 is the 3rd column
        self.table_pics.setColumnWidth(3, 80)  # 2 is the 3rd column
        self.table_pics.horizontalHeader().setStretchLastSection(True)  # Stretches the last column till the end
        self.table_pics.setHorizontalHeaderLabels(QtCore.QString("Name;Resolution;Size(kb);NewSize(kb)").split(";"))  # Assign headers

        layout.addWidget(self.table_pics)
        #layout.addStretch(1)
        self.displayGroupBox.setLayout(layout)

    def showDialog(self):
        # This function is to provide a folder open dialog

        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open folder',
                '/home')
        if fname:
            self.file_list = [os.path.join(str(fname), f) for f in os.listdir(str(fname))]
            print self.file_list
        file_name_only = [os.path.basename(f) for f in self.file_list]  # Get only file name into a list

        #self.list_pics.addItems(d)
        self.table_pics.setRowCount(len(self.file_list))  # Based of no of files found, numbering of the rows
        #table.setVerticalHeaderLabels(QString("V1;V2;V3;V4").split(";"))
        #self.table_pics.setVerticalHeaderLabels(QtCore.QString("V1;V2;V3;V4").split(";"))
        for m, pic in enumerate(file_name_only):
            size_of_pic = resizer.size_of_photo_in_kilobytes(self.file_list[m])  # Get size
            resolution_of_pic = resizer.resolution_of_file(self.file_list[m])  # Get resolution

            photo_name_widget = QtGui.QTableWidgetItem(pic)  # Convert to widget item
            photo_size_widget = QtGui.QTableWidgetItem(str(size_of_pic))  # Convert to widget item
            resolution_widget = QtGui.QTableWidgetItem(str(resolution_of_pic))  # Convert to widget item
            self.table_pics.setItem(m, 0, photo_name_widget)  # Set name on 1st column
            self.table_pics.setItem(m, 1, resolution_widget)  # Set size of file on 2nd
            self.table_pics.setItem(m, 2, photo_size_widget)  # Set size of file on 2nd


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
        self.table_pics.clearContents()  # Clears the table

    def Process(self):
        percentage = True
        print self.optionsComboBox.currentText()
        if not self.optionsComboBox.currentText() == 'Percentage %':
            percentage = False

        text_in_box = self.optionsLineEdit.text()  # Get value from text box for base width or percentage
        if not text_in_box:
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Hi'),
                                               QtCore.QString('No option selected'),
                                               )
            return
        try:
            int(text_in_box)
        except Exception:
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Hi'),
                                           QtCore.QString('You must enter Integer only'),
                                           )

        if percentage:
            new_size_list = resizer.resize_list_of_images(self.file_list, percent=int(text_in_box))
        else:
            new_size_list = resizer.resize_list_of_images(self.file_list, basewidth=int(text_in_box))

        for m, size in enumerate(new_size_list):
            photo_size = QtGui.QTableWidgetItem(str(size))
            self.table_pics.setItem(m, 3, photo_size)  # Set name on 1st column


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
