import mainWindow
import PySide6.QtWidgets as QtW
import sys


if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = mainWindow.MainWindow()
    widget.show()
    sys.exit(app.exec())
