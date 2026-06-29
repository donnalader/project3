import json
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament

class LoadTournamentCommand:
    def __init__(self):
        self.view = TournamentView()

    def execute(self):
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)

        tournaments = [Tournament.from_dict(t) for t in data]

        self.view.display_tournament_list(tournaments)
        selection = int(self.view.ask_for_tournament_selection()) - 1

        tournament = tournaments[selection]

        print("\nTournament loaded:")
        self.view.display_tournament(tournament)

        # Here you could call a TournamentDetailsMenuController
