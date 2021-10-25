import sys
import platform
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from main_functions import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    sys.exit(app.exec_())
