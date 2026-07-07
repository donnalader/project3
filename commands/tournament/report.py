import json
import os
from commands.base import BaseCommand
from commands import NoopCmd
from models.tournament import Tournament

class TournamentReportCmd(BaseCommand):
    name = "tournament-report"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament

        index = (
            self.tournament_index
            if self.tournament_index is not None
            else kwargs.get("tournament_index")
        )

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        print("\n=== TOURNAMENT REPORT ===")
        print(f"Name: {tournament.name}")
        print(f"Players: {len(tournament.players)}")
        print(f"Total Rounds: {tournament.total_rounds}")
        print("------------------------------------")

        # Sort players by points (descending)
        sorted_players = sorted(tournament.players, key=lambda p: p.points, reverse=True)

        print("\n=== FINAL STANDINGS ===")
        for i, player in enumerate(sorted_players, start=1):
            print(f"{i}. {player.name} - {player.points} points")

        print("\n=== ROUND DETAILS ===")
        for rnd in tournament.rounds:
            print(f"\n--- Round {rnd.round_number} ---")
            for match in rnd.matches:
                p1 = match.player1.name
                p2 = match.player2.name

                if match.result == "1":
                    result_text = f"{p1} defeated {p2}"
                elif match.result == "2":
                    result_text = f"{p2} defeated {p1}"
                elif match.result == "T":
                    result_text = f"{p1} and {p2} tied"
                else:
                    result_text = "Result not entered"

                print(result_text)

        print("\nReport complete!")

        # ============================================================
        # ⭐ EXPORT REPORT TO HTML
        # ============================================================

        html = []
        html.append("<html><head><title>Tournament Report</title>")
        html.append("<style>")
        html.append("body { font-family: Arial; margin: 20px; }")
        html.append("h1, h2 { color: #333; }")
        html.append("table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }")
        html.append("th, td { border: 1px solid #ccc; padding: 8px; }")
        html.append("th { background-color: #f2f2f2; }")
        html.append("</style></head><body>")

        html.append(f"<h1>Tournament Report: {tournament.name}</h1>")
        html.append(f"<p><strong>Players:</strong> {len(tournament.players)}</p>")
        html.append(f"<p><strong>Total Rounds:</strong> {tournament.total_rounds}</p>")

        # Standings
        html.append("<h2>Final Standings</h2>")
        html.append("<table>")
        html.append("<tr><th>Rank</th><th>Player</th><th>Points</th></tr>")
        for i, player in enumerate(sorted_players, start=1):
            html.append(f"<tr><td>{i}</td><td>{player.name}</td><td>{player.points}</td></tr>")
        html.append("</table>")

        # Round details
        html.append("<h2>Round Details</h2>")
        for rnd in tournament.rounds:
            html.append(f"<h3>Round {rnd.round_number}</h3>")
            html.append("<table>")
            html.append("<tr><th>Player 1</th><th>Player 2</th><th>Result</th></tr>")

            for match in rnd.matches:
                p1 = match.player1.name
                p2 = match.player2.name

                if match.result == "1":
                    result_text = f"{p1} defeated {p2}"
                elif match.result == "2":
                    result_text = f"{p2} defeated {p1}"
                elif match.result == "T":
                    result_text = "Tie"
                else:
                    result_text = "Not entered"

                html.append(f"<tr><td>{p1}</td><td>{p2}</td><td>{result_text}</td></tr>")

            html.append("</table>")

        html.append("</body></html>")

        # Ensure reports folder exists
        os.makedirs("reports", exist_ok=True)

        filename = f"reports/tournament_{index}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(html))

        print(f"\nHTML report saved to: {filename}")

        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )
