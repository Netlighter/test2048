# cd /mnt/c/Users/NetLight/Desktop/pythoshik/2048
# cd /home/netlight/Desktop/projects/py3/test2048
from random import randint
import copy


NULL = 0

WRONG_USER_INPUT = 'wrong_user_input'
FINE_STATE = 'fine_state'
GAME_END = 'game_end'


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


def to_one_dim(field):
    one_dim_field = []
    for row in field:
        one_dim_field.extend(row)
    return one_dim_field


def find_free_cells(field):
    free_cells_list = []

    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == NULL:
                free_cells_list.append([y, x])

    return free_cells_list


def rand_el_from_list(search_list):
    return search_list[randint(0, len(search_list) - 1)]


def transpose(field):
    return map(list, zip(*field))


def reverse(some_list):
    return map(lambda arr: arr[::-1], some_list)


def generate_number_in_free_cell(field, numbers_list):
    field_copy = copy.deepcopy(field)
    free_cells_list = find_free_cells(field_copy)
    number_to_generate = rand_el_from_list(numbers_list)
    y, x = rand_el_from_list(free_cells_list)
    field_copy[y][x] = number_to_generate
    return field_copy


def swipe_and_sum(col_or_row):
    swiped_col_or_row = []
    cells_were_summed = False
    for number in col_or_row:
        if number == NULL:
            continue
        elif (swiped_col_or_row != [] and number == swiped_col_or_row[-1] and
                not cells_were_summed):
            swiped_col_or_row[-1] += number
            cells_were_summed = True
        else:
            cells_were_summed = False
            swiped_col_or_row.append(number)

    for waifu in range(len(col_or_row) - len(swiped_col_or_row)):
        swiped_col_or_row.append(NULL)

    return swiped_col_or_row


def process_game_step(field, user_input):
    if user_input not in WAYS.keys():
        return WRONG_USER_INPUT, field

    need_to_transpose_field = False
    need_to_reverse_field = False
    new_field_state = field
    if WAYS[user_input] in (UP, DOWN):
        need_to_transpose_field = True
    if WAYS[user_input] in (DOWN, RIGHT):
        need_to_reverse_field = True

    if need_to_transpose_field:
        new_field_state = transpose(new_field_state)
    if need_to_reverse_field:
        new_field_state = reverse(new_field_state)

    new_field_state = map(swipe_and_sum, new_field_state)

    if need_to_reverse_field:
        new_field_state = reverse(new_field_state)
    if need_to_transpose_field:
        new_field_state = transpose(new_field_state)

    field = list(map(list, new_field_state))
    if (any(filter(lambda cols_or_row: 2048 in cols_or_row, field)) or
            not find_free_cells(field)):
        return GAME_END, field

    return FINE_STATE, field
