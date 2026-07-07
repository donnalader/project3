import json
from commands.base import BaseCommand
from commands import NoopCmd
from models.player import Player
from models.tournament import Tournament
import os

class TournamentSearchPlayersCmd(BaseCommand):
    name = "tournament-search-players"

    def __init__(self, tournament, tournament_index=None, **kwargs):
        self.tournament = tournament
        self.tournament_index = tournament_index

    def load_all_club_players(self):
        """Load all players from all club JSON files."""
        players = []

        clubs_folder = "data/clubs"
        if not os.path.exists(clubs_folder):
            print("No clubs folder found.")
            return players

        for filename in os.listdir(clubs_folder):
            if filename.endswith(".json"):
                with open(os.path.join(clubs_folder, filename), "r") as f:
                    club_data = json.load(f)
                    for pdata in club_data.get("players", []):
                        try:
                            players.append(Player.from_dict(pdata))
                        except Exception:
                            pass

        return players

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

        print("\n=== SEARCH PLAYERS ===")
        print("Search by:")
        print("1. Chess Identifier")
        print("2. Partial Name")
        print("X. Cancel")

        choice = input("Choice: ").strip().upper()

        if choice == "X":
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        all_players = self.load_all_club_players()

        if not all_players:
            print("No club players found.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # -----------------------------
        # SEARCH BY CHESS ID
        # -----------------------------
        if choice == "1":
            cid = input("Enter Chess ID: ").strip().upper()
            matches = [p for p in all_players if p.chess_id.upper() == cid]

        # -----------------------------
        # SEARCH BY PARTIAL NAME
        # -----------------------------
        elif choice == "2":
            part = input("Enter part of name: ").strip().lower()
            matches = [p for p in all_players if part in p.name.lower()]

        else:
            print("Invalid choice.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # -----------------------------
        # DISPLAY RESULTS
        # -----------------------------
        if not matches:
            print("No matching players found.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        print("\nMatches:")
        for i, p in enumerate(matches, start=1):
            print(f"{i}. {p.name} ({p.chess_id}) — {p.email}")

        print("\nSelect a player number to register, or X to cancel.")
        sel = input("Choice: ").strip().upper()

        if sel == "X":
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        try:
            sel_index = int(sel) - 1
            player = matches[sel_index]
        except Exception:
            print("Invalid selection.")
            return NoopCmd(
                "tournament-actions",
                tournament=tournament,
                tournament_index=index
            )

        # -----------------------------
        # REGISTER PLAYER
        # -----------------------------
        tournament.add_player(player)

        # ⭐ FIX: Save to correct file
        with open("data/tournaments/in-progress.json", "r") as f:
            data = json.load(f)

        data[index] = tournament.to_dict()

        with open("data/tournaments/in-progress.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nPlayer {player.name} registered successfully!")

        # ⭐ FIX: Reload updated tournament so UI sees new player
        with open("data/tournaments/in-progress.json", "r") as f:
            updated_data = json.load(f)

        updated_tournament = Tournament.from_dict(updated_data[index])

        return NoopCmd(
            "tournament-actions",
            tournament=updated_tournament,
            tournament_index=index
        )

       