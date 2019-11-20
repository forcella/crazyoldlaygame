class Position:
    def __init__(self, column, line, player):
        self.column = column
        self.line = line
        self.player = player

    def __str__(self):
        return str(self.__dict__)
