from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file('mexican_train_dominos.kv')


class MexicanTrainDominos(Screen):
    def start_game(self):
        self.ids.start_game.disabled = True
        self.ids.score_round.disabled = False
        self.ids.end_game.disabled = False
        self.ids.add_player.disabled = True
        self.ids.remove_player.disabled = True

    def end_game(self):
        self.ids.start_game.disabled = False
        self.ids.score_round.disabled = True
        self.ids.end_game.disabled = True
        self.ids.add_player.disabled = False
        self.ids.remove_player.disabled = False
    #     todo add a popup that askes if you are sure,
    #      if yes display the score and winner

    def score_round(self):
        ...

    def add_player(self):
        ...

    def remove_player(self):
        ...

    def save_score(self):
        ...
