class Player:
    def __init__(self, name):
        self.name = name

    def initials(self):
        return self.name[:2].upper()
