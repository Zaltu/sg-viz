from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QComboBox
from gui.entityviewer import EntityViewer
from libs import json_reader, const
from shotgun_api3 import Shotgun

class EntitySelector(QWidget):

    def __init__(self, parent):
        self.parent = parent
        QWidget.__init__(self)
        self.initUI()


    def initUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        asksel = QLabel("Please select the entity information you wish to peruse:")
        self.layout.addWidget(asksel, 0, 0)

        self.entityTypes = QComboBox()
        self.getEntityTypes()
        self.layout.addWidget(self.entityTypes, 0, 1)

        self.go = QPushButton("Go")
        self.go.clicked.connect(self.enterentview)
        self.layout.addWidget(self.go, 1, 0, 1, 2)


    def getEntityTypes(self):
        self.entityTypes.addItems(json_reader.getcomplexdata('entities'))


    def enterentview(self):
        self.parent.changeState(EntityViewer(self, self.entityTypes.currentText()))
