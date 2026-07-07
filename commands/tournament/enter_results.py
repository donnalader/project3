import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.match import Match
from models.round import Round
from models.tournament import Tournament

class TournamentEnterResultsCmd(BaseCommand):
    name = "tournament-enter-results"

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

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        # Ensure there is a current round
        if not tournament.rounds:
            print("No rounds have been generated yet.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        current_round = tournament.rounds[-1]
        print(f"\n=== ENTER RESULTS FOR ROUND {current_round.round_number} ===")

        # Loop through matches
        for i, match in enumerate(current_round.matches, start=1):
            print(f"\nMatch {i}: {match.player1.name} vs {match.player2.name}")

            while True:
                print("Enter result:")
                print("1 = Player 1 wins")
                print("2 = Player 2 wins")
                print("T = Tie")
                result = input("Result: ").strip().upper()

                if result in ("1", "2", "T"):
                    match.set_result(result)
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or T.")

        # ⭐ FIX: Save to correct file
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nAll results recorded successfully!")

        # ⭐ FIX: Reload updated tournament so UI sees new results
        with open("data/tournaments/in-progress.json", "r") as f:
            updated_data = json.load(f)

        updated_tournament = Tournament.from_dict(updated_data[index])

        return NoopCmd(
            "tournament-actions",
            tournament=updated_tournament,
            tournament_index=index
        )
