class Asset:
    def __init__(self, thumbnail, name):
        self.thumbnail = thumbnail
        self.name = name

    def getName(self):
        return self.name

    def getThumbnail(self):
        return self.thumbnail
        
