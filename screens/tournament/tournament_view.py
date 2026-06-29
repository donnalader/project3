class TournamentView:
    """View for displaying tournament information and collecting user input."""

    def display_tournament(self, tournament):
        print("\n=== TOURNAMENT INFORMATION ===")
        print(f"Name: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Dates: {tournament.start_date} → {tournament.end_date}")
        print(f"Total Rounds: {tournament.total_rounds}")
        print(f"Current Round: {tournament.current_round}")
        print(f"Registered Players: {len(tournament.players)}")

    def display_tournament_list(self, tournaments):
        print("\n=== AVAILABLE TOURNAMENTS ===")
        for i, t in enumerate(tournaments, start=1):
            print(f"{i}. {t.name} ({t.start_date} → {t.end_date})")

    def ask_for_tournament_selection(self):
        return input("Select a tournament number: ").strip()

    def ask_for_new_tournament_info(self):
        print("\n=== CREATE NEW TOURNAMENT ===")
        name = input("Tournament name: ").strip()
        venue = input("Venue: ").strip()
        start = input("Start date (YYYY-MM-DD): ").strip()
        end = input("End date (YYYY-MM-DD): ").strip()
        rounds = input("Number of rounds: ").strip()
        return name, venue, start, end, rounds
