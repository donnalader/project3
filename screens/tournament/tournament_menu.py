from commands import NoopCmd, ExitCmd
from screens.base_screen import BaseScreen


class TournamentMenu(BaseScreen):
    """Tournament menu screen"""

    def display(self):
        print("\n=== TOURNAMENT MENU ===")
        print("1. List tournaments")
        print("2. Create a tournament")
        print("3. Load a tournament")
        print("X. Return to main menu")

    def get_command(self):
        value = self.input_string()

        if value == "1":
            from commands.tournament.list_tournaments import TournamentListCmd
            return TournamentListCmd()

        elif value == "2":
            from commands.tournament.create_tournament import TournamentCreateCmd
            return TournamentCreateCmd()

        elif value == "3":
            from commands.tournament.load_tournament import TournamentLoadCmd
            return TournamentLoadCmd()

        elif value.upper() == "X":
            return NoopCmd("main-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-menu")
