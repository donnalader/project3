from screens.base_screen import BaseScreen
from commands.tournament.enter_results import TournamentEnterResultsCmd
from commands import NoopCmd


class TournamentEnterResultsScreen(BaseScreen):
    """Screen to enter results for the current round."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        print("\n=== ENTER RESULTS ===")
        print("Enter results for the current round.")
        print("Press Enter to continue or X to cancel.")

    def get_command(self):
        value = self.input_string()

        if value.upper() == "X":
            return NoopCmd("tournament-actions",
                           tournament=self.context.kwargs.get("tournament"),
                           tournament_index=self.context.kwargs.get("tournament_index"))

        return TournamentEnterResultsCmd(
            tournament=self.context.kwargs.get("tournament"),
            tournament_index=self.context.kwargs.get("tournament_index")
        )
