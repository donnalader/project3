import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.tournament import Tournament

class TournamentEnterResultsBulkCmd(BaseCommand):
    name = "tournament-enter-results-bulk"

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

        # No rounds yet
        if tournament.current_round == 0 or len(tournament.rounds) == 0:
            print("\nNo rounds have been generated yet.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Get current round
        current_round_number = tournament.current_round
        current_round = tournament.rounds[current_round_number - 1]

        print(f"\n=== ENTER RESULTS FOR ROUND {current_round_number} ===")
        print("Enter results for each match:")
        print("  1 = Player 1 wins")
        print("  2 = Player 2 wins")
        print("  T = Draw")
        print("------------------------------------")

        # Collect results
        results = []

        for i, match in enumerate(current_round.matches, start=1):
            p1 = match.player1
            p2 = match.player2

            print(f"\nMatch {i}: {p1.name} vs {p2.name}")

            if match.result is not None:
                print(f"Existing result: {match.result} (will be overwritten)")

            while True:
                result = input("Result (1/2/T): ").strip().upper()
                if result in ("1", "2", "T"):
                    results.append(result)
                    break
                print("Invalid input. Please enter 1, 2, or T.")

        # Apply results
        for match, result in zip(current_round.matches, results):
            match.result = result

            if result == "1":
                match.player1.points += 1
            elif result == "2":
                match.player2.points += 1
            elif result == "T":
                match.player1.points += 0.5
                match.player2.points += 0.5

        # ⭐ FIX: Save to correct file
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nAll results saved successfully!")

        # ⭐ FIX: Reload updated tournament so UI sees new results
        with open("data/tournaments/in-progress.json", "r") as f:
            updated_data = json.load(f)

        updated_tournament = Tournament.from_dict(updated_data[index])

        return NoopCmd(
            "tournament-actions",
            tournament=updated_tournament,
            tournament_index=index
        )
