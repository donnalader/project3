

class TournamentView:
    """View for listing tournaments and creating new ones."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # ---------------------------------------------------------
    # DISPLAY LIST OF TOURNAMENTS
    # ---------------------------------------------------------
    def display_tournament_list(self, tournaments):
        print("\n=== TOURNAMENTS ===")

        if not tournaments:
            print("No tournaments found.")
            return

        for i, t in enumerate(tournaments, start=1):
            print(f"{i}. {t.name} ({t.start_date} → {t.end_date})")

        print("\nSelect a tournament number, or press X to cancel.")

    # ---------------------------------------------------------
    # ASK USER TO SELECT A TOURNAMENT INDEX
    # ---------------------------------------------------------
    def ask_for_tournament_index(self, tournaments):
        value = input("Choice: ").strip().upper()

        if value == "X":
            return None

        try:
            index = int(value) - 1
            if 0 <= index < len(tournaments):
                return index
        except ValueError:
            pass

        print("Invalid selection.")
        return None

    # ---------------------------------------------------------
    # ASK USER FOR NEW TOURNAMENT INFO
    # ---------------------------------------------------------
    def ask_for_new_tournament_info(self):
        print("\n=== CREATE NEW TOURNAMENT ===")

        name = input("Tournament name: ").strip()
        venue = input("Venue: ").strip()
        start = input("Start date (YYYY-MM-DD): ").strip()
        end = input("End date (YYYY-MM-DD): ").strip()

        while True:
            rounds = input("Number of rounds: ").strip()
            try:
                rounds = int(rounds)
                break
            except ValueError:
                print("Please enter a valid number.")

        return name, venue, start, end, rounds

