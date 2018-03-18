# cd /mnt/c/Users/NetLight/Desktop/pythoshik/2048
import funcs


NULL = 0
CELL_2 = 2

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]
WAYS = {
    'w': UP,
    's': DOWN,
    'a': LEFT,
    'd': RIGHT, }

field = [
    [NULL, NULL, NULL, NULL],
    [NULL, NULL, NULL, NULL],
    [NULL, NULL, NULL, NULL],
    [NULL, NULL, NULL, NULL],
]


field = funcs.generate_number_in_free_cell(field, [2, 2, 2, 4])

is_game_end = False
while not is_game_end:
    field = funcs.generate_number_in_free_cell(field, [1024, 2, 2, 4])
    funcs.print_info(field)

    curr_move = input('make move: ').lower()
    if curr_move not in WAYS.keys():
        print('Wrong user input.')
        continue

    need_to_transpose_field = False
    need_to_reverse_field = False
    new_field_state = field
    if WAYS[curr_move] in (UP, DOWN):
        need_to_transpose_field = True
    if WAYS[curr_move] in (DOWN, RIGHT):
        need_to_reverse_field = True

    if need_to_transpose_field:
        new_field_state = funcs.transpose(new_field_state)
    if need_to_reverse_field:
        new_field_state = funcs.reverse(new_field_state)

    new_field_state = map(funcs.swipe_and_sum, new_field_state)

    if need_to_reverse_field:
        new_field_state = funcs.reverse(new_field_state)
    if need_to_transpose_field:
        new_field_state = funcs.transpose(new_field_state)

    field = list(map(list, new_field_state))
    is_game_end = (
        any(filter(lambda cols_or_row: 2048 in cols_or_row, field)) or
        not funcs.find_free_cells(field))

print('--------------------')
print('Nice Work!', sep='\n')
print(*field, sep='\n')
print('--------------------')
