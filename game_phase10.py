from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel

Builder.load_file("game_phase10.kv")


class Phase10(Screen):

    def add_player(self):
        self.ids.players.add_widget(self.player_row())

    def remove_player(self):  # may require instance
        print('Remove Player')
        self.ids.players.remove_widget(self.player_row())  # todo does not work

    def score_button(self, instance):
        score_button = Button(text='0')
        print(instance)
        return score_button

    def check_button(self):
        check_button = Button()
        check_button.bind(on_release=self.check)
        return check_button

    def check(self, instance):  # instance tells func which button to press
        if instance.text == '':
            instance.text = 'X'
        elif instance.text == 'X':
            instance.text = ''

    def reset_game(self):
        self.ids.players.clear_widgets()

    def add_score(self):
        score_0 = self.text
        print(score_0)

    def player_row(self):
        player_layout = BoxLayout(orientation='vertical')

        name_input = TextInput(multiline=False)
        score_input = TextInput(multiline=False)

        name_row = GridLayout(cols=2, rows=1, size_hint=(1, .25))
        name_row.add_widget(name_input)
        name_row.add_widget(score_input)

        player_row = GridLayout(cols=11, rows=1, size_hint=(1, .25))
        for i in range(10):
            player_row.add_widget(self.check_button())
        player_row.add_widget(self.score_button(self))

        player_layout.add_widget(name_row)
        player_layout.add_widget(player_row)

        return player_layout

    def rules(self):  # todo reformat to make look better
        return """
        DESCRIPTION:
        Phase 10 is played in a series of rounds in which players attempt to build combinations 
        of cards known as "Phases". When someone "goes out" by both playing a completed Phase and
        getting rid of their remaining cards, the round ends. If you didn't finish building your
        Phase before the round ended, you must try to build the same Phase again. The race is on
        to finish your 10th Phase first!
                
        OBJECTIVE:
        Be the first player to complete all 10 Phases.
        
        SETUP:
        Choose one player to be dealer. 
        The dealer places the two Phase Reference cards (which list the 10 Phases) where everyone can see them. 
        The dealer then shuffles the deck and deals 10 cards, face down, to each player. 
        
        Players can look at their cards but should hold them so other players can't see them. 
        
        Place the remaining deck face down in the center of the play area to form a draw pile.
        Turn the top card of the draw pile over and place it beside the draw pile to start a discard pile.
        The player to the left of the dealere goes first. Play proceeds in a clockwise direction.
        
        LET'S PLAY:
        Each player's turn followns these four steps:
            1. Draw a card.
            2. Lay down a Phase (if possible)
            3. Play cards on completed Phases by "hitting" (if possible)
            4. End your turn by discarding one card.
        We will look at each step in detail below.
                
        STEP 1:
        On your turn, draw one card, either the top card from the draw pile or the top card from the discard 
        pile, and add it to your hand.
        
        STEP 2:
        If you are able to make a Phase with the cards in your hand, lay the Phase down, face-up on the table.
        Each player can only make one Phase per round. During the first round, all players try to complete 
        Phase 1.
        
        What is a Phase?
        A Phase is a combination of cards made up of sets, runs, cards of all one color, or a combination thereof.
        
        DEFINITIONS:
        SETS: A set is make of two or more cards with the same number, in any combination of colors.
        EXAMPLE: Phase 1 is "2 sets of 3", which could be three 7s and three 10s. The two sets could also be 
        the same number, e.g., three 10s and three more 10s.
        
        RUNS: A run is made of four or more cards numbered in consecutive order, in any combination of colors.
        EXAMPLE: Part of Phase 2 requires "1 run of 4", which could be 3, 4, 5, 6.
        
        ALL ONE COLOR: The cards are all the same color, but they do not need to be in numerical order.
        EXAMPLE: Phase 8 requires "7 cards of 1 color", which could be seven red cards or seven blue cards, etc.
        
        Phases are listed under the Phases tab.
        
        Making a Phase:
        -Phases must be made IN ORDER, from 1 to 10.
        -You can only make one Phase per round.
        -You must have the whole Phase in hand before laying it down.
        -You receive credit for makeing a Phase as soon as you lay it down (you do not need to win the round by 
        going out to advance to the next Phase).
        -If you fail to make a Phase before the round ends, you must try to make the same Phase again in the 
        next round.
        As a result, players may not all be working on the same Phase in the same round.
        EXAMPLE: You are trying to make Phase 1. You have three 5s and two 7s, and you draw another 7. You now 
        have "2 sets of 3", and you may lay them down. In the next round, you will begin working on Phase 2.
        
        SPECIAL CARDS:
        Wild Cards: A WILD card may be used in place of a number card or may be used as any color to complete 
        a Phase.
        EXAMPLE: A player wants to make a run of 4, but only has cards 3, 4, and 6. The player uses a WILD card as 
        a 5 to complete the run. Or, a player has 6 green cards, and uses a WILD card as a green card to complete 
        Phase 8.
        -Players can use as many WILD cards as they want when completeing a Phase, as long as tehy use at least one
        numbered card.
        -Once a WILD card has been played in a Phase, it cannot be removed from that Phase for the rest of the round.
        -If the dealer starts the discard pile with a WILD card, the card may be picked up by the first player.
        
        Skip Cards: SKIP cards have only one purpose, to cause another player to lose a turn. To use, simply discard
        the SKIP card on your turn by placing it in front of the player you've chosen to skip instead of placing it 
        on the discard pile. That player will be skipped on their next turn. When it is the skipped player's turn, 
        that player's only action is to take the SKIP card and place it on the discard pile. It is tne the next 
        player's turn.
        -Playing a SKIP card counts as a discard and ends your turn.
        -A SKIP card may never be picked up from the discard pile.
        -A SKIP card may necer be used in making a Phase.
        -If the dealer starts the discard pile with a SKIP card, the first player's first turn is automatically 
        skipped.
        -A SKIP card may not be played against a player with a SKIP card in front of them.
        
        STEP 3: HITTING
        After making a Phase, you must try to get rid of any cards that remain in your hand so you can go out and win
        the round, which ends the round for everyone (see GOING OUT below). Hitting is how you do this. As soon as you
        have made your Phase, you may "hit" by putting a card or cards from your hand directly on any matching Phase
        that has been laid down.
        -Before you can make a hit, your own Phase must already be laid down.
        -You may hit only during your turn.
        -You may hit your own cards, another player's cards, or both, as long as the cards you play properly fit with
        the cards already laid down.
        EXAMPLE: You may add one or more 4s to any player's existing set of 4s. You may add a 2 to any player's 
        existing run of 3, 4, 5, 6. You may also add a 7 and an 8 to this run, if you have them. You may add one 
        or more green cards to a player's seven green cards in Phase 8. You may also add a WILD card to any of these 
        card situations.
        
        STEP 4: DISCARD ONE CARD TO END YOUR TURN
        End your turn by discarding one of your cards face up onto the top of the discard pile.
        
        GOING OUT (ENDING THE ROUND)
        After laying down a Phase, players try to "go out" as soon as possible. Going out ends the round for everyone.
        To go out, you must get rid of all your remaining cards by hitting on existing Phases, discarding your last 
        card onto the discard pile, or a combination of both. The player to go out first wins the round. The winner of 
        the round, and any other players who also completed their Phase, will advance to their next Phase on the next 
        round. Players total the cards left in their hands (the fewer cards left in your hand, the better!).
        
        Remember, if you did not complete the Phase before another player went out, you nust work on the same Phase 
        again during the next round.
        
        SCORING
        You will not need paper and pencil to keep a unning total due to this app. The winner of the round scores zero 
        (players wnat to get the lowest score). All remaining players score points against them for any cards still in 
        their hands, as follows:
        
        -5 points for each card numbered 1-9
        -10 points for each card numbered 10-12
        -15 points for each SKIP card
        25 points for each WILD card
        
        Only the cards in a player's hand are scored, not cards already laid down. After the scores are recorded, the 
        player to the left of the dealer becomes the new dealer. All cards are gathered and shuffled, and a new round 
        begins.
        
        WINNING THE GAME
        The first player to complete Phase 10 at the end of a round is the winner. If two or more players complete their 
        10th Phase in the same round, then the player with the fewest total points is the winner. In the event of a tie, 
        the players that tied replay the 10th Phase. The forst one to go out is the winner.
        """

    def phases(self):  # todo align phases to the left, ??add extra phases??
        return """
        Phases:
        1. 2 sets of 3
        2. 1 set of 3 + 1 run of 4
        3. 1 set of 4 + 1 run of 4
        4. 1 run of 7
        5. 1 run of 8
        6. 1 run of 9
        7. 2 sets of 4
        8. 7 cards of one color
        9. 1 set of 5 + 1 set of 2
        10. 1 set of 5 + 1 set of 3
        """
