from models.player_model import Player
from models.match import Match
from models.round import Round


def main():
    # Create players
    p1 = Player("Alice", "alice@example.com", "AB12345", "1990-05-12")
    p2 = Player("Bob", "bob@example.com", "CD67890", "1988-03-22")
    p3 = Player("Carol", "carol@example.com", "EF54321", "1992-11-10")
    p4 = Player("David", "david@example.com", "GH98765", "1995-07-30")

    # Create matches for Round 1
    m1 = Match(p1, p2)
    m2 = Match(p3, p4)

    # Set results
    m1.set_result("1")  # Alice wins
    m2.set_result("T")  # Tie

    # Create Round 1
    round1 = Round(round_number=1)
    round1.add_match(m1)
    round1.add_match(m2)

    # Display round info
    print("=== ROUND 1 SUMMARY ===")
    print(round1)
    for match in round1.matches:
        print(match)

    # Show points earned
    print("\n=== POINTS ===")
    for match in round1.matches:
        p1_pts, p2_pts = match.get_points()
        print(f"{match.player1.name}: {p1_pts} points")
        print(f"{match.player2.name}: {p2_pts} points")
        print("---")


if __name__ == "__main__":
    main()
