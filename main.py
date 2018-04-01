import os

import kivy
from kivy.uix.button import Label, Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.config import Config

import funcs


Builder.load_file(os.path.join('kv_config.kv'))

kivy.require('1.0.8')

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)
Config.write()
Window.size = (550, 550)


# Custom class to not override global Label styles in .kv files.
class Cell(Label):
    pass


class GameFieldWidget(GridLayout):
    def __init__(self, game_field_matrix, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.look_for_game_win_state = True

        self.game_field_matrix = game_field_matrix
        self.generate_random_number()
        self.generate_random_number()
        for label_text in funcs.to_one_dim(self.game_field_matrix):
            self.add_widget(Cell(text=str(label_text)))

    def generate_random_number(self):
        self.game_field_matrix = funcs.generate_number_in_free_cell(
            self.game_field_matrix, [2, 2, 2, 2, 4])

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        key_str = keycode[1]

        if not funcs.check_possibility_to_move(self.game_field_matrix):
            popup = ModalView(
                size_hint=(None, None),
                size=(200, 50),
                background_color=(1, .7, .2, .4))
            popup.add_widget(Button(
                text='You LOSE!',
                font_size='25sp',
                background_color=(1, .7, .2, 1)))
            popup.open()
            keyboard.release()

        state, updated_field = funcs.process_game_step(
            self.game_field_matrix, key_str)
        if state != funcs.WRONG_USER_INPUT:
            self.game_field_matrix = updated_field
            self.generate_random_number()
            updated_field = funcs.to_one_dim(self.game_field_matrix)[::-1]
            for index in range(len(updated_field)):
                self.children[index].text = str(updated_field[index])

        if self.look_for_game_win_state and state == funcs.GAME_WON:
            self.look_for_game_win_state = False
            popup = ModalView(
                size_hint=(None, None),
                size=(200, 50),
                background_color=(1, .7, .2, .4))
            popup.add_widget(Button(
                text='You WON!',
                font_size='25sp',
                background_color=(1, .7, .2, 1)))
            popup.open()

        return True


if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(GameFieldWidget(
        game_field_matrix=[
            [funcs.NULL, funcs.NULL, funcs.NULL, funcs.NULL],
            [funcs.NULL, funcs.NULL, funcs.NULL, funcs.NULL],
            [funcs.NULL, funcs.NULL, funcs.NULL, funcs.NULL],
            [funcs.NULL, funcs.NULL, funcs.NULL, funcs.NULL],
        ],
        cols=4))
