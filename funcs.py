from random import randint


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
    # print('transpose')
    # print(*list(map(list, zip(*field))), sep='\n')
    return list(map(list, zip(*field)))


def reverse(some_list):
    # print('reverse')
    # print(*list(map(lambda arr: arr[::-1], some_list)), sep='\n')
    return list(map(lambda arr: arr[::-1], some_list))


def swipe_and_sum(col_or_row):
    swiped_col_or_row = []
    col_or_row_iter = iter(col_or_row)
    curr_cell = next(col_or_row_iter)
    for next_cell in col_or_row_iter:
        if next_cell == curr_cell:
            swiped_col_or_row.append(curr_cell + next_cell)
            curr_cell = next(col_or_row_iter, NULL)
        elif curr_cell == NULL:
            curr_cell = next_cell
            continue
        else:
            swiped_col_or_row.append(curr_cell)
            curr_cell = next_cell
    else:
        swiped_col_or_row.append(curr_cell)

    for waifu in range(len(col_or_row) - len(swiped_col_or_row)):
        swiped_col_or_row.append(NULL)

    return swiped_col_or_row


def transpose_and_or_reverse(field, transpose_field, reverse_field):
    print({
        (True, True): reverse(transpose(field)),
        (True, False): transpose(field),
        (False, True): field[::-1],
        (False, False): field,
    }.get((transpose_field, reverse_field)), sep='\n')
    return {
        (True, True): reverse(transpose(field)),
        (True, False): transpose(field),
        (False, True): field[::-1],
        (False, False): field,
    }.get((transpose_field, reverse_field))


# def transpose_and_reverse(curr_move):
#     if curr_move in (UP, DOWN):
#         # Field transpose.
#         field_cols_or_rows = map(list, zip(*field))
#     else:
#         field_cols_or_rows = field
#
#     if curr_move in (DOWN, RIGHT):
#         field_cols_or_rows = map(reversed, field_cols_or_rows)


# def detranspose_and_reverse()


def print_info(field):
    print(*field, sep='\n')
    print('use W A S D to move the field\n')
