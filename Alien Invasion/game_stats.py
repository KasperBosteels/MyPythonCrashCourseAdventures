

class Game_stats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.ships_left = self.settings.ship_limit
        self.level = 1
        self.check_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def check_high_score(self):
        try:
            with open("./memory/high_score.txt") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        if(self.score > self.high_score):
            try:
                with open("./memory/high_score.txt", "w") as f:
                    f.write(str(self.score))
            except FileNotFoundError:
                print("Error saving high score")