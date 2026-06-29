import json
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament

class CreateTournamentCommand:
    def __init__(self):
        self.view = TournamentView()

    def execute(self):
        name, venue, start, end, rounds = self.view.ask_for_new_tournament_info()

        tournament = Tournament(
            name=name,
            venue=venue,
            start_date=start,
            end_date=end,
            total_rounds=int(rounds),
            players=[],
            rounds=[]
        )

        # Save to JSON
        try:
            with open("data/tournaments.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(tournament.to_dict())

        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nTournament created and saved.")
