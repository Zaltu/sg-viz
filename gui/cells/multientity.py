from PySide.QtGui import QPushButton, QWidget, QGridLayout
from gui.cells.entity import EntityField

class MultiEntityField(QWidget):

    def __init__(self, entities, ops):
        self.entities = entities
        self.ops = ops
        QWidget.__init__(self)

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        if not entities:
            entities = []
        for entity in entities:
            self.layout.addWidget(EntityField(entity, ops))


    def edit(self):
        return None


def save(multientity):
    pass