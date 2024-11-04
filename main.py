import sys
from PySide6.QtWidgets import QApplication
from ui.MainWindow_logic import MainWindowLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindowLogic()
    mainWindow.show()

    sys.exit(app.exec())
