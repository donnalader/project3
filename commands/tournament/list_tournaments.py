import json
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament

class ListTournamentsCommand:
    def __init__(self):
        self.view = TournamentView()

    def execute(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)

        tournaments = [Tournament.from_dict(t) for t in data]
        self.view.display_tournament_list(tournaments)
