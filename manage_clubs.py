from commands import ClubListCmd, NoopCmd, ExitCmd

from screens.clubs import ClubCreate, ClubView
from screens.players import PlayerView, PlayerEdit
from screens import MainMenu
from screens.tournament.tournament_menu import TournamentMenu

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
        "tournament-menu": TournamentMenu,

        "exit": False,
    }
   
    def __init__(self):
        # We start with the list of clubs (= main menu)
        command = ClubListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
