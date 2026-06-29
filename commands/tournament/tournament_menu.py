from screens.tournament.tournament_view import TournamentMenuView
from commands.tournament.list_tournaments import ListTournamentsCommand
from commands.tournament.create_tournament import CreateTournamentCommand
from commands.tournament.load_tournament import LoadTournamentCommand

class TournamentMenuController:
    def __init__(self):
        self.view = TournamentMenuView()

    def run(self):
        while True:
            choice = self.view.display_menu()

            if choice == "1":
                ListTournamentsCommand().execute()

            elif choice == "2":
                CreateTournamentCommand().execute()

            elif choice == "3":
                LoadTournamentCommand().execute()

            elif choice == "4":
                print("Returning to main menu.")
                return

            else:
                print("Invalid choice.")
