import json
from models.player_model import Player

def load_players_from_cornville():
    """Load players from data/clubs/cornville.json."""
    path = "data/clubs/cornville.json"

    with open(path, "r") as f:
        data = json.load(f)

    # Cornville JSON stores players under the "players" key
    players_data = data.get("players", [])

    # Convert dictionaries to Player objects
    return [Player.from_dict(p) for p in players_data]


def main():
    players = load_players_from_cornville()

    chess_id = input("Enter a Chess ID: ").strip()

    found = next((p for p in players if p.chess_id == chess_id), None)

    if found:
        print("\nPlayer found:")
        print(found)
    else:
        print("\nNo player with that ID.")


if __name__ == "__main__":
    main()

