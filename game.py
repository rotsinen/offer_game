"""
Markus Takkinen, rotsinen@proton.me
"""

"Player class"

class Player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def change_score(self, points):
        "Points can be negative"
        self.score += points

    def name(self):
        return self.name

    def score(self):
        return self.score
    
    def __str__(self):
        return f"{self.name} {self.score}point(s)"


class Game():
    def __init__(self):
        self.player_amount = 0
        self.players = []
        self.round = 17
        self.sum = 0


    def player_max(self):
        "Defining the number of players"
        while True:
            try:
                number_of_players = int(input("Insert the number of players: "))
                if(2<=number_of_players<=8):
                    break
                else:
                    print("Insert a number between 2 and 8")
            except:
                print("Insert a valid number!")

        self.player_amount = number_of_players


    def add_player(self, player_number):
        while True:
            try:
                player_name = str(input(f"Insert a name for player {player_number}: "))
                return player_name
            except:
                print("Enter a valid player name!")

    def init_players(self):
        self.player_max()
        for i in range(0,self.player_amount):
            current_player_amount = len(self.players) + 1
            player_name = self.add_player(current_player_amount)
            player = Player(player_name)
            self.players.append(player)

    def players(self):
        "return print(self.players[0].name)"
        pass

    def offers(self):
        print(f"Maximum offer for this round is {self.round}")
        for player in self.players:
            if(player != self.players[-1]):
                offer = make_offer(player.name, self.round, self.sum, False)
                self.offer_sum_add(offer)
            else:
                offer = make_offer(player.name, self.round, self.sum, True)


    def make_offer(self, player_name, max_offer, offer_sum, last_player):
        while True:
            try:
                offer_amount = int(input(f"Enter {player_name}'s offer for this round: "))
            except:
                print(f"Enter a valid offer!")
    
            if(not (0 <= offer_amount <= max_offer)):
                print(f"Offer must be between 0 and {max_offer}!")
                continue
            if(not last_player):
                return offer_amount
            if(max_offer - offer_sum != offer_amount):
                return offer_amount
            print(f"Last offer cannot be {max_offer - offer_sum}!")

    
    def results(self):
        pass

    def offer_round(self):
        pass

    def card_counter(self):
        return self.round

    def round_finish(self):
        self.round -= 1
        self.sum = 0

    def offer_sum(self):
        return self.sum

    def offer_sum_add(self, amount):
        self.sum += amount
        
    def game_loop(self):
        while (self.round > 0):
            self.offer_round()

 
game = Game()
game.init_players()
game.game_loop()



