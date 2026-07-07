import json
from commands.base import BaseCommand
from commands import NoopCmd

class TournamentReportCmd(BaseCommand):
    name = "tournament-report"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament

        # ⭐ FIX: preserve index 0 correctly
        index = (
            self.tournament_index
            if self.tournament_index is not None
            else kwargs.get("tournament_index")
        )

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        print("\n====================================")
        print(f"      TOURNAMENT REPORT")
        print("====================================")
        print(f"Name: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Dates: {tournament.start_date} → {tournament.end_date}")
        print(f"Total Rounds: {tournament.total_rounds}")
        print(f"Current Round: {tournament.current_round}")
        print("------------------------------------")

        # -----------------------------
        # PLAYER STANDINGS
        # -----------------------------
        print("\nPLAYER STANDINGS (sorted by points):")
        sorted_players = sorted(tournament.players, key=lambda p: p.points, reverse=True)

        for p in sorted_players:
            print(f"- {p.name} ({p.chess_id}) — {p.points} points")

        # -----------------------------
        # ROUNDS AND MATCHES
        # -----------------------------
        print("\nROUNDS AND MATCHES:")
        for rnd in tournament.rounds:
            print(f"\nRound {rnd.round_number}:")
            for m in rnd.matches:
                p1 = m.player1.name
                p2 = m.player2.name

                if m.result is None:
                    result_text = "Not played yet"
                elif m.result == "1":
                    result_text = f"{p1} defeated {p2}"
                elif m.result == "2":
                    result_text = f"{p2} defeated {p1}"
                elif m.result == "T":
                    result_text = f"{p1} and {p2} tied"

                print(f"  - {p1} vs {p2} → {result_text}")

        print("\n====================================")
        print("End of Report")
        print("====================================\n")

        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )
