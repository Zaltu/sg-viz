# --coding:utf-8--
import sys
from PySide2.QtWidgets import QApplication
from qtmainframe import MainFrame

APP = QApplication(sys.argv)
WINDOW = MainFrame(APP)
sys.exit(APP.exec_())
