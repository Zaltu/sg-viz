from libs import json_reader, const

class Entity():

    def __init__(self, name):
        self.name = self.sgname = name
        self._fetch()


    def _fetch(self):
        self.data = json_reader.getcomplexdata(self.name, const.ENTITY_PATH)
