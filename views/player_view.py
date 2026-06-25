class PlayerView:
    """Handles displaying player information and collecting player-related input."""

    def display_player(self, player):
        print("\n=== PLAYER INFORMATION ===")
        print(f"Name: {player.name}")
        print(f"Email: {player.email}")
        print(f"Chess ID: {player.chess_id}")
        print(f"Birthdate: {player.birthdate}")

    def display_player_list(self, players):
        print("\n=== PLAYER LIST ===")
        for i, p in enumerate(players, start=1):
            print(f"{i}. {p.name} ({p.chess_id})")

    def ask_for_chess_id(self):
        return input("Enter a Chess ID: ").strip()

    def ask_for_player_selection(self):
        return input("Select a player number: ").strip()
