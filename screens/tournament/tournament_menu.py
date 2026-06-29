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
            return NoopCmd("tournament-list")

        elif value == "2":
            return NoopCmd("tournament-create")

        elif value == "3":
            return NoopCmd("tournament-load")

        elif value.upper() == "X":
            return NoopCmd("main-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-menu")
