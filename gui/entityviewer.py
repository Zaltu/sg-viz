from PySide.QtGui import QWidget, QTableWidget, QGridLayout, QTableWidgetItem, QPushButton, QHeaderView, QMenu
from PySide.QtCore import Qt
from gui import cellmanager
from libs import shotgunmanager, json_reader

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

        self.pullb = QPushButton("Reload from Shotgun")
        self.pullb.clicked.connect(self.pull)
        self.layout.addWidget(self.pullb, 2, 0)

        self.savePage = QPushButton("Save Page")
        self.savePage.clicked.connect(self.setPageSettings)
        self.layout.addWidget(self.savePage, 3, 0)

        self.grid = QTableWidget(self)
        self.layout.addWidget(self.grid, 1, 0)
        self.grid.cellDoubleClicked.connect(self.edit)
        self.grid.cellClicked.connect(self.unedit)
        self.activeCell = None
        self.initData()
        self.grid.horizontalHeader().setMovable(True)
        self.grid.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)

        self.grid.horizontalHeader().customContextMenuRequested.connect(self.hideF)



    def initData(self):
        self.entdata = self.parent.parent.db.get(self.entity)
        self.fieldsToShow = self.sanitizeFields(self.entdata)
        i = 0
        indexMap = {}
        for field in self.fieldsToShow:
            self.grid.insertColumn(self.grid.columnCount())
            self.grid.setHorizontalHeaderItem(i, QTableWidgetItem(field))
            indexMap[field] = i
            i += 1
        for ent in self.entdata.data:
            self.grid.insertRow(self.grid.rowCount())
            for field in ent:
                if field in indexMap:
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


    def pull(self):
        self.parent.parent.db.reloadTable(self.entity)
        self.parent.parent.changeState(EntityViewer(self.parent, self.entity))


    def hideF(self, position):
        menu = QMenu()
        hideField = menu.addAction("Hide")
        ac = menu.exec_(self.grid.mapToGlobal(position))
        if ac == hideField:
            index = self.grid.horizontalHeader().logicalIndexAt(position)
            self.grid.removeColumn(index)
        

    def setPageSettings(self):
        rules = []
        for i in range(0, self.grid.columnCount()):
            rules.append(self.grid.horizontalHeaderItem(self.grid.horizontalHeader().visualIndex(i)).text())
        json_reader.write(rules, "data/pagesettings/%s" % self.entity)


    def sanitizeFields(self, allData):
        try:
            rules = json_reader.read("data/pagesettings/%s" % self.entity)
        except IOError:
            print "No page settings saved for %ss." % self.entity
            return allData.data[0]
        return rules
