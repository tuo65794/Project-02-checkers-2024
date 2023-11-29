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


