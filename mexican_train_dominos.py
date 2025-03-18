from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_file('mexican_train_dominos.kv')


class MexicanTrainDominos(Screen):
    max_players = 8
    # players = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.players = []  # List of player dictionaries
    #     #Clock.schedule_once(self.initialize_ui)

    # def initialize_ui(self):
    #     """Ensures self.ids is initialized before modifying widgets."""
    #     self.players_grid = self.ids.get('players_grid')

    def add_player(self):
        """Adds a new player to the scorboard (max 8)."""
        if len(self.players) < self.max_players:
            player_number = len(self.players) + 1
            # player_data = {
            #     'name': TextInput(hint_text=f'Player {player_number}', size_hint_y=None, height=40),
            #     'scores': [TextInput(hint_text='0', size_hint_y=None, height=40) for _ in range(13)],
            #     'total': Label(text='0', size_hint_y=None, height=40)
            # }
            #
            # # Add player's name to the first column
            # self.ids.player_grid.add_widget(player_data['name'])
            #
            # #  Add 13 score inputs for rounds
            # for score_input in player_data['scores']:
            #     self.ids.players_grid.add_widget(score_input)
            #
            # #  Add final score column
            # self.ids.players_grid.add_widget(player_data['total'])
            #
            # self.players.append(player_data)

            player_box = BoxLayout(orientation='vertical', size_hint_y=None, height=50)
            player_label = Label(text=f'Player {len(self.players) + 1}', size_hint_y=None, height=20)
            player_input = TextInput(hint_text='Enter Name: ', size_hint_y=None, height=30)

            player_box.add_widget(player_label)
            player_box.add_widget(player_input)
            self.ids.players_grid.add_widget(player_box)

            self.players.append(player_box)

    def add_player_popup(self):
        ...

    def remove_player(self):
        """Removes the last added player."""
        if self.players:
            player_box = self.players.pop()
            self.ids.players_grid.remove_widget(player_box)

            # Remove all widgets related to the player
            # player_data = self.players.pop()
            # self.ids.players_grid.remove_widget(player_data['name'])
            # for score_input in player_data['scores']:
            #     self.ids.players_grid.remove_widget(score_input)
            # self.ids.players_grid.remove_widget(player_data['total'])

    def start_game(self):
        """Disables player management and enables game controls."""
        self.ids.start_game.disabled = True
        self.ids.score_round.disabled = False
        self.ids.end_game.disabled = False
        self.ids.add_player.disabled = True
        self.ids.remove_player.disabled = True

    def confirm_end_game(self):
        """Shows a confirmation popup before ending the game."""
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text='Are you sure you want to end the game?'))

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        yes_btn = Button(text='Yes', on_release=lambda *args: self.end_game(popup))
        no_btn = Button(text='No', on_release=lambda *args: popup.dismiss())

        btn_layout.add_widget(yes_btn)
        btn_layout.add_widget(no_btn)
        content.add_widget(btn_layout)

        popup = Popup(title='Confirm End Game', content=content, size_hint=(0.6, 0.4))
        popup.open()

    def end_game(self, popup):
        # self.ids.start_game.disabled = False
        # self.ids.score_round.disabled = True
        # self.ids.end_game.disabled = True
        # self.ids.add_player.disabled = False
        # self.ids.remove_player.disabled = False
        """Resets the game and re-enables player management."""
        popup.dismiss()
        self.ids.start_game.disabled = False
        self.ids.score_round.disabled = True
        self.ids.end_game.disabled = True
        self.ids.add_player.disabled = False
        self.ids.remove_player.disabled = False
    #     todo Display final scores and winner
        # Clear players list and UI
        self.players.clear()
        self.ids.players_grid.clear_widgets()

    def score_round(self):
        """Handles scoring logic (to be implemented)."""
        for player in self.players:
            try:
                total_score = sum(int(score.text) if score.text.isdigit() else 0 for score in player['scores'])
                player['total'].text = str(total_score)
            except ValueError:
                player['total'].text = 'Error'

    def save_score(self):
        ...
