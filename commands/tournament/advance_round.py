import json
from commands.base import BaseCommand
from commands import NoopCmd
from commands.tournament.generate_rounds import TournamentGenerateRoundsCmd
from models.tournament import Tournament

class TournamentAdvanceRoundCmd(BaseCommand):
    name = "tournament-advance-round"

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

        # Check if tournament already completed
        if tournament.current_round >= tournament.total_rounds:
            print("\nTournament has already completed all rounds.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Confirm advancement
        print(
            f"\nYou are about to advance from Round {tournament.current_round} "
            f"to Round {tournament.current_round + 1}."
        )
        confirm = input("Are you sure? (Y/N): ").strip().upper()

        if confirm != "Y":
            print("Advance cancelled.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Advance round counter
        tournament.current_round += 1

        # ⭐ FIX: Generate next round AND capture updated tournament
        print("\nGenerating next round...")
        gen_cmd = TournamentGenerateRoundsCmd(
            tournament=tournament,
            tournament_index=index
        )
        result_cmd = gen_cmd.execute(app=app)

        # ⭐ FIX: Extract updated tournament from NoopCmd
        updated_tournament = result_cmd.kwargs.get("tournament", tournament)
        tournament = updated_tournament

        # ⭐ FIX: Save to correct file
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nRound {tournament.current_round} generated successfully!")

        return NoopCmd(
            "tournament-actions",
            tournament=tournament,
            tournament_index=index
        )

