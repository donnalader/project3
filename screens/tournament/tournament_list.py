class TournamentList:
    """Screen for listing tournaments"""

    def __init__(self, tournaments=None, **kwargs):
        self.tournaments = tournaments or []

    def run(self):
        print("=== Tournament List ===")
        if not self.tournaments:
            print("No tournaments found.")
        else:
            for i, t in enumerate(self.tournaments, start=1):
                print(f"{i}. {t}")

        # Return to tournament menu
        from commands import NoopCmd
        return NoopCmd("tournament-menu")
