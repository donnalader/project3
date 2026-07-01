print("MANAGE CLUBS FILE LOADED")
from commands import ClubListCmd, NoopCmd, ExitCmd

from screens.clubs import ClubCreate, ClubView
from screens.players import PlayerView, PlayerEdit
from screens import MainMenu


from screens.tournament.tournament_menu import TournamentMenu
from screens.tournament.tournament_create import TournamentCreate
from screens.tournament.tournament_load import TournamentLoad
from screens.tournament.tournament_list import TournamentList
from commands.tournament.create_tournament import TournamentCreateCmd
from commands.tournament.list_tournaments import TournamentListCmd
from commands.tournament.load_tournament import TournamentLoadCmd


class App:
    """The main controller for the club management program"""

    SCREENS = {
        "main-menu": MainMenu,
        "club-create": ClubCreate,
        "club-view": ClubView,
        "player-view": PlayerView,
        "player-edit": PlayerEdit,
        "player-create": PlayerEdit,

        # Tournament screens
        "tournament-menu": TournamentMenu,
        "tournament-list": TournamentList, 
        "tournament-load": TournamentLoad, 
                    # Exit screen
        "exit": False,
    }

    def __init__(self):
        # Start with the list of clubs (main menu)
        command = ClubListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            screen_name = self.context.screen

            # Safety check: screen must exist
            if screen_name not in self.SCREENS:
                print(f"Unknown screen '{screen_name}'. Returning to main menu.")
                screen_name = "main-menu"

            screen = self.SCREENS[screen_name]

            # If screen is False → exit
            if screen is False:
                print("Bye!")
                break

            try:
                # Run the screen → get a command object
                command = screen(**self.context.kwargs).run()

                # Run the command → get a new Context
                self.context = command()

            except KeyboardInterrupt:
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
