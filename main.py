from model.game import Game
from model.player import Player
from model.position import Position


def generate_board(size):
    # print("\n" * 130)

    board_matrix = []

    for line in range(size):
        line_array = []
        for col in range(size):
            line_array.append(Position(col + 1, line + 1))
        board_matrix.append(line_array)
    return board_matrix


def draw_board(board):
    print("   | ", end="")
    for i in range(len(board)):
        if i < 9:
            print("\u0332".join("  " + (i + 1).__str__() + " "), end=" | ")
        else:
            print("\u0332".join("  " + (i + 1).__str__() + " "), end="|")
    for i in range(len(board)):
        print()
        if i < 9:
            print(" ", end="")
        print((i + 1).__str__() + " |", end="")

        for position in board[i]:
            print("  " + position.player, end="  |")
    print()
    print()


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
        players.append(Player(player_name))

        # verifica se o tamanho do tabuleiro é 3 e se tem 2 jogadores e continua o jogo, fica impossivel
        # jogar com mais de dois jogadores no mesmo tabuleiro
        if board_size.__eq__(3) and len(players).__eq__(2):
            break

        if board_size > 3 and len(players) >= 2:
            more = input('Continuar(S/N)? ')
            if more.upper().__eq__("N"):
                break

    board = generate_board(board_size)
    return Game(players, board)


def check_winner(plays, board):
    if plays > 2 * plays:
        return "vai"


def play(game, turn):
    board_size = len(game.board)
    board = game.board
    player = game.players[turn]
    valid_play = False
    position = Position(0, 0)

    while not valid_play:
        line = int(input('Número da linha: '))
        col = int(input('Número da coluna: '))
        if line <= board_size and col <= board_size:
            position = board[line - 1][col - 1]
            if position.empty():
                position.player = player.initials()
                board[line - 1][col - 1] = position
                valid_play = True
            else:
                print("Jogada Inválida, preenchido por: " + position.player)
        else:
            print("Jogada inválida, esolha um número de 1 até " + board_size.__str__())
    return [board, position]


def check_for_winner(plays: int, board, position: Position):
    if plays >= 99:  # checar vencedor retornor postion com o nome do vencedor
        return position

    elif plays >= (len(board) * len(board)):
        return Position(0, 0, None)

    return Position(0, 0)


def begin(game):
    winner = None
    turn = 0
    plays = 0

    while winner is None:
        player = game.players[turn]
        print("Vez do Jogador: " + player.name)
        draw_board(game.board)
        [board, position] = play(game, turn)
        if turn < len(game.players) - 1:
            turn += 1
        else:
            turn = 0
        plays += 1

        wining_position = check_for_winner(plays, game.board, position)
        if wining_position.player is None:
            draw_board(game.board)
            print("Nenhum vencedor")
            break
        elif not wining_position.empty():
            draw_board(game.board)
            print("ganhou")
            break
    new_game()


def new_game():
    game = menu()
    begin(game)


def quit_or_restart(option: str):
    if option.upper().__eq__("sair"):
        exit()
    elif option.upper().__eq__("reniciar"):
        new_game()


class Main:
    new_game()
