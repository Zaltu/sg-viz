from libs import json_reader, const

class Entity():

    def __init__(self, name, forcePull=False):
        self.name = self.sgname = name
        self._fetch(forcePull)



    def _fetch(self, forcePull):
        self.data = json_reader.getcomplexdata(self.name, const.ENTITY_PATH, forcePull)

