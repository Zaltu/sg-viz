from PySide.QtGui import QLabel, QPixmap, QIcon
from libs import json_reader
import os

class ThumbnailField(QLabel):

    def __init__(self, path, ops):
        QLabel.__init__(self)
        if path:
            pix = QPixmap(path)
            self.setPixmap(pix)#json_reader.buildPath(QPixmap(path).scaled(100, 100))
            self.path = path
            self.ops = ops


    def edit(self):
        return None


#TODO
class EditThumbnailField(QLabel):

    def __init__(self, text):
        QLabel.__init__(self, text)
        self.text = text


    def save(self):
        #TODO
        return ThumbnailField(self.getText())


def save(thumb):
    pass
