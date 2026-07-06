import json
from commands import NoopCmd
from screens.base_screen import BaseScreen
from models.tournament import Tournament


class TournamentMenu(BaseScreen):

    def __init__(self, **kwargs):
        pass

    def load_json(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def display(self):
        print("\n=== TOURNAMENT MENU ===")

        # Load tournaments
        in_progress_data = self.load_json("data/tournaments/in-progress.json")
        completed_data = self.load_json("data/tournaments/completed.json")

        active = [Tournament.from_dict(t) for t in in_progress_data]
        completed = [Tournament.from_dict(t) for t in completed_data]

        all_tournaments = active + completed
        all_tournaments.sort(key=lambda t: t.start_date, reverse=True)

        # Auto-open active tournament (but DO NOT return here)
        if len(active) == 1:
            print(f"\nAuto-opening active tournament: {active[0].name}")
            self.auto_open = active[0]
            return

        self.auto_open = None

        # Show list
        if not all_tournaments:
            print("No tournaments found.")
        else:
            print("\nAvailable Tournaments:")
            for idx, t in enumerate(all_tournaments, 1):
                status = "ACTIVE" if t in active else "COMPLETED"
                print(f"{idx}. {t.name} ({t.start_date}) — {status}")

        print("\nN. Create new tournament")
        print("X. Back to main menu")

        self.all_tournaments = all_tournaments

    def get_command(self):
        # If exactly one active tournament → return the command here
        if self.auto_open:
            return NoopCmd("tournament-actions", tournament=self.auto_open)

        value = self.input_string("Select an option: ").strip()

        if value.upper() == "N":
            return NoopCmd("tournament-create")

        if value.upper() == "X":
            return NoopCmd("main-menu")

        if value.isdigit():
            index = int(value) - 1
            if 0 <= index < len(self.all_tournaments):
                return NoopCmd("tournament-actions", tournament=self.all_tournaments[index])

        print("Invalid selection.")
        return NoopCmd("tournament-menu")
