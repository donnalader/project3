from screens.base_screen import BaseScreen
from commands import NoopCmd

class TournamentActionsMenu(BaseScreen):
    """Actions available after loading a tournament."""

    def __init__(self, tournament=None, **kwargs):
        self.tournament = tournament or kwargs.get("tournament")

    def display(self):
        print("\n=== TOURNAMENT ACTIONS ===")
        print(f"Tournament: {self.tournament.name}")
        print("1. Add player")
        print("2. Start tournament (generate rounds)")
        print("3. Play current round")
        print("4. View rounds")
        print("X. Return to tournament menu")

    def get_command(self):
        value = self.input_string()

        if value == "1":
            from commands.tournament.add_player import TournamentAddPlayerCmd
            return TournamentAddPlayerCmd(self.tournament)

        elif value == "2":
            from commands.tournament.generate_rounds import TournamentGenerateRoundsCmd
            return TournamentGenerateRoundsCmd(self.tournament)

        elif value == "3":
            from commands.tournament.play_round import TournamentPlayRoundCmd
            return TournamentPlayRoundCmd(self.tournament)

        elif value == "4":
            from commands.tournament.view_rounds import TournamentViewRoundsCmd
            return TournamentViewRoundsCmd(self.tournament)

        elif value.upper() == "X":
            return NoopCmd("tournament-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-actions")
