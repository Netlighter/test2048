#cd /mnt/c/Users/NetLight/Desktop/pythoshik/2048
from random import randint
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


free_cells_list = funcs.find_free_cells(field)
x1, y1 = funcs.rand_el_from_list(free_cells_list)
field[y1][x1] = CELL_2

is_game_end = False
while not is_game_end:
    funcs.print_info(field)

    curr_move = input('make move: ')
    if curr_move not in WAYS.keys():
        print('Wrong user input.')
        continue

    need_to_transpose_field = False
    need_to_reverse_field = False
    if curr_move in ['w', 's']:
        print('make transpose')
        need_to_transpose_field = True
    if curr_move in ['s', 'd']:
        print('make reverse')
        need_to_reverse_field = True

    transpose_or_reversed_field = funcs.transpose_and_or_reverse(
        field,
        need_to_transpose_field,
        need_to_reverse_field)

    updated_field = list(map(funcs.swipe_and_sum, transpose_or_reversed_field))

    field = funcs.transpose_and_or_reverse(
        updated_field,
        need_to_transpose_field,
        need_to_reverse_field)

    is_game_end = any(filter(lambda cols_or_row: 2048 in cols_or_row, field))


# открывает программу
#
# инициализация:
#   библиотеки
#   константы
#   переменные
#
# главный игровой цикл:
#   вывод на экран
#   пользовательский ввод
#   обработка ввода:
#     определяем направление
#     сдвигаем числа & суммируем числа по направлению:
#       только ближайшие
#   recur
#
#
# завершение










#i spizdil this from github URL
