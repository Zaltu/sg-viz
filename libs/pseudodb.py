from src.entity import Entity

class DataBase():

    def __init__(self):
        self.loadedents = {}


    def get(self, entity):
        if entity not in self.loadedents:
            self.loadedents[entity] = Entity(entity)
        return self.loadedents[entity]
