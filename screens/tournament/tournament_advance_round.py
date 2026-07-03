from screens.base_screen import BaseScreen
from commands.tournament.advance_round import TournamentAdvanceRoundCmd
from commands import NoopCmd


class TournamentAdvanceRoundScreen(BaseScreen):
    """Screen to confirm advancing to the next round."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        tournament = self.context.kwargs.get("tournament")
        print("\n=== ADVANCE ROUND ===")
        print(f"Current round: {tournament.current_round}")
        print(f"Total rounds: {tournament.total_rounds}")
        print("Advance to the next round?")
        print("Press Enter to continue or X to cancel.")

    def get_command(self):
        value = self.input_string()

        if value.upper() == "X":
            return NoopCmd("tournament-actions",
                           tournament=self.context.kwargs.get("tournament"),
                           tournament_index=self.context.kwargs.get("tournament_index"))

        return TournamentAdvanceRoundCmd(
            tournament=self.context.kwargs.get("tournament"),
            tournament_index=self.context.kwargs.get("tournament_index")
        )
