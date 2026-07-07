from commands.base import BaseCommand
from commands import NoopCmd

class TournamentViewStandingsCmd(BaseCommand):
    name = "tournament-view-standings"

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

        players = tournament.players

        if not players:
            print("\nNo players found in this tournament.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        print("\n=== CURRENT STANDINGS ===")

        # Sort players by points (descending)
        sorted_players = sorted(players, key=lambda p: p.points, reverse=True)

        for rank, player in enumerate(sorted_players, start=1):
            print(f"{rank}. {player.name} — {player.points} pts")

        print("\nPress Enter to return to the Tournament Actions menu.")
        input()

        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )

