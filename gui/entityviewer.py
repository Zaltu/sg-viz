from PySide.QtGui import QWidget, QTableWidget, QGridLayout, QTableWidgetItem, QPushButton, QHeaderView
from gui import cellmanager

from pprint import pprint as pp

class EntityViewer(QWidget):

    def __init__(self, parent, entity):
        self.parent = parent
        QWidget.__init__(self)
        self.entity = entity
        self.initUI()


    def initUI(self):
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.back = QPushButton("Back")
        self.back.clicked.connect(self.chooseotherentity)
        self.layout.addWidget(self.back, 0, 0)

        self.grid = QTableWidget(self)
        self.layout.addWidget(self.grid, 1, 0)
        self.grid.cellDoubleClicked.connect(self.edit)
        self.grid.cellClicked.connect(self.unedit)
        self.activeCell = None
        self.initData()
        self.grid.horizontalHeader().setMovable(True)


    def initData(self):
        self.entdata = self.parent.parent.db.get(self.entity)
        i = 0
        indexMap = {}
        for field in self.entdata.data[0]:
            self.grid.insertColumn(self.grid.columnCount())
            self.grid.setHorizontalHeaderItem(i, QTableWidgetItem(field))
            indexMap[field] = i
            i += 1
        for ent in self.entdata.data:
            self.grid.insertRow(self.grid.rowCount())
            for field in ent:
                cell = cellmanager.barfCell(ent[field], self.parent)
                self.grid.setCellWidget(self.grid.rowCount()-1, indexMap[field], cell)


    def edit(self, row, column):
        newCell = cellmanager.edit(self.grid.cellWidget(row, column))
        if newCell:
            self.grid.setCellWidget(row, column, newCell)
            self.activeCell = (row, column)


    def unedit(self, row, column):#pylint:disable=unused-argument
        if self.activeCell:
            self.grid.setCellWidget(self.activeCell[0], self.activeCell[1],
                                    cellmanager.save(self.grid.cellWidget(self.activeCell[0],
                                                                          self.activeCell[1])))
            self.activeCell = None


    def chooseotherentity(self):
        self.parent.parent.changeState(self.parent)
