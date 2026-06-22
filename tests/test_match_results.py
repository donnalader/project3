from models.player_model import Player
from models.match import Match


def main():
    # Create players
    p1 = Player("Alice", "alice@example.com", "AB12345", "1990-05-12")
    p2 = Player("Bob", "bob@example.com", "CD67890", "1988-03-22")

    # Create match
    match = Match(p1, p2)

    print("=== MATCH BEFORE RESULT ===")
    print(match)

    # Set result
    match.set_result("1")  # Alice wins

    print("\n=== MATCH AFTER RESULT ===")
    print(match)

    # Show points
    p1_pts, p2_pts = match.get_points()
    print("\n=== POINTS ===")
    print(f"{p1.name}: {p1_pts} points")
    print(f"{p2.name}: {p2_pts} points")


if __name__ == "__main__":
    main()
