win_cells = [
    # diagonals
    {x for x in range(0, 9, 4)},
    {x for x in range(2, 7, 2)},
]

# horizontal
win_cells.extend([{x for x in range(i, i + 3)} for i in range(0, 7, 3)])
# vertical
win_cells.extend([{x for x in range(i, i + 7, 3)} for i in range(0, 3)])

state_plane = [None for _ in range(9)]
state_planes = [[]]

# field states / marks for players
player1 = True
player2 = False

# mappings
player_mapping = {player1: "Player 1", player2: "Player 2"}
win_mapping = {player1: 1, player2: -1, 0: "Nobody!"}

state_to_player_map = {}


def check_current_player(current_state: list[bool]) -> bool:
    moves = 0
    for cell in current_state:
        if cell is not None:
            moves += 1

    modulo = moves % 2
    return False if modulo == 1 else True


def check_player_won(player: bool, current_state: list[bool]) -> int | None:
    """
    0 if draw, else True or False
    """
    single_player_cells = {
        index for index, cell in enumerate(current_state) if cell == player
    }
    for win_cell in win_cells:
        if len(single_player_cells.intersection(win_cell)) == 3:
            return 1 if player else -1

    if all(cell is not None for cell in current_state):
        return 0


def get_available_moves(current_state: list[bool]) -> list[int]:
    moves = []
    for index, cell in enumerate(current_state):
        if cell is None:
            moves.append(index)

    return moves


def make_move(index: int, player: bool, current_state: list[bool]) -> bool:
    current_state[index] = player
    return current_state


def draw_board(current_state):
    plane = [f"{i}" for i in range(9)]
    for index, player in enumerate(current_state):
        if player is not None:
            plane[index] = "X" if player else "O"

    for i in range(0, 7, 3):
        print(plane[i : i + 3])


def min_max(current_state: list[bool], move: int | None):
    current_player = check_current_player(current_state)

    if move:
        current_state = make_move(move, current_player, current_state)
    print("\n")
    draw_board(current_state)
    print(current_player)
    print(move)

    if (win_value := check_player_won(current_player, current_state)) is not None:
        print(win_value)
        return win_value

    available_moves = get_available_moves(current_state)

    next_states = []
    for move in available_moves:
        next_states.append(min_max(current_state.copy(), move))

    if current_player:
        return max(next_states)
    else:
        return min(next_states)


test_list = [False, True, False, None, True, True, None, False, True]
print(min_max(test_list, None))


def game_loop():
    # reference from above, because this is python things
    current_player = True
    game_over = False
    winner = None

    while not game_over:
        draw_board()
        index_input = int(input(f"Index move for {player_mapping[current_player]}: "))
        if not (0 <= index_input <= 8):
            print("Index out of range, not allowed")
            continue

        if not make_move(index_input, current_player):
            print("This cell isn't empty. Choose another one")
            continue

        if (winner_number := check_player_won(current_player)) is not None:
            print(winner_number)
            if winner_number == 0:
                winner = "Nobody..."
            else:
                winner = player_mapping[current_player]
            game_over = True

        current_player = not current_player

    draw_board()
    print(f"{winner} won the game!")


# game_loop()
