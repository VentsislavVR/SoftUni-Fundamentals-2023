class Town:
    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude):
        pass

    def set_longitude(self, longitude):
        pass

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {latitude} | Longitude: {longitude}"
