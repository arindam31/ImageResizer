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
import math

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
        self.setMaximumHeight(800)
        self.createMenuBar()

    def layoutManager(self):
        #self.createMenuBar()
        self.createTopGroupBox()
        self.createOptionsGroupBox()
        self.createDisplayAreaBox()
        self.createbottomGroupBox()

        #Vbox Main
        self.vboxMain = QtGui.QVBoxLayout()

        self.vboxMain.addWidget(self.topGroupBox)
        self.vboxMain.addWidget(self.optionsGroupBox)
        self.vboxMain.addWidget(self.displayGroupBox)
        self.vboxMain.addWidget(self.bottomGroupBox)
        self.setLayout(self.vboxMain)
        palette = QtGui.QPalette()

        #Apply an image background
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('wallpaper.jpg')))
        self.setPalette(palette)

    def createMenuBar(self):
        self.fileMenu = QtGui.QMenu("&File", self)
        self.OptionsMenu = QtGui.QMenu("&Options", self)
        self.HelpMenu = QtGui.QMenu("&Help", self)
        menu = QtGui.QMenuBar(self)
        menu.setGeometry(QtCore.QRect(0, 0, 800, 25))
        menu.setObjectName(_fromUtf8("menubar"))
        menu.addMenu(self.fileMenu)
        menu.addMenu(self.OptionsMenu)
        menu.addMenu(self.HelpMenu)

    def createTopGroupBox(self):
        """
        Top box has buttons
        1) Browse File
        2) Browse Folder
        3) Clear
        """
        self.topGroupBox = QtGui.QGroupBox("Select Action")
        self.topGroupBox.setMaximumHeight(100)
        self.topGroupBox.setFlat(True)

       #  self.topGroupBox.setStyleSheet("""
       #  QGroupBox
       # {
       #     background-color: rgb(255, 255, 200);
       #     border:1px solid rgb(255, 171, 255);
       # }
       # """
       #  )

        #Buttons for selectors
        self.selectFileButton = QtGui.QPushButton('Choose file', self)
        self.selectFolderButton = QtGui.QPushButton('Choose folder', self)
        self.clearListButton = QtGui.QPushButton('Clear list', self)
        self.convertButton = QtGui.QPushButton('Convert', self)

        #self.convertButton.setStyleSheet("font-size:18px;background-color:red;\
        #border: 1px solid blue")

        #Adding tool tips for buttons
        self.selectFileButton.setToolTip('Press this button to select single file to convert')
        self.selectFolderButton.setToolTip('Press this button to select a folder with pictures to convert')
        self.clearListButton.setToolTip('Press this button to clear the list below')
        self.convertButton.setToolTip('Press this button to start conversion of pictures')

        #Assign shortcuts
        self.selectFileButton.setShortcut(QtGui.QKeySequence("Ctrl+F"))
        self.convertButton.setShortcut(QtGui.QKeySequence("Ctrl+P"))
        self.selectFolderButton.setShortcut(QtGui.QKeySequence("Ctrl+D"))
        self.clearListButton.setShortcut(QtGui.QKeySequence("Ctrl+C"))

        # Connect button to functions
        self.selectFileButton.clicked.connect(self.selectFile)
        self.selectFolderButton.clicked.connect(self.showDialog)
        self.clearListButton.clicked.connect(self.resetEverything)
        self.convertButton.clicked.connect(self.Process)

        #Create layout
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.selectFileButton)
        layout.addWidget(self.selectFolderButton)
        layout.addWidget(self.clearListButton)
        layout.addWidget(self.convertButton)
        #layout.addStretch(1)
        self.topGroupBox.setLayout(layout)

    def createOptionsGroupBox(self):
        """
        Option box has buttons
        1) Options combobox
        2) Resize label
        3) Checkbox for proportion
        """
        self.optionsGroupBox = QtGui.QGroupBox("Options Area")
        self.optionsGroupBox.setMaximumHeight(150)
        optionsLayout = QtGui.QGridLayout()
        #Group for options
        optionsLabel = QtGui.QLabel("Resize by:")

        #Add a Slider for Quality Selection
        self.qualitySlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.qualitySlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.qualitySlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.qualitySlider.setTickInterval(10)
        self.qualitySlider.setSingleStep(1)
        self.qualitySlider.setValue(80)  # Set default value at 80

        QualityLabel = QtGui.QLabel("Quality %:")

        self.valueSpinBox = QtGui.QSpinBox()  # This is for quality value display
        self.valueSpinBox.setRange(1, 100)
        self.valueSpinBox.setSingleStep(1)
        self.valueSpinBox.setValue(80)
        self.qualitySlider.valueChanged.connect(self.valueSpinBox.setValue)  # If slider changes, the Spin Box changes
        self.valueSpinBox.valueChanged.connect(self.qualitySlider.setValue)  # If Spin Box  changes, the Slider changes

        #Declare items in options
        self.optionsComboBox = QtGui.QComboBox()

        #Add to combo box
        self.optionsComboBox.addItem("Percentage % (Size of Image)")
        self.optionsComboBox.addItem("Pixel")

        #Edit box
        valueLabel = QtGui.QLabel("Enter Value:")
        self.optionsLineEdit = QtGui.QLineEdit()  # This is a text box for percentage or base width
        self.optionsLineEdit.setFocus()
        self.optionsLineEdit.setToolTip('Enter a number after selecting reduction choice i.e by percentage or by width')

        optionsLayout.addWidget(optionsLabel, 0, 0)
        optionsLayout.addWidget(self.optionsComboBox, 0, 1)
        optionsLayout.addWidget(QualityLabel, 0, 2)
        optionsLayout.addWidget(self.valueSpinBox, 0, 3)
        optionsLayout.addWidget(self.qualitySlider, 0, 4)
        optionsLayout.addWidget(valueLabel, 1, 0)
        optionsLayout.addWidget(self.optionsLineEdit, 1, 1, 1, 2)

        #optionsLayout.setColumnStretch(1, 20)
        #optionsLayout.setColumnStretch(2, 20)
        #optionsLayout.setColumnStretch(3, 20)
        #optionsLayout.setColumnStretch(4, 20)
        #optionsLayout.setColumnStretch(5, 20)
        self.optionsGroupBox.setLayout(optionsLayout)

    def createDisplayAreaBox(self):
        """
        Display Box has a Table that shows files selected to be processed

        """
        self.displayGroupBox = QtGui.QGroupBox("Display Area")
        self.pic = QtGui.QLabel('', self)
        self.displayGroupBox.setMaximumHeight(500)
        layout = QtGui.QVBoxLayout()

        #List for images list
        self.table_pics = QtGui.QTableWidget(self)
        self.table_pics.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.table_pics.setColumnCount(4)  # Set no of columns needed at first launch
        self.table_pics.setColumnWidth(0, 300)  # 0 in the column number, 300 the width
        self.table_pics.setColumnWidth(1, 100)  # 1 is the 2nd column
        self.table_pics.setColumnWidth(2, 80)  # 2 is the 3rd column
        self.table_pics.setColumnWidth(3, 80)  # 3 is the 4th column
        self.table_pics.horizontalHeader().setStretchLastSection(True)  # Stretches the last column till the end
        self.table_pics.setHorizontalHeaderLabels(QtCore.QString("Name;Resolution;Size(kb);NewSize(kb)").split(";"))

        layout.addWidget(self.table_pics)
        layout.addWidget(self.pic)
        self.displayGroupBox.setLayout(layout)

    def createbottomGroupBox(self):
        self.bottomGroupBox = QtGui.QGroupBox("Progress update")
        self.bottomGroupBox.setMaximumHeight(60)
        layout = QtGui.QVBoxLayout()

        self.progressbar = QtGui.QProgressBar(self)

        layout.addWidget(self.progressbar)
        layout.addStretch(1)
        self.bottomGroupBox.setLayout(layout)

    def showDialog(self):
        # This function is to provide a folder open dialog

        selected_dir_name = QtGui.QFileDialog.getExistingDirectory(self, 'Open folder',
                '/home')
        if not selected_dir_name:
            return

        list_with_pics = resizer.get_images_list(str(selected_dir_name))

        if not list_with_pics:
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Warning'),
                                               QtCore.QString('No images found'),
                                               )
            return


        file_name_only = [os.path.basename(f) for f in list_with_pics]  # Get only file name into a list

        self.table_pics.setRowCount(len(list_with_pics))  # Based of no of files found, numbering of the rows
        self.detail_dict = {}  # Dict with all details
        self.checked_list = []  # List to store checked items

        for m, pic in enumerate(file_name_only):
            size_of_pic = resizer.size_of_photo_in_kilobytes(list_with_pics[m])  # Get size
            resolution_of_pic = resizer.resolution_of_file(list_with_pics[m])  # Get resolution
            self.detail_dict[pic] = {'size': size_of_pic,
                                     'resolution': resolution_of_pic,
                                     'full_path': os.path.join(str(selected_dir_name), pic)  # Location of the pic
                                    }

            self.checked_list.append(list_with_pics[m])
            photo_name_widget = QtGui.QTableWidgetItem(pic)  # Convert to widget item
            photo_name_widget.setFlags(QtCore.Qt.ItemIsUserCheckable |  # Adding checkbox to each row
                                  QtCore.Qt.ItemIsEnabled)
            photo_name_widget.setCheckState(QtCore.Qt.Checked)  # Set them as checked
            photo_size_widget = QtGui.QTableWidgetItem(str(size_of_pic))  # Convert to widget item
            resolution_widget = QtGui.QTableWidgetItem(str(resolution_of_pic))  # Convert to widget item
            self.table_pics.setItem(m, 0, photo_name_widget)  # Set name on 1st column
            self.table_pics.setItem(m, 1, resolution_widget)  # Set size of file on 2nd
            self.table_pics.setItem(m, 2, photo_size_widget)  # Set size of file on 3rd


        self.table_pics.itemClicked.connect(self.handleItemClicked)  # Connecting to
        # The function that handles what happens after selecting a checkbox
        self.table_pics.doubleClicked.connect(self.print_hi)

        if len(list_with_pics) * 60 > 500:
            pass
        #else:
        #    self.displayGroupBox.setMaximumHeight(len(list_with_pics) * 60)


        if self.convertButton.isEnabled():
            pass
        else:
            self.convertButton.setDisabled(True)
        self.file_list = list_with_pics

    def print_hi(self):
        print 'Hi'
        row = self.table_pics.currentRow()
        print "Row no:", row
        self.item = self.table_pics.item(row, 0)
        print str(self.item.text())


    def handleItemClicked(self, item):
        self.file_name_only = [os.path.basename(f) for f in self.checked_list]
        if item.checkState() == QtCore.Qt.Checked:
            if item.text() not in self.file_name_only:
                self.checked_list.append(self.detail_dict[str(item.text())]['full_path'])
        else:
            if item.text() in self.file_name_only:
                self.checked_list.remove(self.detail_dict[str(item.text())]['full_path'])

    def barUpdate(self):
        self.barState = 0
        while self.barState < len(self.file_list):
            self.barState += 1
            self.progressbar.setValue(self.barState * 100/len(self.file_list))


    def selectFile(self):
        filedialog = QtGui.QFileDialog(self)
        if not hasattr(self, 'file_list'):
            self.file_list = []
            self.checked_list = []

        if not hasattr(self, 'detail_dict'):
            self.detail_dict = {}
        self.single_pic = str(filedialog.getOpenFileName()) # String converted
        file_name = os.path.basename(self.single_pic)
        if self.single_pic:  # This is , if someone selects "Cancel"
            self.file_list.append(self.single_pic)
            self.checked_list.append(self.single_pic)
            self.table_pics.hide()  # Hide the table which by default shown on launch
            size_of_pic = resizer.size_of_photo_in_kilobytes(self.single_pic)  # Get size
            resolution_of_pic = resizer.resolution_of_file(self.single_pic)  # Get resolution
            self.detail_dict[file_name] = {'size': size_of_pic,
                                     'resolution': resolution_of_pic,
                                     'full_path': self.single_pic,
                                    }
        else:
            return

        if hasattr(self, 'pic'):
            self.pic.clear()  # This is for 2nd or more times selection of single picture
            self.setLayout(self.vboxMain)
        else:
            return
        self.setPicture(self.single_pic)  # Show the selected pic in display area


    def setPicture(self, file_name):
        pixmap = QtGui.QPixmap(file_name)
        pixmap = pixmap.scaledToHeight(100)
        self.pic.setPixmap(pixmap)

    def resetEverything(self):
        self.table_pics.setRowCount(0)
        #self.table_pics.setColumnCount(0)
        self.table_pics.show()

        self.table_pics.clearContents()  # Clears the table
        self.table_pics.reset()
        self.convertButton.setDisabled(False)
        self.pic.clear()
        if hasattr(self, 'file_list'):
            del self.file_list

        if hasattr(self, 'file_list'):
            del self.checked_list
        self.progressbar.reset()  # Get the progress bar to zero level


    def Process(self):
        percentage = True
        self.barState = 0
        if 'Percentage' not in self.optionsComboBox.currentText():
            percentage = False

        text_in_box = self.optionsLineEdit.text()  # Get value from text box for base width or percentage
        if not text_in_box:
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Warning'),
                                               QtCore.QString('No value entered'),
                                               )
            return
        try:
            int(text_in_box)
        except Exception:
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Warning'),
                                           QtCore.QString('You must enter Integer only'),
                                           )
            return

        if not hasattr(self, 'file_list'):
            self.pop_up_warning = QtGui.QMessageBox.warning(self, QtCore.QString('Warning'),
                                               QtCore.QString('No files added to convert'),
                                               )
            return

        new_size_list = []
        if percentage:
            percent_factor = math.sqrt(float(text_in_box)/100)  # The base width will be based on this percentage
        else:
            percent_factor = 1

        setQuality = int(self.valueSpinBox.value()) # Collect quality value from the quality spinner

        while self.barState < len(self.file_list):
            for img in self.file_list:
                if img in self.checked_list or hasattr(self, 'single_pic'):
                    try:
                        base_name = os.path.basename(img)
                    except TypeError:
                        base_name = os.path.basename(str(img))
                    width = self.detail_dict[base_name]['resolution'][0]
                    size = resizer.resize_image(img, basewidth=int(round(width * percent_factor)), QUALITY=setQuality)
                    new_size_list.append(size)
                    self.barState += 1
                    self.progressbar.setValue(self.barState * 100/len(self.checked_list))
                else:
                    new_size_list.append('Skipped')

        for m, size in enumerate(new_size_list):
            photo_size = QtGui.QTableWidgetItem(str(size))
            self.table_pics.setItem(m, 3, photo_size)  # Set name on 1st column

        self.convertButton.setDisabled(True)  # We don't want to let user press process button again without reset


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()