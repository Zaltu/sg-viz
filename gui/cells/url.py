from PySide.QtGui import QTextBrowser, QDesktopServices
import gui

class FileField(QTextBrowser):

    def __init__(self, url, ops):
        self.url = url
        self.ops = ops
        QTextBrowser.__init__(self)
        self.append('<a href="%s">%s</a>' % (url, url.split("/")[-1]))
        self.anchorClicked.connect(self._openFile)
        self.setOpenLinks(False)


    def  _openFile(self):
        QDesktopServices.openUrl(self.url)


def save(entity):
    pass
