from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QFileDialog, QGridLayout, QCheckBox
from PySide6.QtGui import QTextOption, QIcon
from PySide6.QtCore import Qt

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
        self.link = SingleLineTextEdit(self)
        self.link.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.link.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.link.setFixedSize(220, 26)
        # Managing directory path text field and explorer button
        self.dir = SingleLineTextEdit(self)
        self.dir.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.dir.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dir.setEnabled(False)
        self.dir.setFixedSize(170, 26)
        self.dir.setStyleSheet("color: gray")
        self.dir.setPlaceholderText("Path where u want(if u want) save QR")

        self.pathbut = QPushButton(self)
        self.pathbut.setToolTip('Explore directories')
        self.pathbut.setFixedSize(20, 20)
        # pathicon = QIcon("/IMG/file-explorer.png")
        # pathico = pathicon.pixmap(10, 10)
        # self.pathbut.setIcon(pathico)
        self.pathbut.setVisible(False)
        self.pathbut.clicked.connect(self.openDirectoryDialog)

        self.pathbox = QCheckBox(self)
        self.pathbox.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px; }")
        self.pathbox.stateChanged.connect(self.onPathCheckbox)
        # Creating button
        self.crbut = QPushButton("Make It QR!")
        self.crbut.clicked.connect(self.makeQR)
        # Taking value from text field
        # Create layout and adding items
        layout = QGridLayout()
        layout.addWidget(lab1, 0, 0, 1, 3)
        layout.addWidget(self.link, 1, 0, 1, 3)
        layout.addWidget(self.dir, 2, 0)
        layout.addWidget(self.pathbut, 2, 1)
        layout.addWidget(self.pathbox)
        layout.addWidget(self.crbut, 3, 0, 1, 3)
        self.setLayout(layout)
        self.setWindowTitle("QR Creator")
        self.show()
        self.activateWindow()
        # Setting start pos and size of window
        self.setGeometry(100, 100, 300, 250)
        # Setting maximum size
        self.setMaximumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumWidth(250)

    def openDirectoryDialog(self):
        # Show the directory dialog and get the selected directory
        directory_dialog = QFileDialog(self)
        directory_path = directory_dialog.getExistingDirectory(self, "Open Directory", "")

        if directory_path:
            self.dir.setText(directory_path)

    def onPathCheckbox(self, state):
        if state == 2:
            self.dir.setEnabled(True)
            self.pathbut.setVisible(True)
            self.poss = True
        else:
            self.dir.setEnabled(False)
            self.pathbut.setVisible(False)
            self.poss = False

    def makeQR(self):
        dat = self.link.toPlainText()
        ipath = self.dir.toPlainText()
        print(self.poss, ipath)
        qrCreate.qrcreator(dat, self.poss, ipath)


# Needed classes and functions
class SingleLineTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptRichText(False)  # Disable rich text pasting

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            event.ignore()  # Ignore Enter key press event
        else:
            super().keyPressEvent(event)

    def insertFromMimeData(self, source):
        # Prevent multiline text pasting
        if source.hasText():
            text = source.text().replace('\n', '')
            self.insertPlainText(text)
