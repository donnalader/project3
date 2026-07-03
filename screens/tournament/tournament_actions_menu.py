from screens.base_screen import BaseScreen
from commands import NoopCmd

class TournamentActionsMenu(BaseScreen):
    """Actions available after loading a tournament."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        print("\n=== TOURNAMENT ACTIONS ===")
        print("1. Add player")
        print("2. View players")
        print("3. Generate rounds")
        print("4. Import players from club file")
        print("5. Enter results for current round")
        print("6. Advance to next round")
        print("7. View tournament report")
        print("8. Search players")
        print("X. Return to tournament menu")

    def get_command(self):
        value = self.input_string()

        tournament = self.context.kwargs.get("tournament")
        tournament_index = self.context.kwargs.get("tournament_index")

        if value == "1":
            from commands.tournament.add_player import TournamentAddPlayerCmd
            return TournamentAddPlayerCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )

        elif value == "2":
            from commands.tournament.view_players import TournamentViewPlayersCmd
            return TournamentViewPlayersCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )

        elif value == "3":
            from commands.tournament.generate_rounds import TournamentGenerateRoundsCmd
            return TournamentGenerateRoundsCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )

        elif value == "4":
            from commands.tournament.import_players import TournamentImportPlayersCmd
            return TournamentImportPlayersCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )
        elif value == "5":
            from commands.tournament.enter_results import TournamentEnterResultsCmd
            return TournamentEnterResultsCmd(
                tournament=tournament,
                tournament_index=tournament_index             
            )
        elif value == "6":
            from commands.tournament.advance_round import TournamentAdvanceRoundCmd
            return TournamentAdvanceRoundCmd(
                tournament=tournament,
                tournament_index=tournament_index
            ) 
        elif value == "7":
            from commands.tournament.report import TournamentReportCmd
            return TournamentReportCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )  
        elif value == "8":
            from commands.tournament.search_players import TournamentSearchPlayersCmd
            return TournamentSearchPlayersCmd(
                tournament=tournament,
                tournament_index=tournament_index
            )


        elif value.upper() == "X":
            return NoopCmd("tournament-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=tournament_index)
