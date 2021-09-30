from pprint import pprint as pp
import os
from shotgun_api3 import Shotgun
from libs import const


def getentitydatafromshotgun():
    sg = Shotgun(const.SHOTGUN_URL, const.API_NAME, const.API_KEY)
    entityData = sg.schema_entity_read({'type':'Project', 'id':70})
    visibleEntities = []
    for entityName in entityData:
        fields = sg.schema_field_read(entityName)
        if 'project' in fields:
            if entityData[entityName]['visible']['value']:
                visibleEntities.append(entityData[entityName]['name']['value'])
                print("\""+entityData[entityName]['name']['value']+"\": \"" + entityName + "\",")
    return visibleEntities


def getentitiesfromshotgun(name):
    sg = Shotgun(const.SHOTGUN_URL, const.API_NAME, const.API_KEY)
    sgname = name
    if name in const.ENTITY_MAP:
        sgname = const.ENTITY_MAP[name]
    fields = sg.schema_field_read(sgname)
    rawents = sg.find(sgname, [['project', 'is', {'type':'Project', 'id':70}]], list(fields.keys()))
    pp(rawents)
    clean = []
    for ent in rawents:

        if 'image' in ent and ent['image']:
            directory = "data/filestorage/%s/%s/%s" % (name, ent['id'], "image")
            if not os.path.exists(os.path.dirname(directory)):
                os.makedirs(os.path.dirname(directory))
            sg.download_attachment({'url':ent['image']}, directory)
            ent['image'] = directory
        for field in fields:
            if fields[field]['data_type']['value'] == 'url' and ent[field]:
                pp(ent)
                directory = "data/filestorage/%s/%s/%s" % (name, ent['id'], ent[field]['name'])
                if not isinstance(ent['id'], int):
                    directory = "data/filestorage/%s/%s/%s" % (name, ent['id']['value'], ent[field]['name'])
                if not os.path.exists(os.path.dirname(directory)):
                    os.makedirs(os.path.dirname(directory))
                sg.download_attachment(ent[field], directory)
                ent[field] = directory

            ent[field] = {"value":ent[field], "type":fields[field]['data_type']['value']}

        ent.pop("created_at", None)
        ent.pop("created_by", None)
        ent.pop("updated_at", None)
        ent.pop("updated_by", None)
        ent.pop("filmstrip_image", None)
        ent.pop("cached_display_name", None)

        dic = {}
        dic['type'] = {'type':'text', 'value':ent.pop('type')}
        for f in ent:
            dic[fields[f]['name']['value']] = ent[f]

        clean.append(dic)

    return clean
