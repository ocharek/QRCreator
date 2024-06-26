from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QGridLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, Signal
import os

import qrCreate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Create items
        # Label
        lab1 = QLabel('What should QR code contain?')
        # Managing value text field
        self.link = enterP(self)
        self.link.enterPressed.connect(self.makeQR)
        self.link.setFixedSize(220, 26)
        # Managing directory path text field and explorer button
        self.dir = QLineEdit(self)
        self.dir.setEnabled(False)
        self.dir.setFixedSize(190, 26)
        self.dir.setStyleSheet("color: gray")
        self.dir.setPlaceholderText("Path to save")

        self.pathbut = QPushButton(self)
        self.pathbut.setToolTip('Explore directories')
        self.pathbut.setFixedSize(25, 25)
        image_path = "IMG/fexp.png"
        if os.path.exists(image_path):
            # Load the image
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(25, 25)

            # Create and set the icon
            icon = QIcon(pixmap)
            self.pathbut.setIcon(icon)
        else:
            print("Image file not found:", image_path)
        self.pathbut.clicked.connect(self.openDirectoryDialog)

        # Creating button
        self.crbut = QPushButton("Make It QR!")
        self.crbut.clicked.connect(self.makeQR)
        # Taking value from text field
        # Create layout and adding items
        layout = QGridLayout()
        layout.addWidget(lab1, 0, 0, 1, 2)
        layout.addWidget(self.link, 1, 0, 1, 2)
        layout.addWidget(self.dir, 2, 0)
        layout.addWidget(self.pathbut, 2, 1)
        layout.addWidget(self.crbut, 3, 0, 1, 2)
        self.setLayout(layout)
        self.setWindowTitle("QR Creator")
        self.setWindowIcon(QIcon('IMG/CrIcon.png'))
        self.show()
        self.activateWindow()
        # Setting start pos and size of window
        self.setGeometry(100, 100, 300, 250)
        # Setting maximum size
        self.setMaximumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumWidth(250)

        # Message box
        self.nodat = QMessageBox()
        self.nodat.setWindowTitle('Warning')
        self.nodat.setWindowIcon(QIcon('IMG/warning.png'))
        self.nodat.setText('You need to put some data into QR code')
        self.nodat.setStandardButtons(QMessageBox.Ok)
        self.nodat.setGeometry(150, 200, 0, 0)
        self.nodat.setIcon(QMessageBox.Icon.Information)



    def openDirectoryDialog(self):
        # Show the directory dialog and get the selected directory
        directory_dialog = QFileDialog(self)
        directory_path = directory_dialog.getExistingDirectory(self, "Open Directory", "")

        if directory_path:
            self.dir.setText(directory_path)

    # QR maker func
    def makeQR(self):
        dat = self.link.text()
        if dat != '':
            ipath = self.dir.text()
            if ipath != '':
                qrCreate.qrcreator(dat, True, ipath)
            else:
                qrCreate.qrcreator(dat, False, ipath)
        else:
            self.nodat.exec()


# Action when Enter is pressed
class enterP(QLineEdit):
    enterPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.enterPressed.emit()  # MakeQR
        else:
            super().keyPressEvent(event)
