class Location:

    def __init__(self, lat, long):
        self.latitude = lat
        self.longitude = long

    def set_latitude(self, lat):
        self.latitude = lat
        return

    def get_latitude(self):
        return self.latitude

    def set_longitude(self, long):
        self.longitude = long
        return

    def get_longitude(self):
        return self.longitude
