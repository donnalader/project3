import json
from commands.base import BaseCommand
from commands import NoopCmd

class ResetTournamentCmd(BaseCommand):
    name = "tournament-reset"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):
        tournament = self.tournament
        index = self.tournament_index or kwargs.get("tournament_index")

        print("\nAre you sure you want to reset this tournament?")
        print("This will clear all rounds and all player points.")
        confirm = input("Type YES to confirm: ")

        if confirm != "YES":
            print("Reset cancelled.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Reset rounds and points
        tournament.rounds = []
        tournament.current_round = 0

        for p in tournament.players:
            p.points = 0

        # Save changes
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nTournament has been reset successfully!")

        return NoopCmd("tournament-actions",
                       tournament=tournament,
                       tournament_index=index)
