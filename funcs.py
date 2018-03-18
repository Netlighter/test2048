from random import randint
import copy


NULL = 0


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


def print_info(field):
    field = list(map(list, field))
    print('--------------------')
    print(*field, sep='\n')
    print('--------------------')
    print('use W A S D to move the field')
    print('--------------------')
