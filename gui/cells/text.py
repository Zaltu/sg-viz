from PySide2.QtWidgets import QTextEdit, QLabel


class TextField(QLabel):

    def __init__(self, text, ops):
        QLabel.__init__(self, str(text))
        self.text = str(text)
        self.ops = ops



class EditTextField(QTextEdit):

    def __init__(self, text, ops):
        QTextEdit.__init__(self, text)
        self.text = text
        self.ops = ops



def save(textfieldcell):
    return TextField(textfieldcell.toPlainText(), textfieldcell.ops)


def edit(textfieldcell):
    return EditTextField(textfieldcell.text, textfieldcell.ops)
