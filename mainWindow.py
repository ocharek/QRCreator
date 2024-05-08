from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PySide6.QtGui import QTextOption
from PySide6.QtCore import Qt

import qrCreate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Create items
        # Label
        lab = QLabel('What should QR code contain?')
        # Managing text field
        self.link = SingleLineTextEdit(self)
        self.link.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.link.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.link.setFixedSize(200, 26)
        # Button
        crbut = QPushButton("Make It QR!")
        crbut.clicked.connect(self.makeQR)
        # Taking value from text field
        # Create layout and adding items
        layout = QVBoxLayout()
        layout.addWidget(lab)
        layout.addWidget(self.link)
        layout.addWidget(crbut)
        self.setLayout(layout)
        self.setWindowTitle("QR Creator")
        self.show()
        self.activateWindow()
        self.setGeometry(100, 100, 300, 200)

    def makeQR(self):
        dat = self.link.toPlainText()
        qrCreate.qrcreator(dat)


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
