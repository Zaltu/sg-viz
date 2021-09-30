from PySide2.QtWidgets import QCheckBox, QWidget
from libs.const import ENTITY_REVERSE_MAP
import gui

class CheckBoxField(QCheckBox):

    def __init__(self, checked, ops):
        self.checked = checked
        self.ops = ops
        QCheckBox.__init__(self)
        if checked:
            self.toggle()


def save(entity):
    pass
