import json
from commands.base import BaseCommand
from commands import NoopCmd

class TournamentViewPlayersCmd(BaseCommand):
    name = "tournament-view-players"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def execute(self, app, **kwargs):

        tournament = self.tournament

        # ⭐ FIX: index must be outside the "tournament is None" block
        index = (
            self.tournament_index
            if self.tournament_index is not None
            else kwargs.get("tournament_index")
        )

        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd("tournament-actions")

        print("\n=== REGISTERED PLAYERS ===")

        if not tournament.players:
            print("No players have been registered yet.")
        else:
            for i, player in enumerate(tournament.players, start=1):
                print(f"{i}. {player.name} ({player.chess_id}) — {player.email}")

        print("\nPress Enter to return.")
        input()

        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )

