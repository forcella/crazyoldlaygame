class Position:
    def __init__(self, col, line, player="--"):
        self.col = col
        self.line = line
        self.player = player

    def empty(self):
        return self.player.__eq__('--')

    def check_player_eq(self, first, second):
        first: Position
        second: Position
        return self.player.__eq__(first.player) and self.player.__eq__(second.player)
