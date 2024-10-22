# main.py

import sys
from PySide6.QtWidgets import QApplication
from ui.home_window_logic import HomeWindowLogic

if __name__ == '__main__':
    # Create the PyQt application
    app = QApplication(sys.argv)

    # Initialize the Signup Window
    home_window = HomeWindowLogic()
    home_window.show()

    # Execute the application
    sys.exit(app.exec())
