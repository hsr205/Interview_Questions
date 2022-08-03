board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]


def game_conditionals(list_obj):
    if list_obj[0] == 'X' or list_obj[0] == 'O':
        if len(list_obj) == 1:
            print('Game win!')
            return


def diagonal_conditionals(game_board):
    result = []
    for i in range(3):
        diagonal = [item[i] for item in game_board][i]
        result.append(diagonal)
    diagonal = list(set(result))

    game_conditionals(diagonal)


def diagonal_win(game_board):
    diagonal_conditionals(game_board)

    game_board.reverse()

    diagonal_conditionals(game_board)


def is_win(game_board, col_row_num):
    column = list(set(item[col_row_num] for item in game_board))

    game_conditionals(column)

    row = list(set([item for item in game_board[col_row_num]]))

    game_conditionals(row)

    diagonal_win(game_board)


is_win(board, 0)
is_win(board, 1)
is_win(board, 2)
