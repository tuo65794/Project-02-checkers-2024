import json
from Player import Player
from SecondMenu import SecondMenu

class ScoreManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.user_scores = self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_scores(self):
        with open(self.filename, 'w') as file:
            json.dump(self.user_scores, file)


# Example usage:
score_manager = ScoreManager("scores.json")

# Create players
player1 = Player("user1")
player2 = Player("user2")

# Player 1 wins a game
player1.win = 1

# Update scores
score_manager.update_scores(player1)
score_manager.update_scores(player2)

# Save scores to file
score_manager.save_scores()

# Display user scores
print("User Scores:", score_manager.user_scores)
