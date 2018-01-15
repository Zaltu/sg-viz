# --coding:utf-8--
import sys
from PySide.QtGui import QApplication
from qtmainframe import MainFrame

APP = QApplication(sys.argv)
WINDOW = MainFrame(APP)
sys.exit(APP.exec_())
