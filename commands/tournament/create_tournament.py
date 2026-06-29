import json
from commands.base_command import BaseCommand
from commands import NoopCmd
from screens.tournament.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentCreateCmd(BaseCommand):
    name = "tournament-create"

    def execute(self, app, **kwargs):
        view = TournamentView()

        name, venue, start, end, rounds = view.ask_for_new_tournament_info()

        tournament = Tournament(
            name=name,
            venue=venue,
            start_date=start,
            end_date=end,
            total_rounds=int(rounds),
            players=[],
            rounds=[]
        )

        # Load existing tournaments
        try:
            with open("data/tournaments.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        # Save new tournament
        data.append(tournament.to_dict())

        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nTournament created and saved.")

        return NoopCmd("tournament-menu")

