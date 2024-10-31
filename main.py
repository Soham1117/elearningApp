# main.py

import sys
from PySide6.QtWidgets import QApplication
from ui.MainWindow_logic import MainWindowLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Initialize the Signup Window
    mainWindow = MainWindowLogic()
    mainWindow.show()

    # Execute the application
    sys.exit(app.exec())
