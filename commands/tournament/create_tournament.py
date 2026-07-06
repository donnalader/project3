import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.tournament import Tournament
from screens.tournament.tournament_view import TournamentView


class TournamentCreateCmd(BaseCommand):
    name = "tournament-create"

    def execute(self, app, **kwargs):

        # Load existing tournaments
        try:
            with open("data/tournaments.json", "r") as f:
                tournaments_data = json.load(f)
        except FileNotFoundError:
            tournaments_data = []

        # Use the TournamentView to collect user input
        view = TournamentView()
        name, venue, start, end, rounds = view.ask_for_new_tournament_info()

        # Create the Tournament object
        tournament = Tournament(
            name=name,
            venue=venue,
            start_date=start,
            end_date=end,
            total_rounds=rounds,
            players=[],
            rounds=[]
        )

        # Save to JSON
        tournaments_data.append(tournament.to_dict())

        with open("data/tournaments.json", "w") as f:
            json.dump(tournaments_data, f, indent=4)

        print(f"\nTournament '{name}' created successfully!")

        # Return to tournament menu
        return NoopCmd("tournament-menu")


