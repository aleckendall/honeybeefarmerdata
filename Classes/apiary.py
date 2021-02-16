class Apiary:

    def __init__(self, id_, location_, name_=None, hives_=[]):
        self.id = id_
        self.location = location_
        self.name = name_
        self.hives = hives_

    def set_id(self, id_):
        self.id = id_
        return

    def get_id(self):
        return self.id

    def set_location(self, loc):
        self.location = loc
        return
    
    def get_location(self):
        return self.location

    def set_name(self, name_):
        self.name = name_
        return
    
    def get_name(self):
        return self.name

    def set_hives(self, hives_):
        self.hives = hives_
        return

    def get_hives(self):
        return self.hives