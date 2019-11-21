from model.game import Game
from model.player import Player
from model.position import Position


def generate_board(size):
    # print("\n" * 130)

    board_matrix = []

    for line in range(size):
        line_array = []
        for col in range(size):
            line_array.append(Position(col + 1, line + 1, "--"))
        board_matrix.append(line_array)
    return board_matrix


def draw_board(board):
    print("   | ", end="")
    for i in range(len(board)):
        if i < 9:
            print("\u0332".join("  " + (i + 1).__str__() + " "), end=" |")
        else:
            print("\u0332".join(" " + (i + 1).__str__() + " "), end=" |")
    for i in range(len(board)):
        print()
        if i < 9:
            print(" ", end="")
        print((i + 1).__str__() + " | ", end="")

        for position in board[i]:
            print(" " + position.player, end="  |")


def menu():
    players = []
    print('''Entre respectivamente o tamanho da quadra que voce quer usar, um valor de 3 a 10, 
    e o qantidade de jogadores que vao jogar. Minimo 2, maximo 5, para sair digite sair a qualquer momento''')

    while True:
        board_size = int(input('Tamanho do tabuleiro: '))
        if 2 < board_size <= 10:
            break

    while True:
        pos = len(players)
        player_name = input('Nome do jogador ' + (pos + 1).__str__() + ": ")
        players.append(Player(player_name, pos))
        more = input('Continuar(S/N)? ')
        if more.upper().__eq__("N"):
            break

    board = generate_board(board_size)
    return Game(players, board)


def check_winner(plays, board):
    if plays > 2 * plays:
        return "vai"


def play(player: Player, board, line, col):
    board_size = len(board)
    if line < board_size and col < board_size:
        position = board[line - 1][col - 1]
        position: Position
        if position.player.__eq__('--'):
            position.player = player.initials()
            board[line - 1][col - 1] = position
        else:
            print("Jogada Inválida, preenchido por:" + position.player)
    else:
        print("Jogada inválida, esolha um número de 1 até " + board_size.__str__())
    return board


def check_for_winner(plays: int, board, position: Position):
    if plays <= len(board):
        return "can play"
    else:
        return "end game"


def begin(game):
    draw_board(game.board)


class Main:
    game = menu()
    begin(game)
    