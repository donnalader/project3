class RoundView:
    """View for displaying round information and collecting match results."""

    def display_round(self, round_obj):
        print(f"\n=== ROUND {round_obj.round_number} ===")
        for i, match in enumerate(round_obj.matches, start=1):
            result = match.result if match.result else "Not played"
            print(f"{i}. {match.player1.name} vs {match.player2.name} — {result}")

    def ask_for_match_result(self, match):
        print(f"\nEnter result for: {match.player1.name} vs {match.player2.name}")
        print("1 = Player 1 wins")
        print("2 = Player 2 wins")
        print("T = Tie")
        return input("Result: ").strip()
