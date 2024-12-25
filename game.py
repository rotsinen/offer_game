"""
Markus Takkinen, rotsinen@proton.me
"""

def players_set_amount():
    "Defining the number of players"
    while True:
        try:
            number_of_players = int(input("Insert the number of players: "))
            if(2<=number_of_players<=8):
                return number_of_players
            else:
                print("Insert a number between 2 and 8")
        except:
            print("Insert a valid number!")


def player_add(player_number):
    while True:
        try:
            player_name = str(input(f"Insert a name for player {player_number}: "))
            if (len(player_name) > 2):
                return player_name
            print("Playername must be longer than 2 letters.")

        except:
            print("Enter a valid player name!")


def offer_make(player_name, max_offer, offer_sum, last_player):
    while True:
        try:
            offer_amount = int(input(f"Enter {player_name}'s offer for this round: "))
        except:
            print(f"Enter a valid offer!")

        try:
            if(not (0 <= offer_amount <= max_offer)):
                print(f"Offer must be between 0 and {max_offer}!")
                continue
            if(not last_player):
                return offer_amount
            if(max_offer - offer_sum != offer_amount):
                return offer_amount
            print(f"Last offer cannot be {max_offer - offer_sum}!")

        except:
            print("Aswer cannot be 'enter'!")

def win_or_lose(player):
    while True:
        try:
            win_cond = input(f"Did player {player.name} win? (y/n) \n")
            if (win_cond not in ("y", "n")):
                print("Enter a valid answer!")
            elif (win_cond == "y"):
                return True
            elif (win_cond == "n"):
                return False
        except:
                print("Answer is not valid!")



"Player class"
class Player():
    def __init__(self, name, score=0, offer=0):
        self.name = name
        self.score = score
        self.offer = offer

    def score_change(self, win=True):
        if win:
            self.score += self.offer + 10
        else:
            self.score -= self.offer

    def offer_reset(self):
        self.offer = 0

    def offer_set(self, value):
        self.offer = value

    def name(self):
        return self.name

    def score(self):
        return self.score

    def offer(self):
        return self.offer
    
    def __str__(self):
        return f"{self.name} {self.score}point(s)"

"Game class"

class Game():
    def __init__(self):
        self.player_amount = 0
        self.players = []
        self.round = 17
        self.sum = 0


    def players_init(self):
        self.player_amount = players_set_amount()
        for i in range(0,self.player_amount):
            current_player_number = len(self.players) + 1
            player_name = player_add(current_player_number)
            player = Player(player_name)
            self.players.append(player)

    def offer_round(self):
        print(f"Maximum offer for this round is {self.round}")
        for player in self.players:
            if(player != self.players[-1]):
                offer = offer_make(player.name, self.round, self.sum, False)
                self.offer_sum_add(offer)
            else:
                offer = offer_make(player.name, self.round, self.sum, True)

            player.offer_set(offer)

    def results(self):
        for player in self.players:
            win_cond = win_or_lose(player)
            player.score_change(win_cond)
            player.offer_reset()

            print(f"{player.name} has now {player.score} point(s)!")


    def round_finish(self):
        self.round -= 1
        self.sum = 0

   
    def round_game(self):
        self.offer_round()
        self.results()
        self.round_finish()


    def card_counter(self):
        return self.round

    def offer_sum(self):
        return self.sum

    def offer_sum_add(self, amount):
        self.sum += amount
        
    def game(self):
        self.players_init()
        while (self.round > 0):
            self.round_game()

 
game = Game()
game.game()


