class Hive:

    def __init__(self, id_, location_=None, name_=None):
        self.id = id_
        self.location = location_
        self.name = name_

    def set_id(self, id_):
        self.id = id_
        return

    def get_id(self):
        return self.id

    def set_location(self, location_):
        self.location = location_
        return

    def get_location(self):
        return self.location

    def set_name(self, name_):
        self.name = name_
        return

    def get_name(self):
        return self.name