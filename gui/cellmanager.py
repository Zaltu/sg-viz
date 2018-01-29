from PySide.QtGui import QWidget
from gui.cells import entity, text, multientity, thumbnail, checkbox, url


MAP = {
    'image':{'field':thumbnail.ThumbnailField, 'blank':None, 'save':thumbnail.save, 'edit':None},
    'entity':{'field':entity.EntityField, 'blank':None, 'save':entity.save, 'edit':None},
    'multi_entity':{'field':multientity.MultiEntityField, 'blank':None, 'save':multientity.save, 'edit':None},
    'text':{'field':text.TextField, 'blank':None, 'save':text.save, 'edit':text.edit},
    'checkbox':{'field':checkbox.CheckBoxField, 'blank':None, 'save':checkbox.save, 'edit':None},
    'url':{'field':url.FileField, 'blank':None, 'save':url.save, 'edit':None},
    'DEFAULT':{'field':None, 'blank':None, 'save':None, 'edit':None}
}



def barfCell(field, mainframe=None):
    writen = field['value']

    ops = MAP.get(field['type'], MAP["text"])

    # Allows view to change when entity buttons are clicked
    if field['type'] in ['entity', 'multi_entity']:
        ops['extra'] = mainframe

    if writen not in ["None", "", None, [], {}] and ops['field']:
        return ops['field'](writen, ops)
    return ops['blank']


def edit(cell):
    if cell and cell.ops['edit']:
        return cell.ops['edit'](cell)
    return None


def save(cell):
    if cell.ops['save']:
        return cell.ops['save'](cell)
    return None