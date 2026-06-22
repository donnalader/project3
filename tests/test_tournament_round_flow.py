from models.player_model import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament


def main():
    # Create players
    p1 = Player("Alice", "alice@example.com", "AB12345", "1990-05-12")
    p2 = Player("Bob", "bob@example.com", "CD67890", "1988-03-22")
    p3 = Player("Carol", "carol@example.com", "EF54321", "1992-11-10")
    p4 = Player("David", "david@example.com", "GH98765", "1995-07-30")

    # Create tournament
    t = Tournament(
        name="Flow Test Tournament",
        venue="Richmond",
        start_date="2024-05-01",
        end_date="2024-05-03",
        total_rounds=2,
        players=[p1, p2, p3, p4]
    )

    print("=== TOURNAMENT CREATED ===")
    print(t)
    print("Current round:", t.current_round)

    # Round 1
    r1 = Round(1)
    r1.add_match(Match(p1, p2, "1"))  # Alice wins
    r1.add_match(Match(p3, p4, "T"))  # Tie
    t.add_round(r1)

    print("\n=== AFTER ROUND 1 ===")
    for match in r1.matches:
        print(match)

    # Advance to round 2
    t.advance_round()
    print("\nAdvanced to round:", t.current_round)

    # Round 2
    r2 = Round(2)
    r2.add_match(Match(p1, p3, "2"))  # Carol wins
    r2.add_match(Match(p2, p4, "1"))  # Bob wins
    t.add_round(r2)

    print("\n=== AFTER ROUND 2 ===")
    for match in r2.matches:
        print(match)

    # Final summary
    print("\n=== FINAL TOURNAMENT SUMMARY ===")
    print("Total rounds:", len(t.rounds))
    for rnd in t.rounds:
        print(rnd)
        for match in rnd.matches:
            print("  ", match)


if __name__ == "__main__":
    main()
