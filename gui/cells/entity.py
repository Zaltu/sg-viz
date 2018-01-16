from PySide.QtGui import QPushButton, QWidget
from libs.const import ENTITY_REVERSE_MAP
import gui

class EntityField(QPushButton):

    def __init__(self, entity, ops):
        if not entity:
            entity = {}
        self.entity = entity
        self.ops = ops
        self.displayname = entity.get('name') or entity.get('code') or entity.get('content') or self.getDisplayName()
        QPushButton.__init__(self, self.displayname)
        self.clicked.connect(lambda e=ops['extra']: self._goSeeEntity(e))
        # TODO
        #self.setStyleSheet(entsheet)


    def _goSeeEntity(self, parent):
        parent.parent.changeState(gui.entityviewer.EntityViewer(parent, ENTITY_REVERSE_MAP[self.entity['type']]))


    # TODO
    def getDisplayName(self):
        return ""


    def edit(self):
        return None


class EditEntityField():
    pass



def save(entity):
    pass
