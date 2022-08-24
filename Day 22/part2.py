from collections import deque
from itertools import islice

def main():
    data = open("22.txt", "r").read().rstrip('\n\n')

    players = {}
    for p, d in enumerate(data.split("\n\n")):
        players[p] = []
                
        player = []
        for line in d.splitlines()[1:]:
            player.append(int(line))
        
        players[p] = deque(player)

    game = Game(players)
    game.play()

    print(game.calc_result())

class Game:
    def __init__(self, players):
        self.players = players
        self.continue_game = True
        self.round_images = []

    def play(self):
        while self.continue_game:
            if self.decide_continue() and self.check_round_image():
                self.round_cards = [self.players[player].popleft() for player in self.players]

                if self.check_sub_game_rule():
                    self.winner = self.play_a_sub_game()
                else:
                    self.winner = self.normal_round()

                self.update_players()

    def play_a_sub_game(self):
        sub_game_player_config = {p: deque(islice(self.players[p], card)) for p, card in zip(self.players, self.round_cards)}
        sub_game = Game(sub_game_player_config)
        sub_game.play()

        return sub_game.winner

    def check_sub_game_rule(self):
        do_a_sub_game = True
        for player, drawn_card in zip(self.players, self.round_cards):
            if len(self.players[player]) < drawn_card:
                do_a_sub_game = False
                break
                
        return do_a_sub_game

    def normal_round(self):
        return max(enumerate(self.round_cards), key = lambda x: x[1])[0]
        
    def update_players(self):
        # Append the card based on who won the round
        self.players[self.winner].extend(reversed(self.round_cards) if self.winner == 1 else self.round_cards)

    def create_round_image(self):
        round_image = tuple(["".join(map(str, self.players[x])) for x in self.players])
        return round_image

    def check_round_image(self):
        round_image  = self.create_round_image()

        if round_image in self.round_images:
            self.continue_game = False
            self.winner = 0

        else:
            self.round_images.append(round_image)
        
        return self.continue_game

    def decide_continue(self):
        for player in self.players:
            if len(self.players[player]) == 0:
                self.continue_game = False
        
        return self.continue_game

    def calc_result(self):
        result = 0

        for i, x in enumerate(self.players[self.winner]):
            result += (len(self.players[self.winner]) - i) * x

        return result


main()