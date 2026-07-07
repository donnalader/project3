import json
from commands import NoopCmd
from screens.base_screen import BaseScreen
from models.tournament import Tournament


class TournamentMenu(BaseScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_json(self, path):
        """Load JSON safely."""
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def display(self):
        print("\n=== TOURNAMENT MENU ===")

        # -----------------------------
        # Load tournaments from correct files
        # -----------------------------
        in_progress_data = self.load_json("data/tournaments/in-progress.json")
        completed_data = self.load_json("data/tournaments/completed.json")

        # Convert dictionaries → Tournament objects
        active = [Tournament.from_dict(t) for t in in_progress_data]
        completed = [Tournament.from_dict(t) for t in completed_data]

        # Combine and sort by start date (newest first)
        all_tournaments = active + completed
        all_tournaments.sort(key=lambda t: t.start_date, reverse=True)

        self.auto_open = None
        self.all_tournaments = all_tournaments

        # -----------------------------
        # Display tournaments
        # -----------------------------
        if not all_tournaments:
            print("No tournaments found.")
        else:
            print("\nAvailable Tournaments:")
            for idx, t in enumerate(all_tournaments, 1):
                status = "ACTIVE" if t in active else "COMPLETED"
                print(f"{idx}. {t.name} ({t.start_date}) — {status}")

        print("\nN. Create new tournament")
        print("X. Back to main menu")

    def get_command(self):

        value = self.input_string("Select an option: ").strip()

        # Create new tournament
        if value.upper() == "N":
            return NoopCmd("tournament-create")

        # Back to main menu
        if value.upper() == "X":
            return NoopCmd("main-menu")

        # Select tournament by number
        if value.isdigit():
            index = int(value) - 1
            if 0 <= index < len(self.all_tournaments):
                return NoopCmd(
                    "tournament-actions",
                    tournament=self.all_tournaments[index],
                    tournament_index=index
                )

        print("Invalid selection.")
        return NoopCmd("tournament-menu")
