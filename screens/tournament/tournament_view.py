class TournamentView:
    def display_tournament_list(self, tournaments):
        print("=== AVAILABLE TOURNAMENTS ===")
        for i, t in enumerate(tournaments):
            print(f"{i}. {t['name']} ({t['start_date']} → {t['end_date']})")

    def ask_for_tournament_index(self, tournaments):
        self.display_tournament_list(tournaments)
        choice = input("Select tournament index: ").strip()
        try:
            return int(choice)
        except ValueError:
            return None
