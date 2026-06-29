class MatchView:
    """View for displaying match information."""

    def display_match(self, match):
        print("\n=== MATCH ===")
        print(f"{match.player1.name} vs {match.player2.name}")
        print(f"Result: {match.result if match.result else 'Not played'}")

    def display_match_list(self, matches):
        print("\n=== MATCHES ===")
        for i, m in enumerate(matches, start=1):
            result = m.result if m.result else "Not played"
            print(f"{i}. {m.player1.name} vs {m.player2.name} — {result}")

    def ask_for_match_selection(self):
        return input("Select a match number: ").strip()
