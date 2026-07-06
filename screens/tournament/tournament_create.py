import json
from commands import NoopCmd
from screens.base_screen import BaseScreen
from models.tournament import Tournament


class TournamentCreate(BaseScreen):
    """Screen for creating a new tournament"""

    def __init__(self, **kwargs):
        pass

    def display(self):
        print("\n=== Tournament Creation ===")

    def get_command(self):
        name = self.input_string("Enter tournament name: ")
        venue = self.input_string("Enter tournament venue: ")
        start_date = self.input_string("Enter start date (YYYY-MM-DD): ")
        end_date = self.input_string("Enter end date (YYYY-MM-DD): ")
        total_rounds = int(self.input_string("Enter number of rounds: "))

        # Create tournament object
        tournament = Tournament(
            name=name,
            venue=venue,
            start_date=start_date,
            end_date=end_date,
            total_rounds=total_rounds,
            current_round=0,
            players=[],
            rounds=[]
        )

        # Load existing in-progress tournaments
        try:
            with open("data/tournaments/in-progress.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        # Save new tournament
        data.append(tournament.to_dict())

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nTournament '{name}' created successfully!")

        # Return to tournament menu
        return NoopCmd("tournament-menu")

