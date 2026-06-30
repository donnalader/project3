class TournamentLoad:
    """Screen for loading a tournament"""

    def __init__(self, tournaments=None, **kwargs):
        self.tournaments = tournaments or []

    def run(self):
        print("=== Load Tournament ===")
        if not self.tournaments:
            print("No tournaments available to load.")
            from commands import NoopCmd
            return NoopCmd("tournament-menu")

        for i, t in enumerate(self.tournaments, start=1):
            print(f"{i}. {t}")

        choice = input("Select a tournament number to load: ")
        try:
            idx = int(choice) - 1
            selected = self.tournaments[idx]
            print(f"Tournament '{selected}' loaded successfully!")
        except (ValueError, IndexError):
            print("Invalid choice.")

        # Return to tournament menu
        from commands import NoopCmd
        return NoopCmd("tournament-menu")
