import json
from commands.base import BaseCommand
from commands import NoopCmd
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentListCmd(BaseCommand):
    name = "tournament-list"

    def execute(self, app, **kwargs):
        view = TournamentView()

        try:
            with open("data/tournaments.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("\nNo tournaments found.")
            return NoopCmd("tournament-menu")

        tournaments = [Tournament.from_dict(t) for t in data]

        view.display_tournament_list(tournaments)

        # ⭐ IMPORTANT:
        # After listing tournaments, return to the tournament menu screen
        return NoopCmd("tournament-menu")
