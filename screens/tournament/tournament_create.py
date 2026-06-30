class TournamentCreate:
    """Screen for creating a new tournament"""

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def run(self):
        print("=== Tournament Creation ===")
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")

        # Normally you’d save this to your model here
        print(f"Tournament '{name}' created at {location}!")

        # Return to tournament menu
        from commands import NoopCmd
        return NoopCmd("tournament-menu")
