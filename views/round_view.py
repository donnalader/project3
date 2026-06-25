class RoundView:
    """Handles displaying round and match information."""

    def display_round(self, round_obj):
        print(f"\n=== ROUND {round_obj.round_number} ===")
        for i, match in enumerate(round_obj.matches, start=1):
            print(f"{i}. {match.player1.name} vs {match.player2.name} — Result: {match.result}")

    def ask_for_match_result(self, match):
        print(f"\nEnter result for: {match.player1.name} vs {match.player2.name}")
        print("1 = Player 1 wins")
        print("2 = Player 2 wins")
        print("T = Tie")
        return input("Result: ").strip()
