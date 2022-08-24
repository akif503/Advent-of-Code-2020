from collections import deque
from pprint import pprint

def main():
    data = open("22.txt", "r").read().rstrip('\n\n')

    game = Game(data)
    game.play()

    print(game.calc_result())


class Game:
    def __init__(self, data):
        self.players = {}

        for p, d in enumerate(data.split("\n\n")):
            self.players[p] = []
                    
            player = []
            for line in d.splitlines()[1:]:
                player.append(int(line))
            
            self.players[p] = deque(player)
            self.continue_game = True

    def play(self):

        while self.continue_game:
            if self.decide_continue():
                self.round()

    def round(self):
        # This variable shows winner of this round.
        # The winner of the final round will be the winner of the game.
        # So, it can also be used do find the winner of the game in the end

        self.winner = 0
        cards = []
        for player in self.players:
            card = self.players[player].popleft()

            if len(cards) > 0: 
                self.winner = player if card > cards[-1] else 0

            cards.append(card)
        
        # Append the card based on who won the round
        self.players[self.winner].extend(reversed(cards) if self.winner == 1 else cards)

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