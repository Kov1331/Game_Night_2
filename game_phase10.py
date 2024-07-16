from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file("game_phase10.kv")


class Phase10(Screen):

    def add_player(self):
        self.ids.players.add_widget(self.player_row())

    def remove_player(self):
        print('Remove Player')
        self.ids.players.remove_widget(self.player_row()) # todo does not work

    def check_button(self):
        check_button = Button()
        # todo on_release text='X'
        return check_button

    def score_button(self):
        score_button = Button(text='0')
        self.on_release(TextInput.text)
        return score_button

    def check(self):
        ...

    def reset_game(self):
        self.ids.players.clear_widgets()


    def add_score(self):
        score_0 = self.text
        print(score_0)

    def player_row(self):
        player_layout = BoxLayout(orientation='vertical')

        name_row = GridLayout(cols=2, rows=1, size_hint=(1, .25))
        name_row.add_widget(TextInput())
        name_row.add_widget(TextInput())

        player_row = GridLayout(cols=11, rows=1, size_hint=(1, .25))
        for i in range(10):
            player_row.add_widget(self.check_button())
        player_row.add_widget(self.score_button())

        player_layout.add_widget(name_row)
        player_layout.add_widget(player_row)

        return player_layout
