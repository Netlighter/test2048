import kivy
from kivy.uix.button import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import funcs
from kivy.lang.builder import Builder
from kivy.config import Config

Builder.load_file('/home/netlight/Desktop/projects/py3/test2048/kv_config.kv')

kivy.require('1.0.8')

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)
Config.write()
Window.size = (550, 550)


class GameFieldWidget(GridLayout):
    def __init__(self, game_field_matrix, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.game_field_matrix = game_field_matrix
        self.generate_random_number()
        self.generate_random_number()
        for label_text in funcs.to_one_dim(self.game_field_matrix):
            self.add_widget(Label(text=str(label_text)))

    def generate_random_number(self):
        self.game_field_matrix = funcs.generate_number_in_free_cell(
            self.game_field_matrix, [2, 2, 2, 4])

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        key_str = keycode[1]

        state, updated_field = funcs.process_game_step(
            self.game_field_matrix, key_str)
        if state == funcs.FINE_STATE:
            self.game_field_matrix = updated_field
            self.generate_random_number()
            updated_field = funcs.to_one_dim(self.game_field_matrix)[::-1]
            for index in range(len(updated_field)):
                self.children[index].text = str(updated_field[index])

        if key_str == 'escape':
            keyboard.release()
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
