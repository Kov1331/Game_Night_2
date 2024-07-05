from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file("game_phase10.kv")


class Phase10(Screen):

    def add_player(self):
        ...

    def check_button(self):
        if self.text == '':
            self.text = 'X'
        else:
            self.text = '' # todo fix this error?

    def reset_game(self):
        ...

    def add_score(self):
        score_0 = self.text
        print(score_0)
