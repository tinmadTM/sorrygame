import random
playersvar = 0
class Player:
    def __init__(self, name, score=0, doubles=0):
        self.score = score
        self.name = name
        self.doubles = doubles

    def maximize_scores(self):
        scores = [player.score for player in self.game.players]
        self.maximum = max(scores)

    def swap_seven(self, leading_player):
        current_player_score = self.score
        self.score = leading_player.score
        leading_player.score = current_player_score

    def minimize_scores(self):
        scores = [player.score for player in self.game.players]
        self.minimize = min(scores)

    def swap_eleven(self, trailing_player):
        current_player_score = self.score
        self.score = trailing_player.score
        trailing_player.score = current_player_score

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def reset_score(self, other_player):
        if self.score == other_player.score:
            other_player.score = 0

    def roll_dice(self):
        input("Press ENTER to roll the dice, " +self.name+"!")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1, dice2)
        if dice1 == dice2:
            self.doubles += 1
        return dice1 + dice2

    def find_leading_player(self):
        leading_player = game.players[0]
        for player in game.players:
            if player.score > leading_player.score:
                leading_player = player
        return leading_player

    def find_trailing_player(self):
        trailing_player = game.players[0]
        for player in game.players:
            if player.score < trailing_player.score:
                trailing_player = player
        return trailing_player

    def apply_dice_moves(self, roll):
        if roll == 2 and roll + self.score <= 50:
            self.score += 2
        elif roll == 3 and roll + self.score <= 50:
            self.score += 3
        elif roll == 4:
            self.score -= 1
            if self.score < 0:
                self.score = 0
        elif roll == 5:
            self.score -= 2
            if self.score < 0:
                self.score = 0
        elif roll == 6 and roll + self.score <= 50:
            self.score += 6
        elif roll == 7:
            print("Swap with leading player!")
            leading_player = self.find_leading_player()
            self.swap_seven(leading_player)
        elif roll == 8:
            print("You've lost a turn!")
        elif roll == 9 and roll + self.score <= 50:
            self.score += 9
        elif roll == 10 and roll + self.score <= 50:
            self.score += 10
        elif roll == 11:
            print("Swap with the trailing player!")
            trailing_player = self.find_trailing_player()
            self.swap_eleven(trailing_player)
        elif roll == 12:
            self.score = 0

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.current_player_index = 0
        self.winning_spot = 50
        self.gameover = False
        self.leading_player = None
        self.leading_player_index = None
        self.maximum = None
        self.trailing_player = None
        self.trailing_player_index = None
        self.minimum = None
    def display_scores(game):
        print("Player\tScore")
        for player in game.players:
            print(f"{player.name}\t{player.score}")
    def start_game(self):
        self.players = []
        self.names = []
        for i in range(1, self.num_players + 1):
            name = input(f"Player {i}'s name: ")
            player = Player(name, 0, 0)
            self.players.append(player)
            self.names.append(name)
            print(f"{player.name} has joined the game.")
    def start_turn(self):
        global roll
        current_player = self.players[self.current_player_index]
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        roll = current_player.roll_dice()
        if current_player.doubles == 0:
            print(f"{current_player.name} has not rolled a double.")
        else:
            print(f"{current_player.name} rolled a double!.")
        if current_player.doubles > 0:
            roll = current_player.roll_dice()
            current_player.apply_dice_moves(roll)
            print(f"{current_player.name}'s score is now {current_player.score}.")
            for player in game.players:
                if player != current_player:
                    current_player.apply_dice_moves(roll)
    def play_game(self):
        self.current_player_index = 0
        while not self.gameover:
            player = self.players[self.current_player_index]
            roll = player.roll_dice()
            if player.doubles > 0:
                game.current_player_index = (game.current_player_index + 1) % game.num_players
                player.apply_dice_moves(roll)
                self.display_scores()
                for player in game.players:
                    for other_player in game.players:
                        if player.score == other_player.score and player != other_player:
                            player.reset_score(other_player)
                if self.winning_spot == player.score:
                    self.gameover = True
            else:
                print("No double yet!")
                game.current_player_index = (game.current_player_index + 1) % game.num_players
                self.display_scores() 
        if player.score == game.winning_spot:
            game.gameover = True
            print(f"{player.name} has won the game!")    
            game.current_player_index = (game.current_player_index + 1) % game.num_players
    def maximize_scores(self):
        scores = [player.score for player in self.players]
        self.maximum = max(scores)

    def swap_seven(self, leading_player):
        current_player_score = self.score
        self.score = leading_player.score
        leading_player.score = current_player_score

    def minimize_scores(self):
        scores = [player.score for player in self.players]
        self.minimize = min(scores)

    def swap_eleven(self, trailing_player):
        # Swap scores between current player and trailing player
        current_player_score = self.score
        self.score = trailing_player.score
        trailing_player.score = current_player_score
    def find_leading_player(self):
        leading_player = self.players[0]
        for player in self.players:
            if player.score > leading_player.score:
                leading_player = player
        return leading_player
    def find_trailing_player(self):
        trailing_player = self.players[0]
        for player in self.players:
            if player.score > trailing_player.score:
                trailing_player = player
        return trailing_player
def reset():
    global playersvar 
    global keepgoing
    global game
    keepgoing = True
    playersvar = 0
    while keepgoing is True:
        if playersvar <= 4 and playersvar >= 2:
            keepgoing = False
        else:
            playersvar = int(input("You need 2-4 players. How many players?: "))
            keepgoing = True
reset()
game = Game(playersvar)
game.start_game()
game.play_game()

while game.gameover==True:
    print("Congrats to the winner!")
    game.display_scores()
    goagain = input("Would you like to play again? y/n :")
    if goagain == "y":
        keepgoing = True
        game.gameover = False
        reset()
        game = Game(playersvar)
        game.start_game()
        game.play_game()
    else:
        break

