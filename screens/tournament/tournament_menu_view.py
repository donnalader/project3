class TournamentMenuView:
    def display_menu(self):
        print("\n=== TOURNAMENT MENU ===")
        print("1. List tournaments")
        print("2. Create a new tournament")
        print("3. Load a tournament")
        print("4. Return to main menu")
        return input("Choose an option: ").strip()
