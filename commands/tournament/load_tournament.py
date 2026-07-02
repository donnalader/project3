import json
from commands.base import BaseCommand
from commands import NoopCmd
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament

class TournamentLoadCmd(BaseCommand):
    name = "tournament-load"

    def execute(self, app, **kwargs):
        view = TournamentView()

        # Load tournaments JSON
        try:
            with open("data/tournaments.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("No tournaments found.")
            return NoopCmd("tournament-menu")

        if not data:
            print("No tournaments available.")
            return NoopCmd("tournament-menu")

        # Ask user which tournament to load
        index = view.ask_for_tournament_index(data)

        # Validate selection
        if index is None or index < 0 or index >= len(data):
            print("Invalid selection.")
            return NoopCmd("tournament-menu")

        # Convert dict → Tournament object
        tournament = Tournament.from_dict(data[index])

        # Store BOTH the tournament and its index
        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )

        
