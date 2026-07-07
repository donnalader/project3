import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.player import Player
from models.tournament import Tournament

class TournamentImportPlayersCmd(BaseCommand):
    name = "tournament-import-players"

    def __init__(self, tournament, tournament_index=None, club_file=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index
        self.club_file = club_file

    def execute(self, app, **kwargs):

        tournament = self.tournament

        # ⭐ FIX: preserve index 0 correctly
        index = (
            self.tournament_index
            if self.tournament_index is not None
            else kwargs.get("tournament_index")
        )

        # Safety check
        if tournament is None or index is None:
            print("Error: Tournament or index missing.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Ask for club file if not provided
        if not self.club_file:
            club_file = input("Enter club JSON filename (e.g., club1.json): ").strip()
        else:
            club_file = self.club_file

        try:
            with open(f"data/{club_file}", "r") as f:
                club_data = json.load(f)
        except FileNotFoundError:
            print(f"Error: File '{club_file}' not found in /data.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # Validate structure
        if "players" not in club_data:
            print("Error: Club file does not contain a 'players' list.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        imported_count = 0

        for pdata in club_data["players"]:
            try:
                player = Player.from_dict(pdata)
                tournament.add_player(player)
                imported_count += 1
            except Exception as e:
                print(f"Skipping invalid player entry: {pdata} ({e})")

        # ⭐ Load tournaments JSON (correct file)
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        # Save updated tournament
        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nImported {imported_count} players from '{club_file}' into '{tournament.name}'.")

        # ⭐ FIX: Reload updated tournament so UI sees new players
        with open("data/tournaments/in-progress.json", "r") as f:
            updated_data = json.load(f)

        updated_tournament = Tournament.from_dict(updated_data[index])

        # ⭐ Always return with updated tournament
        return NoopCmd(
            "tournament-actions",
            tournament=updated_tournament,
            tournament_index=index
        )
