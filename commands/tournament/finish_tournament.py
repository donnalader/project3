import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.tournament import Tournament

class FinishTournamentCmd(BaseCommand):
    name = "finish-tournament"

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

        print("\n=== FINISH TOURNAMENT ===")

        # ---------------------------------------------------------
        # 1. Check if tournament is actually complete
        # ---------------------------------------------------------
        if tournament.current_round < tournament.total_rounds:
            print("Tournament is not finished yet.")
            print(f"Current round: {tournament.current_round}")
            print(f"Total rounds: {tournament.total_rounds}")
            return NoopCmd("tournament-actions",
                           tournament=tournament,
                           tournament_index=index)

        # Check if final round has all results
        final_round = tournament.rounds[-1]
        for match in final_round.matches:
            if match.result not in ("1", "2", "T"):
                print("Cannot finish tournament: Final round has missing results.")
                return NoopCmd("tournament-actions",
                               tournament=tournament,
                               tournament_index=index)

        print("All rounds completed and all results entered.")
        print("Moving tournament to completed.json...")

        # ---------------------------------------------------------
        # 2. Load in-progress tournaments
        # ---------------------------------------------------------
        with open("data/tournaments/in-progress.json", "r") as f:
            inprog = json.load(f)

        # ---------------------------------------------------------
        # 3. Load completed tournaments (create file if missing)
        # ---------------------------------------------------------
        try:
            with open("data/tournaments/completed.json", "r") as f:
                completed = json.load(f)
        except FileNotFoundError:
            completed = []

        # ---------------------------------------------------------
        # 4. Move tournament
        # ---------------------------------------------------------
        completed.append(tournament.to_dict())
        del inprog[index]

        # ---------------------------------------------------------
        # 5. Save both files
        # ---------------------------------------------------------
        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(inprog, f, indent=4)

        with open("data/tournaments/completed.json", "w") as f:
            json.dump(completed, f, indent=4)

        print("Tournament successfully moved to completed.json!")
        print("You may now view it in the Completed Tournaments section.")

        return NoopCmd("main-menu", clear_context=True)
