import json

from commands.base import BaseCommand
from commands import NoopCmd
from models import tournament
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentLoadCmd(BaseCommand):
    name = "tournament-load"

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
        selection = view.ask_for_tournament_selection()

        if not selection.isdigit():
            print("Invalid selection.")
            return NoopCmd("tournament-menu")

        index = int(selection) - 1

        if index not in range(len(tournaments)):
            print("Invalid selection.")
            return NoopCmd("tournament-menu")

        tournament = tournaments[index]

        print("\nTournament loaded:")
        view.display_tournament(tournament)

        kwargs["tournament"] = tournament
        return NoopCmd("tournament-actions", tournament=tournament)
