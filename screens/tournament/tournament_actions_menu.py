from screens.base_screen import BaseScreen


class TournamentActionsMenu(BaseScreen):
    """Menu for actions inside a loaded tournament."""

    def display(self):
        tournament = self.context.kwargs.get("tournament")
        tournament_index = self.context.kwargs.get("tournament_index")

        print("\n=== TOURNAMENT ACTIONS ===")

        if tournament:
            # Determine status
            if tournament.current_round == 0:
                status = "Not started"
            elif tournament.current_round < tournament.total_rounds:
                status = "In progress"
            else:
                status = "Completed"

            # Count players
            player_count = len(tournament.players)

            print(f"Current tournament: {tournament.name}")
            print(f"Players: {player_count}")
            print(f"Round: {tournament.current_round} / {tournament.total_rounds}")
            print(f"Status: {status}")
            print("------------------------------------")

        print("1. Add player")
        print("2. View players")
        print("3. Generate rounds")
        print("4. Import players from club file")
        print("5. Enter results for current round")
        print("6. Advance to next round")
        print("7. Tournament report")
        print("8. Search players")
        print("9. View current round")
        print("10. View standings")
        print("11. Enter all results (bulk)")
        print("X. Return to main menu")

    def get_command(self):
        from commands import NoopCmd

        tournament = self.context.kwargs.get("tournament")
        tournament_index = self.context.kwargs.get("tournament_index")

        value = input("Choice: ").strip().upper()

        if value == "1":
            from commands.tournament.add_player import TournamentAddPlayerCmd
            return TournamentAddPlayerCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "2":
            from commands.tournament.view_players import TournamentViewPlayersCmd
            return TournamentViewPlayersCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "3":
            from commands.tournament.generate_rounds import TournamentGenerateRoundsCmd
            return TournamentGenerateRoundsCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "4":
            from commands.tournament.import_players import TournamentImportPlayersCmd
            return TournamentImportPlayersCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "5":
            from commands.tournament.enter_results import TournamentEnterResultsCmd
            return TournamentEnterResultsCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "6":
            from commands.tournament.advance_round import TournamentAdvanceRoundCmd
            return TournamentAdvanceRoundCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "7":
            from commands.tournament.report import TournamentReportCmd
            return TournamentReportCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "8":
            from commands.tournament.search_players import TournamentSearchPlayersCmd
            return TournamentSearchPlayersCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "9":
            from commands.tournament.view_current_round import TournamentViewCurrentRoundCmd
            return TournamentViewCurrentRoundCmd(tournament=tournament, tournament_index=tournament_index)
        
        elif value == "10":
            from commands.tournament.view_standings import TournamentViewStandingsCmd
            return TournamentViewStandingsCmd(tournament=tournament, tournament_index=tournament_index)
        
        elif value == "11":
            from commands.tournament.enter_results_bulk import TournamentEnterResultsBulkCmd
            return TournamentEnterResultsBulkCmd(tournament=tournament, tournament_index=tournament_index)

        elif value == "X":
            return NoopCmd("main-menu")

        else:
            print("Invalid choice.")
            return NoopCmd("tournament-actions", tournament=tournament, tournament_index=tournament_index)
