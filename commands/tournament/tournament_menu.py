from commands import NoopCmd
from commands.tournament.create_tournament import TournamentCreateCmd
from commands.tournament.list_tournaments import TournamentListCmd
from commands.tournament.load_tournament import TournamentLoadCmd
from screens.base_screen import BaseScreen


class TournamentMenu(BaseScreen):
    """Tournament menu screen"""

    def display(self):
        print("\n=== TOURNAMENT MENU ===")
        print("1. List tournaments")
        print("2. Create a tournament")
        print("3. Load a tournament")
        print("X. Return to main menu")

    def run(self):
        self.display()
        value = self.input_string()

        if value == "1":
            # MUST return actual command object
            return TournamentListCmd()

        elif value == "2":
            return TournamentCreateCmd()

        elif value == "3":
            return TournamentLoadCmd()

        elif value.upper() == "X":
            # NoopCmd is correct for screen navigation
            return NoopCmd("main-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-menu")
