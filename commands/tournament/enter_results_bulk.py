import json
from commands.base import BaseCommand
from commands import NoopCmd


class TournamentEnterResultsBulkCmd(BaseCommand):
    name = "tournament-enter-results-bulk"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament
        index = self.tournament_index or kwargs.get("tournament_index")

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        # No rounds yet
        if tournament.current_round == 0 or len(tournament.rounds) == 0:
            print("\nNo rounds have been generated yet.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

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

            # Show match
            print(f"\nMatch {i}: {p1.name} vs {p2.name}")

            # If already has a result, show it and allow overwrite
            if match.result is not None:
                print(f"Existing result: {match.result} (will be overwritten)")

            # Input loop
            while True:
                result = input("Result (1/2/T): ").strip().upper()
                if result in ("1", "2", "T"):
                    results.append(result)
                    break
                print("Invalid input. Please enter 1, 2, or T.")

        # Apply results
        for match, result in zip(current_round.matches, results):
            match.result = result

            # Update points
            if result == "1":
                match.player1.points += 1
            elif result == "2":
                match.player2.points += 1
            elif result == "T":
                match.player1.points += 0.5
                match.player2.points += 0.5

        # Save tournament
        with open("data/tournaments.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\nAll results saved successfully!")

        return NoopCmd("tournament-actions",
                       tournament=tournament,
                       tournament_index=index)
