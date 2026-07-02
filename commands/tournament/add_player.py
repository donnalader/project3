import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.player import Player

class TournamentAddPlayerCmd(BaseCommand):
    name = "tournament-add-player"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        # Tournament is already stored in the command
        tournament = self.tournament

        if tournament is None:
            print("Error: No tournament loaded. Please load a tournament first.")
            return NoopCmd("tournament-menu")

        # Tournament index comes from the command OR kwargs
        index = self.tournament_index or kwargs.get("tournament_index")

        if index is None:
            print("Error: Tournament index missing.")
            return NoopCmd("tournament-menu")

        print("\nEnter player details:")

        name = input("Name: ").strip()
        email = input("Email: ").strip()
        chess_id = input("Chess ID: ").strip()
        birthday = input("Birthday (DD-MM-YYYY): ").strip()

        if not name:
            print("Player name cannot be empty.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Create Player object
        new_player = Player(
            name=name,
            email=email,
            chess_id=chess_id,
            birthday=birthday
        )

        # Add to tournament
        tournament.players.append(new_player)

        # Load tournaments JSON
        try:
            with open("data/tournaments.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Error: tournaments.json missing.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Replace the correct tournament entry
        data[index] = tournament.to_dict()

        # Save JSON
        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nPlayer '{name}' added to tournament '{tournament.name}'.")

        return NoopCmd("tournament-actions",
                       tournament=tournament,
                       tournament_index=index)

