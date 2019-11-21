class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def initials(self):
        return self.name[:2].upper()
