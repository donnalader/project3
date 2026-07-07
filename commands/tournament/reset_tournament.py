import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.tournament import Tournament

class ResetTournamentCmd(BaseCommand):
    name = "tournament-reset"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):
        tournament = self.tournament

        # ⭐ FIX: preserve index 0 correctly
        index = (
            self.tournament_index
            if self.tournament_index is not None
            else kwargs.get("tournament_index")
        )

        print("\nAre you sure you want to reset this tournament?")
        print("This will clear all rounds and all player points.")
        confirm = input("Type YES to confirm: ")

        if confirm != "YES":
            print("Reset cancelled.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Reset rounds and points
        tournament.rounds = []
        tournament.current_round = 0

        for p in tournament.players:
            p.points = 0

        # ⭐ FIX: Save to correct file
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nTournament has been reset successfully!")

        # ⭐ FIX: Reload updated tournament so UI sees reset state
        with open("data/tournaments/in-progress.json", "r") as f:
            updated_data = json.load(f)

        updated_tournament = Tournament.from_dict(updated_data[index])

        return NoopCmd(
            "tournament-actions",
            tournament=updated_tournament,
            tournament_index=index
        )
