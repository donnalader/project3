import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.round import Round
from models.match import Match


class TournamentViewCurrentRoundCmd(BaseCommand):
    name = "tournament-view-current-round"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament
        index = self.tournament_index or kwargs.get("tournament_index")

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        # No rounds generated yet
        if tournament.current_round == 0 or len(tournament.rounds) == 0:
            print("\nNo rounds have been generated yet.")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Get current round
        current_round_number = tournament.current_round
        current_round = tournament.rounds[current_round_number - 1]

        print(f"\n=== CURRENT ROUND: {current_round_number} / {tournament.total_rounds} ===")

        # Display matches
        if not current_round.matches:
            print("No matches found for this round.")
        else:
            for i, match in enumerate(current_round.matches, start=1):
                p1 = match.player1
                p2 = match.player2

                # Determine result text
                if match.result is None:
                    result_text = "Not played yet"
                elif match.result == 1:
                    result_text = f"{p1.name} wins"
                elif match.result == 2:
                    result_text = f"{p2.name} wins"
                elif match.result == "T":
                    result_text = "Draw"
                else:
                    result_text = "Unknown result"

                print(f"\nMatch {i}:")
                print(f"  {p1.name} ({p1.points} pts)  vs  {p2.name} ({p2.points} pts)")
                print(f"  Result: {result_text}")

        print("\nPress Enter to return to the Tournament Actions menu.")
        input()

        return NoopCmd("tournament-actions",
                       tournament=tournament,
                       tournament_index=index)
