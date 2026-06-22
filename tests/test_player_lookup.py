from models.player_model import Player

def main():
    players = [
        Player("Alice", "alice@example.com", "AB12345", "1990-05-12"),
        Player("Bob", "bob@example.com", "CD67890", "1988-03-22")
    ]

    chess_id = input("Enter a Chess ID: ").strip()

    found = next((p for p in players if p.chess_id == chess_id), None)

    if found:
        print("Player found:")
        print(found)
    else:
        print("No player with that ID.")

if __name__ == "__main__":
    main()
