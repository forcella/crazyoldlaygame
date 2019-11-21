class Position:
    def __init__(self, column, line, player="--"):
        self.column = column
        self.line = line
        self.player = player

    def empty(self):
        return self.player.__eq__('--')
