from model.position import Position


def draw_board(size):
    # print("\n" * 130)

    board_matrix = []

    for column in range(size):
        line_array = []
        for line in range(size):
            line_array.append(Position(column + 1, line + 1, None))
        board_matrix.append(line_array)

    for line in board_matrix:
        for col in line:
            print(col)


def print_info():
    print('''Entre respectivamente o tamanho da quadra que voce quer usar, um valor de 3 a 10, 
    e o qantidade de jogadores que vao jogar. Minimo 2, maximo 5.
    Número de jogadores: ''')


def check_winner(plays, board):
    if plays > 2 * plays:
        return "vai"


def player_request(plays, board):
    if plays > 2 * plays:
        return "vai"


class Main:
    print_info()
    plays = 0

    def __init__(self):
        position = Position(1, 2, 3)
        position.__str__()

    draw_board(3)
